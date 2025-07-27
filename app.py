import streamlit as st
import pandas as pd
import re
from io import BytesIO

st.set_page_config(page_title="DMS to Decimal Degree Converter", layout="centered")
st.title("📍 DMS to Decimal Degrees Converter (Lat/Lon)")

st.markdown("""
This tool converts coordinates in **DMS (Degrees Minutes Seconds)** format into **Decimal Degrees**.

✅ Columns accepted for Latitude: `Latitude`, `latitude`, `Lat`, `lat`  
✅ Columns accepted for Longitude: `Longitude`, `longitude`, `Long`, `long`

---
""")

st.warning("""
**Disclaimer:**
Only the latitude and longitude columns will be modified. All other data in the file will remain unchanged. 
Please verify that:
- Your coordinates are in DMS format (e.g., 21°43'58"N or 21 43 58 N)
- Direction (N/S/E/W) is present
- Column names are as specified above
""")

# Enhanced robust DMS to DD conversion function
def dms_to_dd(dms):
    try:
        dms_clean = re.sub(r'[^\d\.NSEWnsew]+', ' ', dms).strip()
        parts = dms_clean.split()

        # Check for valid direction
        direction = next((p.upper() for p in parts if p.upper() in ["N", "S", "E", "W"]), None)
        if not direction:
            return None

        # Extract numbers only
        nums = [float(p) for p in parts if re.match(r'^-?\d+(\.\d+)?$', p)]

        deg = nums[0] if len(nums) > 0 else 0
        min_ = nums[1] if len(nums) > 1 else 0
        sec = nums[2] if len(nums) > 2 else 0

        dd = deg + min_ / 60 + sec / 3600
        if direction in ["S", "W"]:
            dd *= -1

        return round(dd, 6)
    except:
        return None

uploaded_file = st.file_uploader("Upload a file (.xlsx or .csv)", type=["xlsx", "csv"])

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1]
    if file_type == "csv":
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    lat_col = next((col for col in df.columns if col.lower() in ["latitude", "lat"]), None)
    lon_col = next((col for col in df.columns if col.lower() in ["longitude", "long"]), None)

    if not lat_col or not lon_col:
        st.error("Latitude and Longitude columns not found. Please use proper column headers.")
    else:
        df['Lat_DD'] = df[lat_col].astype(str).apply(dms_to_dd)
        df['Lon_DD'] = df[lon_col].astype(str).apply(dms_to_dd)

        st.subheader("🔍 Preview of Converted Data")
        st.dataframe(df.head())

        output = BytesIO()
        df.to_csv(output, index=False)
        st.download_button("📥 Download Converted CSV", output.getvalue(), file_name="converted_coordinates.csv", mime="text/csv")
