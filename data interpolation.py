# ----------------------------
# Path Interpolation
# ----------------------------

import numpy as np

def interpolate_path(waypoints, interval=1.0):
    """
    Interpolates the path between waypoints.
    Args:
        waypoints: List of waypoints
        interval: Time interval between interpolated points
    Returns:
        List of interpolated points as (x, y, z, time) tuples.
    """
    path = []
    for i in range(len(waypoints) - 1):
        wp1, wp2 = waypoints[i], waypoints[i + 1]
        duration = wp2.time - wp1.time
        steps = max(int(duration / interval), 1)
        for s in range(steps + 1):
            t = s / steps
            x = wp1.x + t * (wp2.x - wp1.x)
            y = wp1.y + t * (wp2.y - wp1.y)
            z = wp1.z + t * (wp2.z - wp1.z)
            time = wp1.time + t * (wp2.time - wp1.time)
            path.append((x, y, z, time))
    return path
