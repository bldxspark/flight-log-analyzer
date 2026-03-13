# Flight Log Analyzer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

A simple, user-friendly Streamlit web app for parsing and analyzing ArduPilot `.bin` flight logs. Extract telemetry data (vibration, battery, GPS, flight modes), generate interactive graphs, and export downloadable Excel reports for drone performance insights.

![Home Screen](images/home.png)

## Table of Contents
- [Features](#features)
- [Screenshots](#screenshots)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **Log Parsing**: Reads ArduPilot `.bin` files using `pymavlink` for accurate telemetry extraction.
- **Data Extraction**: Pulls key metrics like vibration, battery voltage/current, GPS coordinates, and flight modes.
- **Interactive Graphs**: Visualizes data with Plotly charts in the browser.
- **Excel Export**: Generates multi-sheet Excel reports via pandas and openpyxl.
- **Web UI**: Simple Streamlit interface for uploading logs and running analysis.

## Screenshots
### Home Screen
![Home Screen](images/home.png)

### Vibration and Power Graphs
![Vibration Graph](images/vibration_graph.png)
![Power Graph](images/power_graph.png)

### Upload and Analysis
![Bin File Uploaded](images/bin_file_uploaded.png)
![Report Generated](images/report_generated.png)

### Download Report
![Download Report](images/download_report.png)

## Prerequisites
- **Python**: 3.8 or higher
- **ArduPilot Log File**: A valid `.bin` log from an ArduPilot-based drone
- **Browser**: Modern web browser for the Streamlit UI

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/bldxspark/flight_log_analyzer.git
   cd flight_log_analyzer
   ```

## 🚀 Quick start
1. Create and activate a virtual environment (recommended):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python -m streamlit run app.py
   ```
4. In the browser UI, upload an ArduPilot `.bin` log and click **Run Analysis**.

(images/bin_file_uploaded.png)
(images/report_generated.png)

## 📁 Output
- Generated reports are saved under `flight_reports/report_<n>/excel/flight_data.xlsx`
- Uploaded logs are stored in `logs/`

(images/download_report.png)

## Notes
- `.venv/`, `logs/`, `flight_reports/` and Python bytecode are ignored via `.gitignore`.
