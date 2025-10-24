import os
import trimesh

def main():
    print("Aktuelles Arbeitsverzeichnis:", os.getcwd())

    # Relativer Pfad von tests-Ordner aus
    relative_path = "robot_configs/urdf_Yaskawa_GP7/meshes/base_link_fixed.stl"

    # Absoluten Pfad ermitteln
    abs_path = os.path.abspath(relative_path)
    print(f"Relativer Pfad: {relative_path}")
    print(f"Absoluter Pfad: {abs_path}")

    # Existenz prüfen
    if not os.path.isfile(abs_path):
        print("❌ Datei existiert NICHT an diesem Pfad!")
        return
    else:
        print("✅ Datei gefunden!")

    # Versuchen, die STL mit trimesh zu laden
    try:
        mesh = trimesh.load(abs_path)
        print("✅ STL geladen!")
        print(f"Mesh info: {mesh}")
        print(f"Anzahl Vertices: {len(mesh.vertices)}")
        print(f"Anzahl Faces: {len(mesh.faces)}")
    except Exception as e:
        print("❌ Fehler beim Laden der STL:")
        print(e)

if __name__ == "__main__":
    main()
