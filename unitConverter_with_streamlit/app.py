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

value = st.number_input("Enter Value", min_value=0.0, format="%.4f")
from_unit = st.selectbox("From Unit", ["km", "m", "cm", "mm", "mile", "yard"])
to_unit = st.selectbox("To Unit", ["km", "m", "cm", "mm", "mile", "yard"])
convert = st.button("🔄 Convert")

if convert:
    st.success(f"Converted Value: **{value} {from_unit} = ??? {to_unit}**")
