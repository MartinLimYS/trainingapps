import streamlit as st
import joblib
model = joblib.load('house_price_model.pkl')
st.title('House Price Estimator')
med_inc = st.number_input('Median Income (in $10,000s)', 0.0, 20.0, 3.5)
house_age = st.number_input('House Age', 0, 60, 20)
rooms = st.number_input('Average Rooms', 1.0, 15.0, 5.0)
bedrooms = st.number_input('Average Bedrooms', 0.5, 5.0, 1.0)
population = st.number_input('Population', 1, 40000, 1000)
occup = st.number_input('Average Occupancy', 0.5, 10.0, 3.0)
lat = st.number_input('Latitude', 32.0, 42.0, 34.0)
lon = st.number_input('Longitude', -125.0, -114.0, -118.0)
if st.button('Estimate Price'):
    row = [med_inc, house_age, rooms, bedrooms, population, occup, lat, lon]
    price = model.predict([row])[0]
st.success(f'Estimated Median House Value: ${price*100000:,.0f}')
