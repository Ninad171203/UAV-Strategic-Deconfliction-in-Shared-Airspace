# 🚁 UAV Strategic Deconfliction System

A simulation-based system to manage **strategic deconfliction** for multiple UAVs operating in shared airspace. This project is part of the **FlytBase Robotics Assignment 2025**.

📌 Features

✅ Spatial and temporal conflict detection using 4D data (x, y, z, time)

✅ Conflict explanation with location, time, and conflicting drone ID

✅ Animated 3D simulation using matplotlib

✅ Conflict trails and visual conflict markers

✅ External mission input via JSON file

📁 File Structure

project_root/
             
             ├── uav_deconfliction_4d.py        # Main script
                 
                 ├── utils.py                       # JSON loader function (if separated)
                     
                     ├── missions.json                  # Input file with drone waypoints
                         
                         ├── test_conflicts.py              # Optional unit tests
                              
                              ├── README.md                      # This file
                                   
                                   ├── requirements.txt               # Dependencies
                                      
                                      └── demo.mp4                       # Optional exported animation video


🚀 How to Run

1.Install dependencies:

pip install matplotlib numpy

2.Ensure missions.json is present with proper structure.

3.Run the script:

python uav_deconfliction_4d.py

4.Optional: Export as MP4 (uncomment the writer block in the script).

📂 Sample missions.json


       {
              "primary": {
     
     "id": "Primary",
     
      "waypoints": [
      
      { "x": 0, "y": 0, "z": 0, "time": 0 },
      
      { "x": 10, "y": 10, "z": 10, "time": 10 },
      
      { "x": 20, "y": 10, "z": 20, "time": 20 }
    
    ]
  
  
        "simulated": [
  
    {
    
      "id": "Sim1",
      
      "waypoints": [
      
        { "x": 10, "y": 0, "z": 0, "time": 5 },
        
        { "x": 10, "y": 20, "z": 20, "time": 15 }
      
      ]
    
    },
    
    {
    
      
      "id": "Sim2",
      
      "waypoints": [
      
        { "x": 25, "y": 10, "z": 15, "time": 18 },
        
        { "x": 0, "y": 10, "z": 15, "time": 25 }
      
      ]
    
    }
  
  
✅ Deliverables

📁 Full Python implementation

📝 Reflection & Design Document

🎞️ Demo video with voiceover (3–5 mins)

📊 3D animated visualization with time and conflict highlights

🔬 Testing

To run optional unit tests:

python test_conflicts.py

🧠 Scalability

For real-world implementation:

Stream processing with Apache Kafka or Flink

Spatial-temporal indexing using KD-Trees or Octrees

Use of TimescaleDB or similar for time-aware querying

Real-time ingestion pipelines and fault tolerance mechanisms




#Preview 

![Screenshot 2025-05-10 204538](https://github.com/user-attachments/assets/8080a2b9-f206-41f0-94ca-c4bf3d2307c1)



👤 Author

Ninad Metkar

Assignment for Flytbase Internship.
