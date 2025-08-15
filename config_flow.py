from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_API_KEY
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .const import DOMAIN, API_URL, API_HEADER_NAME

class PientereTuinenConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            api_key = user_input[CONF_API_KEY]
            valid = await self._test_api_key(self.hass, api_key)
            if valid:
                await self.async_set_unique_id("pientere_tuinen")
                self._abort_if_unique_id_configured()
                return self.async_create_entry(title="Pientere Tuinen", data={CONF_API_KEY: api_key})
            else:
                errors["base"] = "invalid_auth"
        schema = vol.Schema({vol.Required(CONF_API_KEY): str})
        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)

    async def _test_api_key(self, hass: HomeAssistant, api_key: str) -> bool:
        session = async_get_clientsession(hass)
        try:
            async with session.get(API_URL, headers={API_HEADER_NAME: api_key}, timeout=15) as resp:
                return resp.status == 200
        except Exception:
            return False
