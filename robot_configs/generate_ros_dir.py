import os
import stat

def generate_ros_dir(robot_data):
    # aktuelles Verzeichnis auslesen
    current_dir = os.path.dirname(__file__)

    # bennenung -> Name: urdf_+Robotermarke+_+Roboterbezeichnung+
    package_name = f'urdf_{robot_data["brand"]}_{robot_data["name"]}'

    # ROS-Verzeichnis definieren
    ros_dir = os.path.join(current_dir, package_name)

    # Ordnerstrukturanlegen
    os.makedirs(ros_dir, exist_ok=True)
    os.chmod(ros_dir, stat.S_IRWXU)

    # Unterordner definieren
    sub_dir = ['urdf', 'meshes', 'rviz', 'launch', 'config']

    # Unterordner anlegen
    for sub in sub_dir:
        os.makedirs(os.path.join(ros_dir, sub), exist_ok=True)
        os.chmod(os.path.join(ros_dir, sub), stat.S_IRWXU)

    return ros_dir
