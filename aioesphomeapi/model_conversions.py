from __future__ import annotations

from typing import Any

from .api_pb2 import (  # type: ignore
    AlarmControlPanelStateResponse,
    BinarySensorStateResponse,
    ClimateStateResponse,
    CoverStateResponse,
    FanStateResponse,
    LightStateResponse,
    ListEntitiesAlarmControlPanelResponse,
    ListEntitiesBinarySensorResponse,
    ListEntitiesButtonResponse,
    ListEntitiesCameraResponse,
    ListEntitiesClimateResponse,
    ListEntitiesCoverResponse,
    ListEntitiesFanResponse,
    ListEntitiesLightResponse,
    ListEntitiesLockResponse,
    ListEntitiesMediaPlayerResponse,
    ListEntitiesNumberResponse,
    ListEntitiesSelectResponse,
    ListEntitiesSensorResponse,
    ListEntitiesServicesResponse,
    ListEntitiesSirenResponse,
    ListEntitiesSwitchResponse,
    ListEntitiesTextResponse,
    ListEntitiesTextSensorResponse,
    LockStateResponse,
    MediaPlayerStateResponse,
    NumberStateResponse,
    SelectStateResponse,
    SensorStateResponse,
    SirenStateResponse,
    SwitchStateResponse,
    TextSensorStateResponse,
    TextStateResponse,
)
from .model import (
    AlarmControlPanelEntityState,
    AlarmControlPanelInfo,
    BinarySensorInfo,
    BinarySensorState,
    ButtonInfo,
    CameraInfo,
    ClimateInfo,
    ClimateState,
    CoverInfo,
    CoverState,
    EntityInfo,
    EntityState,
    FanInfo,
    FanState,
    LightInfo,
    LightState,
    LockEntityState,
    LockInfo,
    MediaPlayerEntityState,
    MediaPlayerInfo,
    NumberInfo,
    NumberState,
    SelectInfo,
    SelectState,
    SensorInfo,
    SensorState,
    SirenInfo,
    SirenState,
    SwitchInfo,
    SwitchState,
    TextInfo,
    TextSensorInfo,
    TextSensorState,
    TextState,
)

SUBSCRIBE_STATES_RESPONSE_TYPES: dict[Any, type[EntityState]] = {
    BinarySensorStateResponse: BinarySensorState,
    CoverStateResponse: CoverState,
    FanStateResponse: FanState,
    LightStateResponse: LightState,
    NumberStateResponse: NumberState,
    SelectStateResponse: SelectState,
    SensorStateResponse: SensorState,
    SirenStateResponse: SirenState,
    SwitchStateResponse: SwitchState,
    TextStateResponse: TextState,
    TextSensorStateResponse: TextSensorState,
    ClimateStateResponse: ClimateState,
    LockStateResponse: LockEntityState,
    MediaPlayerStateResponse: MediaPlayerEntityState,
    AlarmControlPanelStateResponse: AlarmControlPanelEntityState,
}

LIST_ENTITIES_SERVICES_RESPONSE_TYPES: dict[Any, type[EntityInfo] | None] = {
    ListEntitiesBinarySensorResponse: BinarySensorInfo,
    ListEntitiesButtonResponse: ButtonInfo,
    ListEntitiesCoverResponse: CoverInfo,
    ListEntitiesFanResponse: FanInfo,
    ListEntitiesLightResponse: LightInfo,
    ListEntitiesNumberResponse: NumberInfo,
    ListEntitiesSelectResponse: SelectInfo,
    ListEntitiesSensorResponse: SensorInfo,
    ListEntitiesSirenResponse: SirenInfo,
    ListEntitiesSwitchResponse: SwitchInfo,
    ListEntitiesTextResponse: TextInfo,
    ListEntitiesTextSensorResponse: TextSensorInfo,
    ListEntitiesServicesResponse: None,
    ListEntitiesCameraResponse: CameraInfo,
    ListEntitiesClimateResponse: ClimateInfo,
    ListEntitiesLockResponse: LockInfo,
    ListEntitiesMediaPlayerResponse: MediaPlayerInfo,
    ListEntitiesAlarmControlPanelResponse: AlarmControlPanelInfo,
}
