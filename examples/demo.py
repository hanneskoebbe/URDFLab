# from inverse_kinematics.kinematics import inverse_kinematics
# from inverse_kinematics.visualization import animate_arm

# if __name__ == "__main__":
#     link_lengths = [1.0, 1.0]  # zwei Glieder [m]
#     target = (1.0, 1.0)        # gewünschtes Ziel [m]

#     # IK lösen
#     joint_angles = inverse_kinematics(target, link_lengths)
#     print("Berechnete Gelenkwinkel [rad]:", joint_angles)

#     # Arm animieren
#     animate_arm(joint_angles, link_lengths, target=target)
from inverse_kinematics.load_robotinfo import load_robotinfo

if __name__ == "__main__":
    # Ziel: Roboter mit brand="Yaskawa", name="GP7"
    robot_data = load_robotinfo(["Yaskawa", "GP7"])

    print(f"Marke: {robot_data['brand']}, Modell: {robot_data['name']}")
    print(f"Anzahl Links: {robot_data['num_links']}")
    for i, link in enumerate(robot_data['dh_params'], start=1):
        print(f"Link {i}: {link}")
