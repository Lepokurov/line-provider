import httpx

from settings import (
    BET_MAKER_API_HOST_URL,
    BET_MAKER_API_TOKEN,
    SERVICE_NAME,
)


class BetMakerClient:
    __get_change_status_event_url = f"{BET_MAKER_API_HOST_URL}/in/events/status"

    async def __aenter__(self, *args, **kwargs) -> "BetMakerClient":
        headers = {"User-Agent": SERVICE_NAME, "Authorization": f"Bearer {BET_MAKER_API_TOKEN}"}
        self._client = httpx.AsyncClient(headers=headers, follow_redirects=True)
        return self

    async def __aexit__(self, *args, **kwargs) -> None:
        await self._client.aclose()

    async def update_event_status(self, event_id, state):
        data = {"event_id": event_id, "state": state.value}
        await self._client.put(self.__get_change_status_event_url, data=data)


async def get_line_provider_client() -> BetMakerClient:
    async with BetMakerClient() as session:
        yield session
