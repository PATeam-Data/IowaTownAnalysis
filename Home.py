import streamlit as st
#import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
  
st.title("Iowa Town Analysis")
st.write("Welcome to Bluebonnet's Iowa Town Analysis! Below you will find useful documentation of our product.")

st.subheader("District Analysis:")

st.subheader("Population and Turnout:")
st.write("This calculator helps visualize potential democratic impact of a population center (city or town) on a district election. It answers the question: Will focusing on a specific town be enough to win the district in the upcoming elections? This calculator uses the projected population and projected Democratic voter turnout from the District Analysis tab to estimate the contribution of a town to the district's overall Democratic vote.")
st. write("How to Use the Calculator:")
multi = """
1. Year Selection: Select the year of the election from 2025 to 2030 that you will be focusing on. 

2. District Selection: Choose the specific Iowa State Senate or Iowa State House district from the dropdown list.

3. Population Center Name: Enter the name of the population center/community that you would like to focus on.

4. District Information:
Projected Population of District: Enter the estimated total population of the district for the selected year. This can be taken from the District Analysis tab.
Projected Democratic Election Turnout in District: Provide the expected percentage of Democratic voter turnout in the district. This can be taken from the District Analysis tab.

5. Community Information:
Projected Population of City: Enter the projected population of the community/population center for the selected year.
Projected Democratic Election Turnout in City: Provide the expected percentage of Democratic voter turnout in the city.

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
Democratic Community Turnout = (Population of City * Projected Democratic Election Turnout of Community) / 100
Democratic Vote Share of Community = (Democratic Community Turnout / Democratic District Turnout) * 100
Democratic Votes Needed from Other Parts of the District to Win = (Democratic District Turnout - Democratic Community Turnout)

"""
st.markdown(multi)

st.subheader("Winnability Index:")