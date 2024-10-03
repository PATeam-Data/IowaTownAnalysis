import streamlit as st
import pandas as pd
import openpyxl

st.subheader("Winnability Index: Social Determinant Scoring")

# Add the explanatory text in a wide text box
explanatory_text = """
This section presents scores for each county to assess the negative impact of social determinant issues. The scores range from 1 to 4, where 1 indicates the most significant negative impact and 4 represents the least negative impact.


The scoring methodology is as follows:

1. For each metric within each category, we calculate the quantile for each county.
2. Each county receives a score for each metric based on its quantile ranking, with scores ranging from 1 to 4.
3. For some metrics, a lower quantile indicates a worse situation. For instance, a higher percentage of uninsured adults is more concerning if a county falls into the first quantile rather than the fourth. As a result, counties in the first quantile for this metric receive a score of 4, while those in the fourth quantile receive a score of 1.
4. Conversely, for metrics where a higher quantile is preferable, the scoring is reversed.
5. After assigning scores for all metrics within a category, we average these scores to calculate the composite scores.
6. Additionally, certain metrics are weighted more heavily than others within specific categories.

"""

# Use a wide text box for the explanatory text
st.markdown(f"<div style='background-color: #2E2E2E; color: white; padding: 20px; border-radius: 5px;'>{explanatory_text}</div>", unsafe_allow_html=True)

# Tableau Public URL for the first view
tableau_url = "https://public.tableau.com/views/IowaSocialDeterminantScoring/SummaryMap"

# HTML code to embed the first Tableau visualization with dynamic sizing
tableau_html_1 = f"""
    <div class='tableauPlaceholder' id='viz1727391933235' style='position: relative'>
        <noscript>
            <a href='#'>
                <img alt='Iowa Social Determinant Issue Scoring' 
                src='https://public.tableau.com/static/images/Io/IowaSocialDeterminantScoring/SummaryMap/1_rss.png' 
                style='border: none' />
            </a>
        </noscript>
        <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
            <param name='embed_code_version' value='3' /> 
            <param name='site_root' value='' />
            <param name='name' value='IowaSocialDeterminantScoring/SummaryMap' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https://public.tableau.com/static/images/Io/IowaSocialDeterminantScoring/SummaryMap/1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1727391933235');                    
        var vizElement = divElement.getElementsByTagName('object')[0];                    
        vizElement.style.width='100%'; 
        vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    
        var scriptElement = document.createElement('script');                    
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
"""

# Embed the first Tableau visualization
st.components.v1.html(tableau_html_1, height=575)

# Load the Excel file
file_path = '/Users/elizabethlites/Desktop/Vscode Practice/SD Scoring Final.xlsx'
sheets_dict = pd.read_excel(file_path, sheet_name=None)

st.subheader("Social Determinant Metrics and Lowest Scoring Counties by Category")
# Create a dropdown menu to select a sheet above Category Metrics
sheet_names = list(sheets_dict.keys())
selected_sheet = st.selectbox("Select a category to view the associated metrics and the counties with the lowest scores for that category.:", sheet_names)

# Get the selected DataFrame
df = sheets_dict[selected_sheet]

# Remove the 99th row if the sheet is not 'Allscores' or 'Longdata'
if selected_sheet not in ['Allscores', 'Longdata'] and len(df) > 99:
    df = df.drop(99)  # 99th row has index 98 since index is 0-based

st.write("Category Metrics:")

# Filter out columns that shouldn't appear in metrics
excluded_keywords = ["Quantile", "Score", "quantile", "score", "COUNTY", "Category", "Region"]
filtered_columns = [col for col in df.columns if not any(keyword in col for keyword in excluded_keywords)]

# Display metrics in a vertical numbered list
if filtered_columns:
    metrics_list = "<ol style='padding-left: 20px;'>" + "".join(f"<li>{col}</li>" for col in filtered_columns) + "</ol>"
    st.markdown(metrics_list, unsafe_allow_html=True)
else:
    st.write("No metrics to display.")

# Display the lowest 10 Composite Scores directly below the Category Metrics
if 'Composite_Score' in df.columns:
    lowest_scores = df.nsmallest(10, 'Composite_Score')
    st.write(f"Top 10 Lowest Scoring Counties for '{selected_sheet}':")
    st.dataframe(lowest_scores[['COUNTY', 'Composite_Score']], use_container_width=True)
else:
    st.write("Composite_Score column not found in this DataFrame.")

st.subheader("Full Dataset with raw metrics and calculated fields (quantiles and scores)")
# Filter by county in the left column (below the lowest scores)
county_filter = st.text_input("Enter county name to filter:", key="county_filter")

# Filter the DataFrame based on the county input
if county_filter:
    filtered_df = df[df['COUNTY'].str.contains(county_filter, case=False, na=False)]  # Adjust 'COUNTY' to your actual column name
else:
    filtered_df = df

# Display the filtered DataFrame
st.dataframe(filtered_df.style.set_properties(**{'min-width': '150px'}), use_container_width=True)

st.markdown("<hr style='border: 1px solid #2E2E2E;' />", unsafe_allow_html=True)

st.subheader(" ")
st.subheader("Winnability Index: CAFOs and Opposition Scoring")
# Embed the third Tableau visualization
tableau_html_3 = """
<div class='tableauPlaceholder' id='viz1727746523656' style='position: relative'>
    <noscript>
        <a href='#'>
            <img alt=' ' src='https://public.tableau.com/static/images/Io/IowaOppositionScoring/CAFOsMap/1_rss.png' style='border: none' />
        </a>
    </noscript>
    <object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
        <param name='embed_code_version' value='3' /> 
        <param name='site_root' value='' />
        <param name='name' value='IowaOppositionScoring/CAFOsMap' />
        <param name='tabs' value='yes' />
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https://public.tableau.com/static/images/Io/IowaOppositionScoring/CAFOsMap/1.png' /> 
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
    </object>
</div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1727746523656');                    
    var vizElement = divElement.getElementsByTagName('object')[0];                    
    vizElement.style.width='100%'; 
    vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    
    var scriptElement = document.createElement('script');                    
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""

# Embed the third Tableau visualization
st.components.v1.html(tableau_html_3, height=800)