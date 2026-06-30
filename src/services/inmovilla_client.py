import asyncio
import time

import httpx
from loguru import logger

from src.config.settings import settings

BASE_URL = "https://procesos.inmovilla.com/api/v1"


class InmovillaRateLimit:
    def __init__(self, max_per_minute: int):
        self.max_per_minute = max_per_minute
        self._timestamps: list[float] = []

    async def acquire(self):
        now = time.monotonic()
        self._timestamps = [t for t in self._timestamps if now - t < 60]
        if len(self._timestamps) >= self.max_per_minute:
            sleep_for = 60 - (now - self._timestamps[0])
            if sleep_for > 0:
                logger.warning(f"Inmovilla rate limit reached, waiting {sleep_for:.1f}s")
                await asyncio.sleep(sleep_for)
        self._timestamps.append(time.monotonic())


class InmovillaClient:
    def __init__(self):
        self._token = settings.inmovilla_token
        self._numagencia = settings.inmovilla_numagencia
        self._http = httpx.AsyncClient(timeout=30.0)
        self._general_limit = InmovillaRateLimit(18)
        self._enum_limit = InmovillaRateLimit(1)

    @property
    def enabled(self) -> bool:
        return bool(self._token)

    def _headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "Token": self._token,
        }

    async def _request(
        self, method: str, path: str, json_data: dict | None = None, is_enum: bool = False
    ) -> dict | list | None:
        if not self.enabled:
            logger.warning("Inmovilla token not configured — skipping API call")
            return None

        limiter = self._enum_limit if is_enum else self._general_limit
        await limiter.acquire()

        url = f"{BASE_URL}{path}"
        for attempt in range(3):
            try:
                r = await self._http.request(method, url, headers=self._headers(), json=json_data)
                if r.status_code == 408:
                    logger.warning(f"Inmovilla rate limited (408), attempt {attempt + 1}/3")
                    await asyncio.sleep(5 * (attempt + 1))
                    continue
                r.raise_for_status()
                return r.json()
            except httpx.HTTPStatusError as e:
                logger.error(f"Inmovilla HTTP error {e.response.status_code}: {e.response.text}")
                return None
            except httpx.RequestError as e:
                logger.error(f"Inmovilla request error: {e}")
                return None
        return None

    async def create_client(
        self, nombre: str, apellidos: str = "", telefono: str = "", email: str = ""
    ) -> str | None:
        data = {"nombre": nombre}
        if apellidos:
            data["apellidos"] = apellidos
        if telefono:
            data["telefono1"] = int(telefono) if telefono.isdigit() else telefono
        if email:
            data["email"] = email
        result = await self._request("POST", "/clientes/", json_data=data)
        if result and "cod_cli" in result:
            cod_cli = str(result["cod_cli"])
            logger.info(f"Cliente creado en Inmovilla: cod_cli={cod_cli}")
            return cod_cli
        return None

    async def get_client(self, cod_cli: str) -> dict | None:
        return await self._request("GET", f"/clientes/?cod_cli={cod_cli}")

    async def search_client(self, telefono: str = "", email: str = "") -> list[dict] | None:
        params = []
        if telefono:
            params.append(f"telefono={telefono}")
        if email:
            params.append(f"email={email}")
        if not params:
            return None
        qs = "&".join(params)
        result = await self._request("GET", f"/clientes/buscar/?{qs}")
        if isinstance(result, list):
            return result
        if isinstance(result, dict):
            return [result]
        return None

    async def list_properties(self) -> list[dict] | None:
        result = await self._request("GET", "/propiedades/?listado")
        if isinstance(result, list):
            return result
        return None

    async def get_property(self, cod_ofer: str) -> dict | None:
        return await self._request("GET", f"/propiedades/?cod_ofer={cod_ofer}")


inmovilla_client = InmovillaClient()
