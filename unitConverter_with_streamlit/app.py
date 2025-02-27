import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")

# Apply Glassmorphism CSS
st.markdown(
    """
    <style>
    .stApp { background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(10px); }
    .stTextInput, .stSelectbox, .stNumberInput, .stButton {
        background: rgba(255, 255, 255, 0.3);
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔄 Glassmorphism Unit Converter")

st.subheader("Convert different units with a modern UI!")

# Conversion factors (All relative to meters)
conversion_factors = {
    "km": 1000,
    "m": 1,
    "cm": 0.01,
    "mm": 0.001,
    "mile": 1609.34,
    "yard": 0.9144,
    "foot": 0.3048,
    "inch": 0.0254,
    "nautical mile": 1852,
}

value = st.number_input("Enter Value", min_value=0.0, format="%.4f")
from_unit = st.selectbox("From Unit", list(conversion_factors.keys()))
to_unit = st.selectbox("To Unit", list(conversion_factors.keys()))
convert = st.button("🔄 Convert")

if convert:
    if from_unit == to_unit:
        converted_value = value  # Same unit conversion
    else:
        # Convert to meters first, then to target unit
        converted_value = value * (conversion_factors[from_unit] / conversion_factors[to_unit])

    st.success(f"Converted Value: **{value} {from_unit} = {converted_value:.4f} {to_unit}**")
