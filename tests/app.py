import os
import sys
from vedo import Mesh, Plotter, show
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

def try_qt_plotter(mesh):
    try:
        print("🔧 Versuche Qt-Modus...")
        app = QApplication(sys.argv)
        window = QMainWindow()
        window.setWindowTitle("STL Viewer")
        window.setGeometry(100, 100, 800, 600)

        widget = QWidget()
        layout = QVBoxLayout()

        plotter = Plotter(qtWidget=True)
        layout.addWidget(plotter.interactor)

        widget.setLayout(layout)
        window.setCentralWidget(widget)

        plotter.show(mesh, "STL-Vorschau", axes=1, viewup="z")
        plotter.render()

        window.show()
        sys.exit(app.exec_())

    except TypeError as e:
        print("⚠️ Qt-Modus fehlgeschlagen:", e)
        return False

    return True

def main():
    stl_file = "../robot_configs/urdf_yaskawa_gp7/meshes/base_link_fixed.stl"
    full_path = os.path.abspath(stl_file)
    print(f"📂 Lade STL-Datei: {full_path}")

    mesh = Mesh(full_path)
    if mesh is None or mesh.npoints == 0:
        print("❌ STL konnte nicht geladen werden oder ist leer.")
        return

    mesh.color("lightblue").lineWidth(1)

    if not try_qt_plotter(mesh):
        print("🔁 Fallback auf normalen Viewer...")
        show(mesh, "Fallback STL Viewer", axes=1, viewup="z")

if __name__ == "__main__":
    print("🚀 main block reached")
    main()
