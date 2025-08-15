from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import UnitOfTemperature, PERCENTAGE
from .const import DOMAIN
from .coordinator import PientereCoordinator

SENSORS = [
    SensorEntityDescription(
        key="temperatureCelsius",
        name="Pientere Tuinen Bodemtemperatuur",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="moisturePercentage",
        name="Pientere Tuinen Bodemvochtigheid",
        device_class=SensorDeviceClass.MOISTURE,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
]

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator: PientereCoordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]
    async_add_entities(PientereSensor(coordinator, desc, entry.entry_id) for desc in SENSORS)

class PientereSensor(SensorEntity):
    def __init__(self, coordinator: PientereCoordinator, description: SensorEntityDescription, entry_id: str):
        self.coordinator = coordinator
        self.entity_description = description
        self._attr_unique_id = f"{entry_id}-{description.key}"
        self._attr_name = description.name

    @property
    def native_value(self):
        value = (self.coordinator.data or {}).get(self.entity_description.key)
        if self.entity_description.key == "moisturePercentage" and value is not None:
            return round(value * 100, 1)
        return value

    @property
    def extra_state_attributes(self):
        data = self.coordinator.data or {}
        attrs = {k: data[k] for k in ("measuredAt", "latitude", "longitude") if k in data}
        return attrs

    async def async_update(self):
        await self.coordinator.async_request_refresh()
