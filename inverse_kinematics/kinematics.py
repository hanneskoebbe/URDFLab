import numpy as np


def forward_kinematics(joint_angles, link_lengths):
    """
    Berechnet die Endeffektor-Position eines 2-DOF-Arms.

    joint_angles: [theta1, theta2] (in rad)
    link_lengths: [l1, l2]
    """
    theta1, theta2 = joint_angles
    l1, l2 = link_lengths

    x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)

    return np.array([x, y])


def inverse_kinematics(target, link_lengths):
    """
    Berechnet Gelenkwinkel für ein Ziel (x, y).
    Nutzt analytische IK für 2-DOF.

    target: (x, y)
    link_lengths: [l1, l2]
    """
    x, y = target
    l1, l2 = link_lengths

    # Abstand vom Ursprung zum Ziel
    r = np.sqrt(x**2 + y**2)

    # Kosinussatz für theta2
    cos_theta2 = (r**2 - l1**2 - l2**2) / (2 * l1 * l2)
    if np.abs(cos_theta2) > 1.0:
        raise ValueError("Ziel nicht erreichbar")

    theta2 = np.arccos(cos_theta2)

    # Theta1 berechnen
    k1 = l1 + l2 * np.cos(theta2)
    k2 = l2 * np.sin(theta2)
    theta1 = np.arctan2(y, x) - np.arctan2(k2, k1)

    return np.array([theta1, theta2])
