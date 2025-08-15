from __future__ import annotations

from typing import Any, Dict, Optional
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import API_URL, API_HEADER_NAME

class PientereTuinenClient:
    def __init__(self, hass: HomeAssistant, api_key: str) -> None:
        self._hass = hass
        self._api_key = api_key
        self._session = async_get_clientsession(hass)

    async def _get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        headers = {
            API_HEADER_NAME: self._api_key,
             "accept": "application/json",
             }
        async with self._session.get(url, headers=headers, params=params, timeout=30) as resp:
            resp.raise_for_status()
            return await resp.json()

    async def fetch_latest_measurement(self) -> Optional[Dict[str, Any]]:
        data = await self._get(API_URL)
        content = data.get("content") or []
        if not content:
            return None
        return max(content, key=lambda x: x.get("measuredAt", ""))
