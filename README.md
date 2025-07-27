# 🗺️ DMS to Decimal Degrees Converter (Streamlit App)

A web-based utility to convert latitude and longitude from **DMS (Degrees, Minutes, Seconds)** format to **Decimal Degrees (DD)**.

## 🚀 Features
- Accepts `.csv` or `.xlsx` files
- Detects `Latitude`/`Longitude` columns (supports variations like `lat`, `Lat`, `long`, etc.)
- Handles:
  - Degrees + minutes
  - Decimal minutes or seconds
  - Space-separated or symbol-based DMS
- Outputs `.csv` with `Lat_DD` and `Lon_DD`

## 📂 Input Format
Your file must include two columns:
- `Latitude` or `Lat`
- `Longitude` or `Long`

Example values:
- `21°43'58"N`
- `21 43 58 N`
- `22°28.5'N`
- `70 22.066 E`

## 📥 Sample Files
See the `sample_data/` folder for example files.

## 💻 Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
