import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Multi-Converter",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a beautiful page layout
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #e0e0e0;
    }
    .block-container {
        padding-top: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar settings
st.sidebar.title("Multi-Converter")
st.sidebar.markdown("Choose a converter:")

converter_type = st.sidebar.radio(
    "Converter Type",
    ('Temperature', 'Length', 'Weight')
)

st.title("🔄 Multi-Converter")
st.markdown("Convert between different units easily.")

def temperature_converter():
    st.subheader("Temperature Converter")
    temp_input = st.number_input("Enter temperature:", format="%f")
    temp_unit = st.selectbox("Select unit:", ("Celsius", "Fahrenheit", "Kelvin"))

    if temp_unit == "Celsius":
        f = (temp_input * 9/5) + 32
        k = temp_input + 273.15
        st.write(f"{temp_input} °C is {f:.2f} °F")
        st.write(f"{temp_input} °C is {k:.2f} K")
    elif temp_unit == "Fahrenheit":
        c = (temp_input - 32) * 5/9
        k = c + 273.15
        st.write(f"{temp_input} °F is {c:.2f} °C")
        st.write(f"{temp_input} °F is {k:.2f} K")
    elif temp_unit == "Kelvin":
        c = temp_input - 273.15
        f = (c * 9/5) + 32
        st.write(f"{temp_input} K is {c:.2f} °C")
        st.write(f"{temp_input} K is {f:.2f} °F")

def length_converter():
    st.subheader("Length Converter")
    length_input = st.number_input("Enter length:", format="%f")
    length_unit = st.selectbox("Select unit:", ("Meters", "Kilometers", "Miles"))

    if length_unit == "Meters":
        km = length_input / 1000
        miles = length_input / 1609.344
        st.write(f"{length_input} m is {km:.2f} km")
        st.write(f"{length_input} m is {miles:.2f} miles")
    elif length_unit == "Kilometers":
        m = length_input * 1000
        miles = length_input / 1.609344
        st.write(f"{length_input} km is {m:.2f} m")
        st.write(f"{length_input} km is {miles:.2f} miles")
    elif length_unit == "Miles":
        m = length_input * 1609.344
        km = length_input * 1.609344
        st.write(f"{length_input} miles is {m:.2f} m")
        st.write(f"{length_input} miles is {km:.2f} km")

def weight_converter():
    st.subheader("Weight Converter")
    weight_input = st.number_input("Enter weight:", format="%f")
    weight_unit = st.selectbox("Select unit:", ("Kilograms", "Grams", "Pounds"))

    if weight_unit == "Kilograms":
        g = weight_input * 1000
        lbs = weight_input * 2.20462
        st.write(f"{weight_input} kg is {g:.2f} g")
        st.write(f"{weight_input} kg is {lbs:.2f} lbs")
    elif weight_unit == "Grams":
        kg = weight_input / 1000
        lbs = weight_input / 453.592
        st.write(f"{weight_input} g is {kg:.2f} kg")
        st.write(f"{weight_input} g is {lbs:.2f} lbs")
    elif weight_unit == "Pounds":
        kg = weight_input / 2.20462
        g = weight_input * 453.592
        st.write(f"{weight_input} lbs is {kg:.2f} kg")
        st.write(f"{weight_input} lbs is {g:.2f} g")

if converter_type == 'Temperature':
    temperature_converter()
elif converter_type == 'Length':
    length_converter()
elif converter_type == 'Weight':
    weight_converter()
