import streamlit as st
import joblib

st.header('Welcome to My House Price Prediction Model')

# Allow users to upload the model file
model_file = st.file_uploader("Price_Prediction_Model.sav", type=["sav"])


with st.form('Myform'):
        col1, col2, col3 = st.columns([1,1,1])
        area = col1.number_input('Area size(in square feet)', 0, 17000, step=100)
        bedrooms = col1.selectbox('Select no. of Bedrooms', [1,2,3,4,5,6])
        bathrooms = col1.selectbox('Select no. of Bathrooms', [1,2,3,4])
        stories = col1.selectbox('Select no. of Stories', [1,2,3,4])

        def map_main_road(main_road_input):return 1 if main_road_input.lower() == 'yes' else 0
        main_road_input = col2.selectbox('Do you want a property located on the Main road?', ['Yes', 'No'])
        main_road_numeric = map_main_road(main_road_input)

        def map_guestroom(guestroom_input):return 1 if guestroom_input.lower() == 'yes' else 0
        guestroom_input = col2.selectbox('Do you want a property with a Guestroom?', ['Yes', 'No'])
        guestroom_numeric = map_guestroom(guestroom_input)

        def map_basement(basement_input):return 1 if basement_input.lower() == 'yes' else 0
        basement_input = col2.selectbox('Do you want a property with a Basement?', ['Yes', 'No'])
        basement_numeric = map_basement(basement_input)

        def map_hotwater_heating(hotwater_heating_input):return 1 if hotwater_heating_input.lower() == 'yes' else 0
        hotwater_heating_input = col2.selectbox('Do you want a property with a hot water heating?', ['Yes', 'No'])
        hotwater_heating_numeric = map_hotwater_heating(hotwater_heating_input)

        def map_air_conditioning(air_conditioning_input):return 1 if air_conditioning_input.lower() == 'yes' else 0
        air_conditioning_input = col3.selectbox('Do you want a property with an Air conditioning?', ['Yes', 'No'])
        air_conditioning_numeric = map_air_conditioning(air_conditioning_input)

        parking = col3.selectbox('Select no. of Parking lot', [0,1,2,3])

        def map_pref_area(pref_area_input):return 1 if pref_area_input.lower() == 'yes' else 0
        pref_area_input = col3.selectbox('Do you want a property within a preferred area?', ['Yes', 'No'])
        pref_area_numeric = map_pref_area(pref_area_input)

        def map_furnishing_status(furnishing_status_input):
            if furnishing_status_input.lower() == 'furnished':
                return 2
            elif furnishing_status_input.lower() == 'semi-furnished':
                return 1
            else:
                return 0
        furnishing_status_input = col3.selectbox('Select furnishing status:', ['Furnished', 'Semi-Furnished', 'Unfurnished'])
        furnishing_status_numeric = map_furnishing_status(furnishing_status_input)

        submit = st.form_submit_button('Process')

    # Process the inputs and provide feedback
if submit:
        input_data = [[area, bedrooms, bathrooms, stories, main_road_numeric, guestroom_numeric,
                    basement_numeric, hotwater_heating_numeric, air_conditioning_numeric,
                    parking, pref_area_numeric, furnishing_status_numeric]]

        predicted_price = model.predict(input_data)
        st.write(f'Predicted Price: {predicted_price}')
