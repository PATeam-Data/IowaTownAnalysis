import streamlit as st
#import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
  
st.title("Iowa Town Analysis")
st.write("Welcome to Bluebonnet's Iowa Town Analysis! Below you will find useful documentation of our product.")

st.subheader("District Analysis:")
multi = """
Using Python for Machine Learning, my objective was to predict the Total 
and Democratic vote counts, as well as Population estimates for the 2030 
House (Lower) and Senate (Upper) districts. The accuracy and reliability of 
these predictions are expected to improve as new election data becomes 
available and is integrated into the current dataset being fed into the 
machine learning algorithm.
I created two Tableau maps using .csv files created from merging the ML 
model data and Census shapefile data. On these interactive maps, you will 
be able to filter and/or hover over the districts to see the estimates 
mentioned previously.
"""

st.subheader("District Analysis - Precinct Analysis:")
multi = """
The shape file, obtained from: https://catalog.data.gov/dataset/2020-cartographic-boundary-file-kml-2020-census-voting-district-vtd-for-iowa-1-500000/resource/cdc1e62d-348e-42dc-94cf-94c1240e80ac was used on a website for election and census data related mapping, https://davesredistricting.org/maps#home to create a csv file of CVAP data from 2019 - 2022. Using these trends, I created a formula to predict the 2030 population, and controlling for extreme results (such as massive growth or decline). There was an issue with the Washington precinct, so precincts with that title were divided to display more accurate information.
"""
st.markdown(multi)

####

st.subheader("Population and Turnout:")
st.write("This calculator helps visualize potential democratic impact of a population center on a district election. It answers the question: Will focusing on a specific town be enough to win the district in the upcoming elections? This calculator uses the projected population and projected Democratic voter turnout from the Projections Database to estimate the contribution of a community's to the district's overall Democratic vote.")
st. write("How to Use the Calculator:")
multi = """
1. Year Selection: Select the year of the election from 2025 to 2030 that you will be focusing on. 

2. District Selection: Choose the specific Iowa State Senate or Iowa State House district from the dropdown list.

3. Population Center Name: Enter the name of the population center/community that you would like to focus on.

4. District Information:
Projected Population of District: Enter the estimated total population of the district for the selected year. This can be taken from the projections database.
Projected Democratic Election Turnout in District: Provide the expected percentage of Democratic voter turnout in the district. This can be taken from the projections database.

5. Community Information:
Projected Population of City: Enter the projected population of the community/population center for the selected year.
Projected Democratic Election Turnout in City: Provide the expected percentage of Democratic voter turnout in the community.

6. District Strategic Win Target:
Choose the win target for the district:
50% + 1 person: This means winning just a little over half of the projected Democratic vote in the district.
53%: This means winning at 53% of the total projected Democratic vote for a comfortable win.

7. Calculate Impact:
Press the "Calculate Impact" button to generate results based on the data entered.

Understanding the Results:

1. Projected Democratic District Turnout: The estimated number of Democratic voters expected to turn out in the district based on population and turnout percentage.
2. Projected Democratic Community Turnout: The estimated number of Democratic voters expected to turn out in the selected community/population center.
3. Your Community's Democratic Vote Share of District: The percentage of the district's total Democratic votes that will come from the city.
4. Democratic Votes Needed from Other Parts of the District to Win: If the city’s vote is not enough to reach the win threshold, this value shows how many more votes are required from other areas of the district to win the election.

A Further Explanation of the Calculations:

Democratic District Turnout = (Population of District * Projected Democratic Election Turnout of District) / 100
Democratic Community Turnout = (Population of Community * Projected Democratic Election Turnout of Community) / 100
Democratic Vote Share of Community = (Democratic Community Turnout / Democratic District Turnout) * 100
Democratic Votes Needed from Other Parts of the District to Win = (Democratic District Turnout - Democratic Community Turnout)

"""
st.markdown(multi)

####

st.subheader("Winnability Index:")

####

st.subheader("Winnability Index - CAFOs and Opposition Scoring:")

multi = """
The first map displays a composite score of data about the Oppositional factors present in Iowa. For pipelines, there is lower scoring (1) where there are planned pipelines and ethanol production capacity in a county and a higher scoring (4) when there has already been Anti-Pipeline Local Ordinances Enacted and Litigation Initiated. For CAFOs, the quartile of how many exist in a county factor into the composite score.
The second map more granularly places the CAFO facilities on top of their counties. This could be useful for identifying key towns as they relate to the districts in the calculator.
"""
st.markdown(multi)