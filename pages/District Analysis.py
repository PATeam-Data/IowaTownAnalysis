import streamlit as st 
import streamlit.components.v1 as components

# Projections - this is the Machine Learning Model  
st.title("District Analysis")
# add years along to the selection

st.subheader(f"Projected 2030 Analysis")
district = st.selectbox("Iowa General Assembly", ["Senate - Upper", "House - Lower", "Precinct"])

# Display different content based on the selected district
if district == "House - Lower":
    st.write("Here is the analysis for House - Lower:")
    lower_tableau_url = "https://public.tableau.com/views/Project_2030_LH_17273272369200/Dashboard1"
    # HTML code to embed Tableau with dynamic sizing
    lower_tableau_html = f"""
        <div class='tableauPlaceholder' id='viz1727469360505' style='position: relative'>
            <noscript>
                <a href='#'>
                    <img alt='Dashboard 1' 
                    src='https://public.tableau.com/static/images/Pr/Project_2030_LH_17273272369200/Dashboard1/1_rss.png' 
                    style='border: none' />
                </a>
            </noscript>
            <object class='tableauViz' style='display:none;'>
                <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                <param name='embed_code_version' value='3' />
                <param name='site_root' value='' />
                <param name='name' value='Project_2030_LH_17273272369200/Dashboard1' />
                <param name='tabs' value='no' />
                <param name='toolbar' value='yes' />
                <param name='static_image' value='https://public.tableau.com/static/images/Pr/Project_2030_LH_17273272369200/Dashboard1/1.png' />
                <param name='animate_transition' value='yes' />
                <param name='display_static_image' value='yes' />
                <param name='display_spinner' value='yes' />
                <param name='display_overlay' value='yes' />
                <param name='display_count' value='yes' />
                <param name='language' value='en-US' />
            </object>
        </div>
        <script type='text/javascript'>
            var divElement = document.getElementById('viz1727469360505');
            var vizElement = divElement.getElementsByTagName('object')[0];
            vizElement.style.width = '100%';
            vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
            var scriptElement = document.createElement('script');
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
            vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
    """
    # Embed the Tableau visualization using HTML
    st.components.v1.html(lower_tableau_html, height=800)

if district == "Senate - Upper":
    st.write("Here is the analysis for Senate - Upper:")   
    upper_tableau_url = "https://public.tableau.com/app/profile/bluebonnet.data/viz/Project_2030_UH_17273273216760/Dashboard1"
    # HTML code to embed Tableau with dynamic sizing
    upper_tableau_html = f"""
        <div class='tableauPlaceholder' id='viz1727469943966' style='position: relative'>
            <noscript>
                <a href='#'>
                    <img alt='Dashboard 1' 
                    src='https://public.tableau.com/static/images/Pr/Project_2030_UH_17273273216760/Dashboard1/1_rss.png' 
                    style='border: none' />
                </a>
            </noscript>
            <object class='tableauViz' style='display:none;'>
                <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                <param name='embed_code_version' value='3' />
                <param name='site_root' value='' />
                <param name='name' value='Project_2030_UH_17273273216760/Dashboard1' />
                <param name='tabs' value='no' />
                <param name='toolbar' value='yes' />
                <param name='static_image' value='https://public.tableau.com/static/images/Pr/Project_2030_UH_17273273216760/Dashboard1/1.png' />
                <param name='animate_transition' value='yes' />
                <param name='display_static_image' value='yes' />
                <param name='display_spinner' value='yes' />
                <param name='display_overlay' value='yes' />
                <param name='display_count' value='yes' />
                <param name='language' value='en-US' />
            </object>
        </div>
        <script type='text/javascript'>
            var divElement = document.getElementById('viz1727469943966');
            var vizElement = divElement.getElementsByTagName('object')[0];
            vizElement.style.width = '100%';
            vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
            var scriptElement = document.createElement('script');
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
            vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
    """  
    # Embed the Tableau visualization using HTML
    st.components.v1.html(upper_tableau_html, height=800)

