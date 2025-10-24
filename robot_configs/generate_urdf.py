def generate_urdf(robot_data):
    urdf_lines = []

    # Kopf
    urdf_lines.append(f'<robot name="{robot_data["brand"]}_{robot_data["name"]}">')

    # Welt zu Base
    urdf_lines.append('    <!-- Welt -->')
    urdf_lines.append('    <link name="world"/>')
    urdf_lines.append('    <joint name="world_to_base" type="fixed">')
    urdf_lines.append('        <parent link="world"/>')
    urdf_lines.append('        <child link="base_link"/>')
    urdf_lines.append('        <origin xyz="0 0 0" rpy="0 0 0"/>')
    urdf_lines.append('    </joint>')

    # Base Link
    urdf_lines.append('    <!-- Baselink -->')
    urdf_lines.append('    <link name="base_link">')
    urdf_lines.append('        <visual>')
    urdf_lines.append('            <geometry>')
    urdf_lines.append(f'                <mesh filename="meshes/{robot_data["brand"]}/{robot_data["name"]}/base_link.step"/>')
    urdf_lines.append('            </geometry>')
    urdf_lines.append('        </visual>')
    urdf_lines.append('    </link>')

    # Gelenke und Links in Schleife
    for i in range(robot_data['num_links']):
        urdf_lines.append(f'    <joint name="joint{i+1}" type="{robot_data["joint_types"][i]}">')
        if i == 0:
            urdf_lines.append('        <parent link="base_link"/>')
        else:
            urdf_lines.append(f'        <parent link="link{i}"/>')
        urdf_lines.append(f'        <child link="link{i+1}"/>')
        urdf_lines.append(f'        <origin xyz="{robot_data["dh_params"][i]["a"]} 0 {robot_data["dh_params"][i]["d"]}" rpy="{robot_data["dh_params"][i]["alpha"]} 0 0"/>')
        urdf_lines.append('        <axis xyz="0 0 1"/>')
        urdf_lines.append(f'        <limit lower="{robot_data["joint_limits"][i]["lower"]}" upper="{robot_data["joint_limits"][i]["upper"]}" effort="{robot_data["joint_limits"][i]["effort"]}" velocity="{robot_data["joint_limits"][i]["velocity"]}"/>')
        urdf_lines.append('    </joint>')
        urdf_lines.append(f'    <!-- Link {i+1} -->')
        urdf_lines.append(f'    <link name="link{i+1}">')
        urdf_lines.append('        <visual>')
        urdf_lines.append('            <geometry>')
        urdf_lines.append(f'                <mesh filename="meshes/{robot_data["brand"]}/{robot_data["name"]}/link{i+1}.step"/>')
        urdf_lines.append('            </geometry>')
        urdf_lines.append('        </visual>')
        urdf_lines.append('    </link>')

    # Flansch to Handling (Endeffektor)
    urdf_lines.append('    <joint name="flansch_to_handling" type="fixed">')
    urdf_lines.append(f'        <parent link="link{robot_data["num_links"]}"/>')
    urdf_lines.append('        <child link="Handling"/>')
    urdf_lines.append('        <origin xyz="0 0 0" rpy="0 0 0"/>')
    urdf_lines.append('    </joint>')

    # Handling-Link (Endeffektor)
    urdf_lines.append('    <!-- Handling -->')
    urdf_lines.append('    <link name="Handling">')
    urdf_lines.append('        <visual>')
    urdf_lines.append('            <geometry>')
    urdf_lines.append(f'                <mesh filename="meshes/{robot_data["brand"]}/{robot_data["name"]}/Handling.step"/>')
    urdf_lines.append('            </geometry>')
    urdf_lines.append('        </visual>')
    urdf_lines.append('    </link>')

    # TCP (Tool Center Point)
    urdf_lines.append('    <joint name="TCP" type="fixed">')
    urdf_lines.append('        <parent link="Handling"/>')
    urdf_lines.append('        <origin xyz="0 0 0" rpy="0 0 0"/>')
    urdf_lines.append('    </joint>')

    # Schluss
    urdf_lines.append('</robot>')

    return urdf_lines
