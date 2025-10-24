def generate_ros_packages(robot_data):

    # init cmakelists_lines
    cmakelists_lines = []

    # generiere cmakelists_lines
    cmakelists_lines.append('cmake_minimum_required(VERSION 3.5)')
    cmakelists_lines.append(f'project(urdf_{robot_data["brand"]}_{robot_data["name"]})')
    cmakelists_lines.append('\n')
    cmakelists_lines.append('find_package(ament_cmake REQUIRED)')
    cmakelists_lines.append('\n')
    cmakelists_lines.append('install(DIRECTORY "urdf" "meshes"')
    cmakelists_lines.append('    DESTINATION share/${PROJECT_NAME}')
    cmakelists_lines.append(')')
    cmakelists_lines.append('\n')
    cmakelists_lines.append('ament_package()')

    # init package_lines
    package_lines = []

    # generiere package_lines
    package_lines.append('<?xml version="1.0"?>')
    package_lines.append('<package format="2">')
    package_lines.append(f'    <name>urdf_{robot_data["brand"]}_{robot_data["name"]}</name>')
    package_lines.append('    <version>0.1.0</version>')
    package_lines.append(f'    <description>URDF description for {robot_data["brand"]} {robot_data["name"]} robot</description>')
    package_lines.append('\n')
    package_lines.append('    <maintainer email="you@example.com">Max Mustermann</maintainer>')
    package_lines.append('    <license>MIT</license>')
    package_lines.append('\n')
    package_lines.append('    <buildtool_depend>ament_cmake</buildtool_depend>')
    package_lines.append('\n')
    package_lines.append('    <export>')
    package_lines.append('    </export>')
    package_lines.append('</package>')

    # init display_launch_lines
    display_launch_lines = []

    # generiere display_launch_lines
    display_launch_lines.append('from launch import LaunchDescription')
    display_launch_lines.append('from launch_ros.actions import Node')
    display_launch_lines.append('\n')
    display_launch_lines.append('def generate_launch_description():')
    display_launch_lines.append('    return LaunchDescription([')
    display_launch_lines.append('        Node(')
    display_launch_lines.append('        package="robot_state_publisher",')
    display_launch_lines.append('        executable="robot_state_publisher",')
    display_launch_lines.append('        name="robot_state_publisher",')
    display_launch_lines.append('        output="screen",')
    display_launch_lines.append(f'        parameters=[{{"robot_description": open("urdf/{robot_data["name"]}.urdf").read()}}]')
    display_launch_lines.append('    ),')
    display_launch_lines.append('    Node(')
    display_launch_lines.append('        package="rviz2",')
    display_launch_lines.append('        executable="rviz2",')
    display_launch_lines.append('        name="rviz2",')
    display_launch_lines.append(f'        argument=["-d", "rviz/{robot_data["name"]}.rviz"],')
    display_launch_lines.append('        output="screen"')
    display_launch_lines.append('    )')
    display_launch_lines.append('])')

    # init limits_lines
    limits_lines = []

    # linit_lines generieren
    limits_lines.append('joints_limits:')
    for i in range(robot_data['num_links']):
        limits_lines.append(f'    joint{i+1}:')
        limits_lines.append('        has_velocity_limits: true')
        limits_lines.append(f'        max_velocity: {robot_data["joint_limits"][i]["velocity"]}')
        limits_lines.append('        has_acceleration_limits: false')

    # init rviz_lines
    rviz_lines = []

    # rviz-lines generieren
    rviz_lines.append('Panels:')
    rviz_lines.append('  - Class: rviz/Displays')
    rviz_lines.append('    Name: Displays')
    rviz_lines.append('  - Class: rviz/Views')
    rviz_lines.append('    Name: Views')
    rviz_lines.append('Visualization Manager:')
    rviz_lines.append('  Class: ""')
    rviz_lines.append('  Displays:')
    rviz_lines.append('    - Class: rviz/RobotModel')
    rviz_lines.append('      Name: Robot Model')
    rviz_lines.append('      Robot Description: robot_description')
    rviz_lines.append('  Fixed Frame: base_link')
    rviz_lines.append('Views:')
    rviz_lines.append('  Current:')
    rviz_lines.append('    Class: rviz/TopDownOrtho')

    return [cmakelists_lines, package_lines, display_launch_lines, limits_lines, rviz_lines]