elif district == "Precinct":
    st.write("Here is the granualar analysis for Precinct-Wide Data ")
    import pandas as pd
    import numpy as np
    import geopandas as gpd
    import requests
    import tempfile
    import folium
    import branca
    # Read Iowa precinct data
    iowa_precinct_data = pd.read_csv("https://raw.githubusercontent.com/mmargob/Iowa-Precinct/main/district-data.csv", skiprows=2, header=None)

    def predict_30(cvap_2019, cvap_2020, cvap_2022):
        # Combine input vectors into a 2D array for each row (precinct)
        cvap_data = np.array([cvap_2019, cvap_2020, cvap_2022]).T

        # Placeholder for predictions
        predictions = []

        # Calculate the number of years for prediction
        years_to_predict = 2030 - 2022

        # Iterate through each row (precinct) in the input data
        for data_row in cvap_data:
            # Calculate the annual growth rates between years
            growth_rate_2019_2020 = (data_row[1] - data_row[0]) / data_row[0] if data_row[0] != 0 else 0
            growth_rate_2020_2022 = (data_row[2] - data_row[1]) / data_row[1] if data_row[1] != 0 else 0

            # Average growth rate over the period, scaled down further
            average_growth_rate = ((growth_rate_2019_2020 + growth_rate_2020_2022) / 2) / 4  # Adjusting the factor

            # Predict 2030 population using the adjusted average growth rate
            prediction = data_row[2] * ((1 + average_growth_rate) ** years_to_predict)

            # Apply constraints: no negative numbers, cap high values
            prediction = max(0, prediction)  # No negative predictions
            prediction = min(prediction, max(data_row) * 1.5)  # Cap at 1.5x the max historical value

            # Round to the nearest whole number
            predictions.append(round(prediction))

        return np.array(predictions)
    # Calculate the 2030 predicted CVAP
    iowa_precinct_data['cvap_30_pred'] = predict_30(iowa_precinct_data[44], iowa_precinct_data[67], iowa_precinct_data[74])
    # Calculating total 2030 population
    iowa_precinct_data['pop_30_pred'] = predict_30(iowa_precinct_data[9], iowa_precinct_data[23], iowa_precinct_data[30])

    # Load GeoJSON file for Iowa precincts
    geojson_url = "https://raw.githubusercontent.com/mmargob/Iowa-Precinct/main/IowaPrecinct.geojson"
    ia_precinct_geojson = tempfile.NamedTemporaryFile(suffix=".geojson", delete=False)
    response = requests.get(geojson_url)
    ia_precinct_geojson.write(response.content)
    ia_precinct_geojson.flush()

    # Read GeoJSON into GeoDataFrame
    precinct_sf = gpd.read_file(ia_precinct_geojson.name)

    # Merge data with geospatial data
    iowa_precinct_data["NAME"] = precinct_sf["NAME"]
    precinct_sf_merged_cvap2030 = precinct_sf.merge(iowa_precinct_data, left_on="NAME", right_on="NAME")

    # # Correcting the census block named Washington
    washington_precinct = iowa_precinct_data[iowa_precinct_data["NAME"] == "Washington"].copy()

    # Specify the columns you want to divide by 11 (e.g., 'cvap_30_pred', 'pop_30_pred')
    columns_to_modify = ['cvap_30_pred', 'pop_30_pred']

    # Divide the selected columns by 11
    washington_precinct[columns_to_modify] = (washington_precinct[columns_to_modify] / 11).round()

    # Update the original dataframe with the modified values for Washington
    iowa_precinct_data.update(washington_precinct)

    # Re-merge iowa_precinct_data with precinct_sf to update the map data
    precinct_sf_merged_cvap2030 = precinct_sf.merge(iowa_precinct_data, left_on="NAME", right_on="NAME")

    # Ensure there are no missing values in the merged data
    precinct_sf_merged_cvap2030['cvap_30_pred'].fillna(0, inplace=True)  # Replace NaN values with 0 or another suitable value

    # Initialize a folium map centered on Iowa
    m = folium.Map(location=[41.878, -93.097], zoom_start=7)

    # Create a linear colormap
    min_val = precinct_sf_merged_cvap2030['cvap_30_pred'].min()
    max_val = precinct_sf_merged_cvap2030['cvap_30_pred'].max()
    colormap = branca.colormap.LinearColormap(
        colors=['blue', 'green', 'yellow', 'orange', 'red'],
        vmin=min_val, vmax=max_val,
        caption='2030 Predicted CVAP'
    )

    # Define a color function for the GeoJSON data
    def color_function(feature):
        value = feature['properties'].get('cvap_30_pred', 0)  # Default to 0 if value is missing
        return colormap(value)

    # Add precinct polygons to the map
    folium.GeoJson(
        precinct_sf_merged_cvap2030,
        style_function=lambda feature: {
            'fillColor': color_function(feature),
            'color': 'black',
            'weight': 0.5,
            'fillOpacity': 0.7
        },
        tooltip=folium.GeoJsonTooltip(
            fields=['NAME', 'cvap_30_pred'],
            aliases=['Precinct Name:', 'Predicted CVAP 2030:'],
            localize=True
        )
    ).add_to(m)

    # Add the colormap to the map
    colormap.add_to(m)
    map_html = m._repr_html_()
    # Display the map
    st.components.v1.html(map_html, height=600)


# Historical Election Results (Francisco's Work)
st.subheader("Historical Election Results")
year = st.selectbox("Year", ["2012", "2016", "2018","2020", "2022"])

tableau_links = {
    "2020": "https://public.tableau.com/views/Iowa_Book_20/Story1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",
    "2022": "https://public.tableau.com/views/Iowa_Book_22/Story1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
}

if year in tableau_links:
    st.markdown(f"[View Tableau Dashboard for {year}]({tableau_links[year]})")



