import gc
from inverse_kinematics.load_robotinfo import load_robotinfo
from robot_configs.generate_ros_dir import generate_ros_dir
from robot_configs.generate_ros_packages import generate_ros_packages
from robot_configs.generate_urdf import generate_urdf


if __name__ == "__main__":
    # import dh paramater
    robot_data = load_robotinfo(["Yaskawa", "GP7"])

    # generate ROS2-Ordnerstruktur
    ros_dir = generate_ros_dir(robot_data)

    # generate ROS-packages
    [cmakelists_lines, package_lines, display_launch_lines, limits_lines, rviz_lines] = generate_ros_packages(robot_data)

    # generate CMakeLists.txt
    with open(f'{ros_dir}/CMakeLists.txt', "w", encoding="utf-8") as f:
        f.write("\n".join(cmakelists_lines))

    # generate packages.xml
    with open(f'{ros_dir}/packages.xml', "w", encoding="utf-8") as f:
        f.write("\n".join(package_lines))

    # generate display.launch.py
    with open(f'{ros_dir}/launch/display.launch.py', "w", encoding="utf-8") as f:
        f.write("\n".join(display_launch_lines))

    # generate joint_limits.yaml
    with open(f'{ros_dir}/config/joint_limits.yaml', "w", encoding="utf-8") as f:
        f.write("\n".join(limits_lines))

    # generate [robot name].rviz
    with open(f'{ros_dir}/rviz/{robot_data["name"]}.rviz', "w", encoding="utf-8") as f:
        f.write("\n".join(rviz_lines))

    # generate [robot name].urdf
    urdf_lines = generate_urdf(robot_data)

    with open(f'{ros_dir}/urdf/{robot_data["name"]}.urdf', "w", encoding="utf-8") as f:
        f.write("\n".join(urdf_lines))

    gc.collect()
