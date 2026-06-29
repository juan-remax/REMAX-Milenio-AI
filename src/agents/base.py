from abc import ABC, abstractmethod


class BaseAgent(ABC):
    @abstractmethod
    async def handle(self, text: str, user_id: int) -> str:
        ...
