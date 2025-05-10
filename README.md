# 🚁 UAV Strategic Deconfliction System

A simulation-based system to manage **strategic deconfliction** for multiple UAVs operating in shared airspace. This project is part of the **FlytBase Robotics Assignment 2025**.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Design](#system-design)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## 📝 Overview

This project simulates a **pre-flight deconfliction system** that assigns safe, non-overlapping flight paths to multiple UAVs. It ensures strategic separation to avoid mid-air conflicts in a shared 3D airspace.

---

## 🚀 Features

- 3D grid-based airspace modeling
- Pre-flight conflict detection and resolution
- Path planning using A* / Dijkstra algorithms
- Priority-based rerouting
- Console-based or GUI visualization (optional)

---

## 🧠 System Design

```text
+--------------+       +------------------+       +------------------+
| Input Parser | --->  | Conflict Checker | --->  | Path Replanner   |
+--------------+       +------------------+       +------------------+
                           |
                    +----------------+
                    | Path Allocator |
                    +----------------+
                           |
                     [Updated Flight Plans]

---


🛠️ Technologies Used

Language: Python 3.10+

Algorithms: A*, Dijkstra, BFS (based on implementation)

Libraries:

numpy, matplotlib (optional for visualization)

networkx (for graph-based path planning)

tkinter or pygame (if GUI used)

⚙️ Installation

# Clone the repository
git clone https://github.com/your-username/uav-deconfliction-system.git
cd uav-deconfliction-system

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

🧪 Usage

# Run the simulator
python main.py --input data/input.json --output data/output.json

Arguments:

--input: JSON file containing UAV flight plans

--output: JSON file with deconflicted flight plans

📊 Sample Output

{
  "uav_id": "UAV_001",
  "original_path": [...],
  "revised_path": [...],
  "status": "rerouted"
}




🧩 Future Improvements

Real-time (tactical) deconfliction support

Integration with FlytBase APIs

Dynamic obstacle avoidance

GUI-based 3D visualization

📄 License
This project is licensed under the MIT License.









👤 Author

Ninad Metkar
