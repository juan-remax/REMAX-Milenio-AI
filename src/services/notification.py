from typing import Optional


class ConfirmationGuard:
    def __init__(self):
        self._pending: dict[int, dict] = {}

    async def request_confirmation(self, user_id: int, action: str, details: str) -> str:
        self._pending[user_id] = {"action": action, "details": details}
        return (
            f"⚠️ *Confirmación requerida*\n\n"
            f"*Acción:* {action}\n"
            f"*Detalle:* {details}\n\n"
            f"Responde *SÍ* para confirmar o *NO* para cancelar.\n"
            f"Esta solicitud expirará en 5 minutos."
        )

    async def confirm(self, user_id: int) -> Optional[dict]:
        return self._pending.pop(user_id, None)

    def has_pending(self, user_id: int) -> bool:
        return user_id in self._pending


confirmation_guard = ConfirmationGuard()
