# data models
# ----------------------------
# Data Models
# ----------------------------

from dataclasses import dataclass

@dataclass
class Waypoint:
    x: float
    y: float
    z: float
    time: float

@dataclass
class DroneMission:
    id: str
    waypoints: list  # List[Waypoinnt]
