import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from inverse_kinematics.kinematics import forward_kinematics


def animate_arm(joint_angles, link_lengths, target=None):
    """
    Visualisiert den Arm mit matplotlib.
    """
    fig, ax = plt.subplots()
    ax.set_xlim(-sum(link_lengths)-0.5, sum(link_lengths)+0.5)
    ax.set_ylim(-sum(link_lengths)-0.5, sum(link_lengths)+0.5)
    ax.set_aspect("equal")

    line, = ax.plot([], [], "o-", lw=3)

    if target is not None:
        ax.plot(target[0], target[1], "rx", markersize=12)

    def update(frame):
        th1 = joint_angles[0] * frame / 20
        th2 = joint_angles[1] * frame / 20
        x1 = link_lengths[0] * np.cos(th1)
        y1 = link_lengths[0] * np.sin(th1)

        end_eff = forward_kinematics([th1, th2], link_lengths)

        line.set_data([0, x1, end_eff[0]], [0, y1, end_eff[1]])
        return line,

    animation.FuncAnimation(fig, update, frames=20, interval=100, blit=True)
    plt.show()
