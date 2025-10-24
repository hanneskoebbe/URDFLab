from vedo import load
import os

def main():
    # Relativer Pfad zur STL-Datei
    relative_path = "robot_configs/urdf_Yaskawa_GP7/meshes/link1.stl"

    abs_path = os.path.abspath(relative_path)
    print(f"📂 Absoluter Pfad zur STL-Datei:\n{abs_path}")

    if not os.path.isfile(abs_path):
        print("❌ Datei existiert nicht!")
        return

    print("📦 Versuche, STL mit vedo zu laden...")
    mesh = load(abs_path)

    if mesh is None or mesh.npoints == 0:
        print("❌ Fehler: Mesh konnte nicht geladen werden oder ist leer.")
        return

    print("✅ Mesh erfolgreich geladen mit vedo!")
    print(f"ℹ️  Punkte: {mesh.npoints}, Flächen: {mesh.ncells}")

    # Vorschau anzeigen (Fenster öffnet sich)
    mesh.color("lightblue")
    mesh.show(axes=1, viewup="z")

if __name__ == "__main__":
    main()
