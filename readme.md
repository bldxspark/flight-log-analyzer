# Flight Log Analyzer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

Flight Log Analyzer is a Streamlit app for parsing and analyzing ArduPilot `.bin` flight logs. It extracts telemetry such as vibration, battery data, GPS path, and flight modes, then presents interactive charts and an Excel report for download.

![Home Screen](images/home.png)

## Features

- Parse ArduPilot `.bin` logs with `pymavlink`
- Visualize vibration, power, and GPS telemetry with Plotly
- Review detected flight modes in a table
- Export analysis results to a multi-sheet Excel report
- Use a simple browser-based workflow through Streamlit

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

## Tech Stack

- Python
- Streamlit
- pymavlink
- pandas
- openpyxl
- Plotly

## Project Structure

```text
flight_log_analyzer/
|-- app.py
|-- analyzer.py
|-- requirements.txt
|-- render.yaml
|-- images/
```

## Prerequisites

- Python 3.8 or higher
- A valid ArduPilot `.bin` log file
- A modern web browser

## Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/bldxspark/flight_log_analyzer.git
   cd flight_log_analyzer
   ```

2. Create and activate a virtual environment:

   Windows PowerShell:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   python -m streamlit run app.py
   ```

## How It Works

1. Upload an ArduPilot `.bin` file in the Streamlit UI.
2. The app stores the uploaded file temporarily in `logs/`.
3. `analyzer.py` reads MAVLink messages from the log and extracts telemetry.
4. The app renders charts and tables in the browser.
5. An Excel report is generated under `flight_reports/` and exposed through a download button.

## Output

- Uploaded logs are stored in `logs/`
- Generated reports are stored in `flight_reports/report_<n>/excel/flight_data.xlsx`

## Deployment

This project is a Streamlit app, so it requires a Python server process. A plain Netlify site deployment will return a 404 because Netlify expects static files or a supported serverless architecture, and this repository does not include either.

Recommended deployment targets:

- Streamlit Community Cloud
- Render
- Railway

### Render

This repository includes `render.yaml` for Render deployment.

- Build command: `pip install -r requirements.txt`
- Start command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

To deploy on Render:

1. Push the repository to GitHub.
2. Create a new Blueprint or Web Service in Render.
3. Point it to this repository.
4. Deploy and open the generated service URL.

## Limitations

- File storage is local to the running instance, so uploaded logs and generated reports are not durable in a production cloud environment.
- Analysis currently runs synchronously in the app process, which is fine for a prototype but not ideal for a multi-user production system.

## Contributing

Contributions, improvements, and bug reports are welcome.

## Contact

Durgesh Tiwari - durgeshtiwari000x@gmail.com

Project Link: (https://github.com/bldxspark/flight-log-analyzer)
