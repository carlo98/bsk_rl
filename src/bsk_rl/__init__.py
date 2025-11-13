import gymnasium as gym
from gymnasium.envs.registration import register

from bsk_rl.gym import (
    NO_ACTION,
    ConstellationTasking,
    GeneralSatelliteTasking,
    SatelliteTasking,
    ConstellationNStepsTasking,
)

__all__ = [
    "GeneralSatelliteTasking",
    "SatelliteTasking",
    "ConstellationTasking",
    "ConstellationNStepsTasking"
]

register(
    id="GeneralSatelliteTasking-v1",
    entry_point="bsk_rl.gym:GeneralSatelliteTasking",
)

register(
    id="SatelliteTasking-v1",
    entry_point="bsk_rl.gym:SatelliteTasking",
)

register(
    id="ConstellationTasking-v1",
    entry_point="bsk_rl.gym:ConstellationTasking",
)

register(
    id="ConstellationNStepsTasking-v1",
    entry_point="bsk_rl.gym:ConstellationNStepsTasking",
)
