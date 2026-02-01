import streamlit as st
from app.camera.capture import capture_image
from app.camera.detect_waste import detect_from_frame
from app.geo.get_location import get_location
from app.maps.show_map import show_map
from PIL import Image
import os

st.set_page_config(page_title="Smart Waste Management", layout="wide")
st.title("📸 Smart Waste Management System")

# Step 1: Capture Image
if st.button("📷 Capture Waste Image"):
    image_path = "data/captured_images/image1.jpg"
    if capture_image(image_path):
        st.image(image_path, caption="Captured Image", use_column_width=True)

        # Step 2: Detect Waste
        result = detect_from_frame(image_path)
        st.subheader("🧠 Detection Result:")
        st.success(result)

        # Step 3: Get Geo-location
        latlng = get_location()
        if latlng:
            lat, lng = latlng
            st.info(f"📍 Location: Latitude: {lat}, Longitude: {lng}")

            # Step 4: Show Map
            map_path = "data/map.html"
            show_map(lat, lng, map_path)
            st.components.v1.html(open(map_path, 'r').read(), height=500)
        else:
            st.warning("Could not get your location.")
    else:
        st.error("Failed to capture image from webcam.")
