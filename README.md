# HackIndia-Spark-3-2025-Byte-Me
This repository contains the code for Hackindia 2025 track singularity net problem statement 2 - Optimal Flight Route Finder

# ✈️ Flight Path Finder

A web-based application that helps users find the shortest flight path between Indian airports using interactive maps and real-time route calculations.

## 🚀 Features

| Feature                 | Description |
|-------------------------|-------------|
| 🗺️ **Interactive Map**  | Displays Indian airports with flight routes on a Leaflet-based map. |
| 🔍 **Find Shortest Path** | Computes and displays the shortest flight path between selected airports. |
| ⏳ **Travel Time Calculation** | Estimates total travel time based on predefined flight durations. |
| 📍 **Real-time Airport Data** | Provides an up-to-date list of Indian airports with geolocation data. |

## 🏗️ Tech Stack

| Technology | Usage |
|------------|-------------|
| **Python (Flask)** | Backend server for API handling. |
| **JavaScript (ES6+)** | Core logic for flight path calculations and interactivity. |
| **Leaflet.js** | For rendering the interactive map. |
| **HTML/CSS** | Frontend UI structure and styling. |
| **MeTTa** | Used for declarative rule-based shortest path computation. |

## 📂 Project Structure

```
📦 flight-path-finder
├── 📁 templates         # HTML Templates
│   ├── 📄 index.html    # Main HTML file
│
├── 📁 images            # Stores images used in the project
│   ├── 📄 plane.png     # Favicon image file 
│
├── 📄 app.py            # Flask server file
├── 📄 requirements.txt  # Python dependencies
├── 📄 README.md         # Project documentation
├── 📄 .gitignore        # Gitignore file
```

## 🛠️ How to Build and Run

### ✅ Clone the Repository
```sh
git clone https://github.com/NathanCordeiro/flight-path-finder.git
cd flight-path-finder
```

### 📌 Install Dependencies
Ensure you have Python installed, then install dependencies:
```sh
pip install -r requirements.txt
```

### ▶️ Run the Application
Start the Flask backend:
```sh
python app.py
```

The application will run on `http://127.0.0.1:5000/` (localhost:5000). Open this URL in your browser to access the app.




