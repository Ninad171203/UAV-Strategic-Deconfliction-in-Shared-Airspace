import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from dataclasses import dataclass
import numpy as np

# ----------------------------
# Data Models
# ----------------------------

@dataclass
class Waypoint:
    x: float
    y: float
    z: float
    time: float

@dataclass
class DroneMission:
    id: str
    waypoints: list  # List[Waypoint]

# ----------------------------
# Path Interpolation
# ----------------------------

def interpolate_path(waypoints, interval=1.0):
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

# ----------------------------
# Conflict Detection
# ----------------------------

def detect_conflicts(primary_mission, other_missions, buffer_radius=5.0):
    primary_path = interpolate_path(primary_mission.waypoints)
    conflicts = []
    for other in other_missions:
        other_path = interpolate_path(other.waypoints)
        for (x1, y1, z1, t1) in primary_path:
            for (x2, y2, z2, t2) in other_path:
                if abs(t1 - t2) <= 1.0:
                    dist = np.linalg.norm([x1 - x2, y1 - y2, z1 - z2])
                    if dist < buffer_radius:
                        conflicts.append({
                            "time": round(t1),
                            "location": (round((x1 + x2)/2, 2), round((y1 + y2)/2, 2), round((z1 + z2)/2, 2)),
                            "conflicting_drone": other.id
                        })
    return conflicts

def check_mission(primary_mission, other_missions, buffer_radius=5.0):
    conflicts = detect_conflicts(primary_mission, other_missions, buffer_radius)
    if conflicts:
        return "conflict detected", conflicts
    else:
        return "clear", []

# ----------------------------
# 4D Animation (3D + time)
# ----------------------------

def animate_4d(primary_mission, other_missions):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("4D UAV Simulation with Conflict Highlights")

    primary_path = interpolate_path(primary_mission.waypoints)
    sim_paths = [interpolate_path(m.waypoints) for m in other_missions]
    all_conflicts = detect_conflicts(primary_mission, other_missions)

    ax.set_xlim(0, 30)
    ax.set_ylim(0, 30)
    ax.set_zlim(0, 30)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    primary_dot, = ax.plot([], [], [], 'bo', label="Primary (current)")
    sim_dots = [ax.plot([], [], [], 'ro')[0] for _ in other_missions]
    time_text = ax.text2D(0.05, 0.95, '', transform=ax.transAxes)

    primary_trail, = ax.plot([], [], [], 'b--', alpha=0.5, label="Primary Trail")
    sim_trails = [ax.plot([], [], [], 'r--', alpha=0.5)[0] for _ in other_missions]

    conflict_markers = []
    for conflict in all_conflicts:
        x, y, z = conflict["location"]
        marker = ax.plot([x], [y], [z], 'kx', markersize=8, label="Conflict")[0]
        marker.set_visible(False)
        conflict_markers.append((conflict["time"], marker))

    def update(frame):
        time = frame

        # Primary position + trail
        p_now = [p for p in primary_path if round(p[3]) == time]
        p_past = [p for p in primary_path if p[3] <= time]
        if p_now:
            x, y, z = p_now[0][0], p_now[0][1], p_now[0][2]
            primary_dot.set_data([x], [y])
            primary_dot.set_3d_properties([z])
        if p_past:
            xs, ys, zs = zip(*[(p[0], p[1], p[2]) for p in p_past])
            primary_trail.set_data(xs, ys)
            primary_trail.set_3d_properties(zs)

        # Other drones
        for i, path in enumerate(sim_paths):
            s_now = [p for p in path if round(p[3]) == time]
            s_past = [p for p in path if p[3] <= time]
            if s_now:
                x, y, z = s_now[0][0], s_now[0][1], s_now[0][2]
                sim_dots[i].set_data([x], [y])
                sim_dots[i].set_3d_properties([z])
            if s_past:
                xs, ys, zs = zip(*[(p[0], p[1], p[2]) for p in s_past])
                sim_trails[i].set_data(xs, ys)
                sim_trails[i].set_3d_properties(zs)

        # Show conflicts at current time
        for t, marker in conflict_markers:
            marker.set_visible(t == time)

        time_text.set_text(f"Time: {time}s")
        return [primary_dot] + sim_dots + [primary_trail] + sim_trails + [m for _, m in conflict_markers] + [time_text]

    ani = FuncAnimation(fig, update, frames=range(0, 26), interval=500, repeat=False)
    plt.legend()
    plt.show()

# ----------------------------
# Example Test
# ----------------------------

if __name__ == "__main__":
    primary = DroneMission(
        id="Primary",
        waypoints=[
            Waypoint(0, 0, 0, 0),
            Waypoint(10, 10, 10, 10),
            Waypoint(20, 10, 20, 20)
        ]
    )

    other_drones = [
        DroneMission(
            id="Sim1",
            waypoints=[
                Waypoint(10, 0, 0, 5),
                Waypoint(10, 20, 20, 15)
            ]
        ),
        DroneMission(
            id="Sim2",
            waypoints=[
                Waypoint(25, 10, 15, 18),
                Waypoint(0, 10, 15, 25)
            ]
        )
    ]

    status, details = check_mission(primary, other_drones, buffer_radius=5.0)
    print(f"Status: {status}")
    for conflict in details:
        print(f"Conflict at {conflict['location']} with {conflict['conflicting_drone']} around {conflict['time']}s")

    animate_4d(primary, other_drones)
