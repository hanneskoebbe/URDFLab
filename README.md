# URDFLab

**URDFLab** is an experimental Python-based toolkit for visualizing and simulating industrial robots and their environments using URDF (Unified Robot Description Format).  
This project currently focuses on reachability visualization for 6-axis industrial robots, and lays the foundation for motion teaching (PTP, LIN) and servo-control simulations.

---

## 🚀 Current Features  
- Generation / handling of URDFs for 6-axis industrial robots  
- Visualization of robot

---

## 📂 Directory Structure  
Here is the current layout of the repository:

```
/URDFLab
│
├── examples/ # Example scripts and usage demos
│
├── inverse_kinematics/ # Code for inverse kinematics functions
│
├── robot_configs/ # URDF or robot parameter files (pre-configured robots)
│
├── tests/ # Unit tests / test scripts
│
├── .gitignore
├── LICENSE # MIT License
├── README.md # ← this file
├── requirements.txt # Python dependencies
└── setup.ps1 # Windows PowerShell setup script (optional)
```

---

## 🧭 Roadmap / Planned Features  
1. 🎯 **Motion teaching**: PTP (point-to-point) and LIN (linear) path definitions and simulation.  
2. 🔄 **Servo control loops**: Model servo motor dynamics (PID, feed-forward) and integrate with simulation to estimate cycle times.  
3. 🌐 **Environment simulation and interaction**: Incorporate collision checking, workspace obstacles, visualize robot + environment together.  
4. 🔌 **Toolchain integration**: Possibly support frameworks such as ROS, PyBullet or other simulation backends.  
5. 🧑‍💻 **Simple UI / GUI**: An interactive interface for visualizing, teaching paths and analysing results.

---

## 🧰 Installation
Requirement: **Python 3.10+**
  
```bash
git clone https://github.com/hanneskoebbe/URDFLab.git
cd URDFLab
pip install -r requirements.txt
```

## On Windows, you can use the PowerShell setup script:
```powershell
.\setup.ps1
```

🪪 License
This project is licensed under the MIT License.

🧑‍💻 Author
Developed by Hannes Köbbe, passionate about robotics, automation and control systems.

✨ Vision statement
“A modular open-source lab for visualizing, simulating and controlling industrial robots — from URDF to motion dynamics.”

---