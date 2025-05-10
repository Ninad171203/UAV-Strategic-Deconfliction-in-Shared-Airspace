# ----------------------------
# 4D Animation (3D + time)
# ----------------------------

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

from Assets.Scripts.drone2 import detect_conflicts, interpolate_path

def animate_4d(primary_mission, other_missions):
    """
    Animates the UAV missions in 3D space, including conflicts.
    Args:
        primary_mission: The primary drone mission
        other_missions: List of other drone missions
    """
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
