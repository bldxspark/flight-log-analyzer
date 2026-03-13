from pathlib import Path
from pymavlink import mavutil
import pandas as pd

def analyze_log(log_file):
    print("Drone Log Analyzer Started")

    reports_folder = Path("flight_reports")
    reports_folder.mkdir(exist_ok=True)

    existing_reports = list(reports_folder.glob("report_*"))
    next_report_number = len(existing_reports) + 1

    report_folder = reports_folder / f"report_{next_report_number}"
    report_folder.mkdir()

    excel_folder = report_folder / "excel"
    excel_folder.mkdir()

    mav = mavutil.mavlink_connection(log_file)

    vibration_data = []
    power_data = []
    gps_data = []
    mode_data = []

    print("Reading log messages...")

    while True:
        msg = mav.recv_match()
        if msg is None:
            break

        msg_type = msg.get_type()

        if msg_type == "VIBE":
            vibration_data.append({
                "time": msg.TimeUS,
                "x": msg.VibeX,
                "y": msg.VibeY,
                "z": msg.VibeZ
            })

        elif msg_type == "BAT":
            power_data.append({
                "time": msg.TimeUS,
                "voltage": msg.Volt,
                "current": msg.Curr
            })

        elif msg_type == "GPS":
            gps_data.append({
                "time": msg.TimeUS,
                "lat": msg.Lat,
                "lon": msg.Lng
            })

        elif msg_type == "MODE":
            mode_data.append({
                "time": msg.TimeUS,
                "mode": msg.Mode
            })

    vibration_df = pd.DataFrame(vibration_data)
    power_df = pd.DataFrame(power_data)
    gps_df = pd.DataFrame(gps_data)
    mode_df = pd.DataFrame(mode_data)

    excel_file = excel_folder / "flight_data.xlsx"

    with pd.ExcelWriter(excel_file) as writer:
        vibration_df.to_excel(writer, sheet_name="Vibration", index=False)
        power_df.to_excel(writer, sheet_name="Power", index=False)
        gps_df.to_excel(writer, sheet_name="GPS", index=False)
        mode_df.to_excel(writer, sheet_name="FlightModes", index=False)

    print("Excel report generated")

    return vibration_df, power_df, gps_df, mode_df, excel_file