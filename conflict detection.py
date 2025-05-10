# ----------------------------
# Conflict Detection
# ----------------------------

import numpy as np

from Assets.Scripts.drone2 import interpolate_path


def detect_conflicts(primary_mission, other_missions, buffer_radius=5.0):
    """
    Detects conflicts between the primary mission and other drone missions.
    Args:
        primary_mission: The primary drone mission to check
        other_missions: List of other drone missions
        buffer_radius: The distance threshold for conflict detection
    Returns:
        List of conflict details
    """
    primary_path = interpolate_path(primary_mission.waypoints)
    conflicts = []
    for other in other_missions:
        other_path = interpolate_path(other.waypoints)
        for (x1, y1, z1, t1) in primary_path:
            for (x2, y2, z2, t2) in other_path:
                if abs(t1 - t2) <= 1.0:  # Checking if within 1 second
                    dist = np.linalg.norm([x1 - x2, y1 - y2, z1 - z2])
                    if dist < buffer_radius:
                        conflicts.append({
                            "time": round(t1),
                            "location": (round((x1 + x2)/2, 2), round((y1 + y2)/2, 2), round((z1 + z2)/2, 2)),
                            "conflicting_drone": other.id
                        })
    return conflicts

def check_mission(primary_mission, other_missions, buffer_radius=5.0):
    """
    Checks if the primary mission has any conflicts with other missions.
    Args:
        primary_mission: The primary drone mission to check
        other_missions: List of other drone missions
        buffer_radius: The distance threshold for conflict detection
    Returns:
        Tuple: A status message and a list of conflict details
    """
    conflicts = detect_conflicts(primary_mission, other_missions, buffer_radius)
    if conflicts:
        return "conflict detected", conflicts
    else:
        return "clear", []



