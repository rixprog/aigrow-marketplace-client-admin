import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# Page Configuration
st.set_page_config(
    page_title="Smart Farming Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for Interactive Design with Gradient Cards
st.markdown("""
    <style>
    body {
        background-color: #ffffff !important;  /* White background */
        color: #333333;
        font-family: 'Arial', sans-serif;
        padding: 20px;
    }
    .sidebar .sidebar-content {
        background-color: #FF6347; /* Tomato Red for Sidebar */
    }
    h1, h2, h3 {
        color: #FF6347; /* Tomato Red for headings */
        font-family: 'Arial', sans-serif;
    }
    .card {
        background: linear-gradient(145deg, #FF6347, #FF4500); /* Gradient card design */
        color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        text-align: center;
        font-size: 18px;
        margin: 10px 0;
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: scale(1.05);
    }
    .card h3 {
        font-size: 22px;
    }
    .card p {
        font-size: 20px;
    }
    .metric {
        background-color: #F0F0F0;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-size: 18px;
        margin-top: 10px;
        color: #333333;
        box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
    }
    .header {
        text-align: center;
        color: #FF6347;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🌾 Smart Farming Dashboard")
st.markdown("Welcome to the Smart Farming Dashboard that leverages IoT and AI to help farmers make data-driven decisions for efficient agriculture.")

# Function to simulate IoT data updates
def get_iot_data():
    temperature = random.uniform(20, 30)
    humidity = random.uniform(50, 70)
    soil_moisture = random.uniform(30, 100)
    return temperature, humidity, soil_moisture

# Simulate Real-Time IoT Data (for demo purposes)
st.subheader("📊 Real-Time IoT Data")

# Get simulated IoT data
temperature, humidity, soil_moisture = get_iot_data()

# Display Data in Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="card">
        <h3>Temperature</h3>
        <p>{temperature:.2f} °C</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="card">
        <h3>Humidity</h3>
        <p>{humidity:.2f} %</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="card">
        <h3>Soil Moisture</h3>
        <p>{soil_moisture:.2f} %</p>
    </div>
    """, unsafe_allow_html=True)

# Model Predictions Section (Simulated for now)
st.subheader("🤖 AI Model Predictions")
moisture_input = st.slider("Enter Soil Moisture (%)", 30.0, 100.0, 50.0)
predicted_yield = 3 * moisture_input + random.uniform(-5, 5)

# Display Prediction in a Card
st.markdown(f"""
<div class="card">
    <h3>Predicted Crop Yield</h3>
    <p>{predicted_yield:.2f} tons/acre</p>
</div>
""", unsafe_allow_html=True)

# Graph for Yield Trend (Simulated for now)
st.subheader("📈 Crop Yield Trend (Simulated)")
trend_data = pd.DataFrame({
    "Day": np.arange(1, 11),
    "Yield": 3 * np.arange(1, 11) + random.uniform(-5, 5)
})
st.line_chart(trend_data.set_index("Day"))

# Insights Section (Static for demo)
st.subheader("📈 Insights and Recommendations")
st.markdown("""
- **Optimal Temperature Range**: 25-30°C
- **Ideal Humidity Level**: 60-70%
- **Action Recommendations**:
  - Adjust irrigation for consistent soil moisture.
  - Consider planting crops suitable for the current conditions.
""")

# Actionable Insights Image (Optional, for demonstration)
st.image("https://via.placeholder.com/400x200", caption="Actionable Insights")

# JavaScript to Refresh the Page Every 5 Seconds
st.markdown("""
    <script>
    setTimeout(function(){
       window.location.reload(1);
    }, 5000);  // Refresh every 5 seconds
    </script>
""", unsafe_allow_html=True)
