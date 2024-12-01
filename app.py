import streamlit as st
import pandas as pd
import joblib  # To load the pre-trained model

# Load the pre-trained model
model = joblib.load('model.pkl')  # Assuming model.pkl is in the same directory as the Streamlit app

# Streamlit UI
def app():
    st.title("Car Price Prediction")

    # Input fields for the user to provide car details
    car_brand_score = st.number_input("Car Brand Score", min_value=1, max_value=10, value=7)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, value=30000)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Alternative Eco"])
    age = st.number_input("Car Age (in years)", min_value=0, value=3)

    # Convert fuel type into one-hot encoding
    fuel_Petrol = 1 if fuel_type == "Petrol" else 0
    fuel_Diesel = 1 if fuel_type == "Diesel" else 0
    fuel_alternative_eco = 1 if fuel_type == "Alternative Eco" else 0

    # Prepare input data for prediction
    input_data = pd.DataFrame({
        'car_brand_score': [car_brand_score],
        'kms_driven': [kms_driven],
        'fuel_Petrol': [fuel_Petrol],
        'fuel_Diesel': [fuel_Diesel],
        'fuel_alternative_eco': [fuel_alternative_eco],
        'age': [age]
    })

    # Display the input data for the user (optional)
    st.subheader("Input Data")
    st.write(input_data)

    # "Predict" button to trigger prediction
    if st.button('Predict'):
        # Make the price prediction using the loaded model
        predicted_price = model.predict(input_data)

        # Display the predicted price
        st.subheader("Predicted Car Price")
        st.write(f"The estimated price for the car is: ₹ {predicted_price[0]:.2f} Lakh")

if __name__ == "__main__":
    app()
