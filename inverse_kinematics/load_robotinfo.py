import xml.etree.ElementTree as ET
import os


def load_robotinfo(target):
    # Verzeichnis des Skripts bestimmen
    current_dir = os.path.dirname(__file__)

    # Pfad von robotinfo.xml relativ zu current_dir
    file_path = os.path.join(current_dir, "..",
                             "robot_configs",
                             "robotinfo.xml"
                             )

    # Absoluten Pfad erzeugen
    file_path = os.path.abspath(file_path)

    # XML laden
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Alle robot-Elemente finden
    for robot in root.findall('robot'):
        brand = robot.attrib.get("brand")

        # Zielroboter finden
        if brand == target[0]:
            name = robot.attrib.get("name")

            if name == target[1]:
                # Alle link-Elemente finden und Anzahl Zeilen bestimmen
                joints = robot.find("joints").findall("joint")
                num_links = len(joints)

                # Werte iu dh_params aufarbeiten und in dh_params schreiben
                dh_params = []
                joint_types = []
                joint_limits = []

                for joint in joints:
                    dh = {
                        "a": float(joint.find("dh").attrib["a"]),
                        "alpha": float(joint.find("dh").attrib["alpha"]),
                        "d": float(joint.find("dh").attrib["d"]),
                        "theta": float(joint.find("dh").attrib["theta"])
                    }

                    joint_type = joint.find("type").text.strip()

                    limits = {
                        "lower": float(joint.find("limits").attrib["lower"]),
                        "upper": float(joint.find("limits").attrib["upper"]),
                        "effort": float(joint.find("limits").attrib["effort"]),
                        "velocity": float(joint.find("limits").attrib["velocity"])
                    }

                    dh_params.append(dh)
                    joint_types.append(joint_type)
                    joint_limits.append(limits)

                # Ausgabe: Anzahl gelenke & DH-Paramter
                return {
                    "brand": brand,
                    "name": name,
                    "num_links": num_links,
                    "dh_params": dh_params,
                    "joint_types": joint_types,
                    "joint_limits": joint_limits
                }

    # Wenn kein passender Roboter gefunden wurde
    raise ValueError(f"Roboter: '{target}' nicht gefunden.")
