import streamlit as st
import analyzer
import os
import plotly.express as px
import time

st.title("Flight Log Analyzer")

uploaded_file = st.file_uploader("Upload ArduPilot .bin Log", type=["bin"])

if uploaded_file is not None:
    # Create unique filename with timestamp to avoid conflicts
    timestamp = str(int(time.time()))
    unique_name = f"{timestamp}_{uploaded_file.name}"
    
    os.makedirs("logs", exist_ok=True)
    log_path = os.path.join("logs", unique_name)
    
    with open(log_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("Log uploaded successfully")
    
    if st.button("Run Analysis"):
        vibration_df, power_df, gps_df, mode_df, excel_file = analyzer.analyze_log(log_path)
        
        st.success("Analysis completed")
        
        st.subheader("Telemetry Graphs")
        
        # Vibration Graph
        if not vibration_df.empty:
            fig_vibe = px.line(
                vibration_df,
                x="time",
                y=["x", "y", "z"],
                title="Vibration Graph"
            )
            st.plotly_chart(fig_vibe, use_container_width=True)
        
        # Power Graph
        if not power_df.empty:
            fig_power = px.line(
                power_df,
                x="time",
                y=["voltage", "current"],
                title="Voltage and Current"
            )
            st.plotly_chart(fig_power, use_container_width=True)
        
        # GPS Graph (optional)
        if not gps_df.empty:
            fig_gps = px.scatter_mapbox(
                gps_df,
                lat="lat",
                lon="lon",
                title="GPS Path"
            )
            fig_gps.update_layout(mapbox_style="open-street-map")
            st.plotly_chart(fig_gps, use_container_width=True)
        
        # Flight Modes (optional table)
        if not mode_df.empty:
            st.subheader("Flight Modes")
            st.dataframe(mode_df)
        
        # Download button for Excel
        if excel_file.exists():
            with open(excel_file, "rb") as f:
                st.download_button(
                    label="Download Excel Report",
                    data=f,
                    file_name="flight_data.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )