from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description": open("urdf/GP7.urdf").read()}]
    ),
    Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        argument=["-d", "rviz/GP7.rviz"],
        output="screen"
    )
])