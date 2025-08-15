from __future__ import annotations

from typing import Optional
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import PientereTuinenClient
from .const import DEFAULT_UPDATE_INTERVAL
import logging

class PientereCoordinator(DataUpdateCoordinator[Optional[dict]]):
    def __init__(self, hass: HomeAssistant, client: PientereTuinenClient) -> None:
        super().__init__(
            hass,
            logger=logging.getLogger(__name__),
            name="Pientere Tuinen Coordinator",
            update_interval=DEFAULT_UPDATE_INTERVAL,
        )
        self.client = client

    async def _async_update_data(self) -> Optional[dict]:
        try:
            return await self.client.fetch_latest_measurement()
        except Exception as err:
            raise UpdateFailed(str(err)) from err
