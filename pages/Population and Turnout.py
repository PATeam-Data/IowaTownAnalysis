import streamlit as st 

st.title("Population Center Impact and Estimated Turnout")

# This calculator is to visualize a win on a more granular scale between a population center and a district. 
# The question we are trying to answer is: after calculating the overall impact of a population center
# on a district, will it be enough to win the district to just focus on this town in 2030? We have calculated the projected
# population and turnout rate of the district, taken from the District Analysis tab. 

st.write("This calculator is to visualize a win on a more granular scale between a population center and a district. The question we are trying to answer is: after calculating the overall impact of a population center/commununity on a district, will it be enough to win the district to just focus on this town in 2030? Communities are defined by the users, and can be any population center. We have calculated the projected population and turnout rate of the district, taken from the District Analysis tab. All entries should be full numbers.")
year = st.selectbox("Year", ["2025", "2026","2027", "2028", "2029", "2030"])
district = st.selectbox("District", ["Iowa State Senate 1", "Iowa State Senate 2", "Iowa State Senate 3", "Iowa State Senate 4", "Iowa State Senate 5", "Iowa State Senate 6", "Iowa State Senate 7",
                                     "Iowa State Senate 8", "Iowa State Senate 9", "Iowa State Senate 10", "Iowa State Senate 11", "Iowa State Senate 12", "Iowa State Senate 13", "Iowa State Senate 14", "Iowa State Senate 15",
                                     "Iowa State Senate 16", "Iowa State Senate 17", "Iowa State Senate 18", "Iowa State Senate 19", "Iowa State Senate 20", "Iowa State Senate 21", "Iowa State Senate 22", "Iowa State Senate 23",
                                     "Iowa State Senate 24", "Iowa State Senate 25", "Iowa State Senate 26", "Iowa State Senate 27", "Iowa State Senate 28", "Iowa State Senate 29", "Iowa State Senate 30", "Iowa State Senate 31",
                                     "Iowa State Senate 31", "Iowa State Senate 32", "Iowa State Senate 23", "Iowa State Senate 24", "Iowa State Senate 25", "Iowa State Senate 26", "Iowa State Senate 27", "Iowa State Senate 28",
                                     "Iowa State Senate 29", "Iowa State Senate 30", "Iowa State Senate 31", "Iowa State Senate 32", "Iowa State Senate 33", "Iowa State Senate 34", "Iowa State Senate 35", "Iowa State Senate 36",
                                     "Iowa State Senate 37", "Iowa State Senate 38", "Iowa State Senate 39", "Iowa State Senate 40", "Iowa State Senate 41", "Iowa State Senate 42", "Iowa State Senate 43", "Iowa State Senate 44",
                                     "Iowa State Senate 45", "Iowa State Senate 46", "Iowa State Senate 47", "Iowa State Senate 48", "Iowa State Senate 49", "Iowa State Senate 50","Iowa State House 1", "Iowa State House 2", 
                                     "Iowa State House 3", "Iowa State House 4", "Iowa State House 5", "Iowa State House 6", "Iowa State House 7", "Iowa State House 8", "Iowa State House 9", "Iowa State House 10", "Iowa State House 11", "Iowa State House 12",
                                     "Iowa State House 13", "Iowa State House 14", "Iowa State House 15", "Iowa State House 16", "Iowa State House 17", "Iowa State House 18", "Iowa State House 19", "Iowa State House 20", "Iowa State House 21",
                                     "Iowa State House 22", "Iowa State House 23", "Iowa State House 24", "Iowa State House 25", "Iowa State House 26", "Iowa State House 27", "Iowa State House 28", "Iowa State House 29", "Iowa State House 30",
                                     "Iowa State House 31", "Iowa State House 32", "Iowa State House 33", "Iowa State House 34", "Iowa State House 35", "Iowa State House 36", "Iowa State House 37", "Iowa State House 38", "Iowa State House 39",
                                     "Iowa State House 40", "Iowa State House 41", "Iowa State House 42", "Iowa State House 43", "Iowa State House 44", "Iowa State House 45", "Iowa State House 46", "Iowa State House 47", "Iowa State House 48",
                                     "Iowa State House 49", "Iowa State House 50", "Iowa State House 51", "Iowa State House 52", "Iowa State House 53", "Iowa State House 54", "Iowa State House 55", "Iowa State House 56", "Iowa State House 57",
                                     "Iowa State House 58", "Iowa State House 59", "Iowa State House 60", "Iowa State House 61", "Iowa State House 62", "Iowa State House 63", "Iowa State House 64", "Iowa State House 65", "Iowa State House 66",
                                     "Iowa State House 67", "Iowa State House 68", "Iowa State House 69", "Iowa State House 70", "Iowa State House 71", "Iowa State House 72", "Iowa State House 73", "Iowa State House 74", "Iowa State House 75",
                                     "Iowa State House 76", "Iowa State House 77", "Iowa State House 78", "Iowa State House 79", "Iowa State House 80", "Iowa State House 81", "Iowa State House 82", "Iowa State House 83", "Iowa State House 84",
                                     "Iowa State House 85", "Iowa State House 86", "Iowa State House 87", "Iowa State House 88", "Iowa State House 89", "Iowa State House 90", "Iowa State House 91", "Iowa State House 92", "Iowa State House 93",
                                     "Iowa State House 94", "Iowa State House 95", "Iowa State House 96", "Iowa State House 97", "Iowa State House 98", "Iowa State House 99", "Iowa State House 100"])
city = st.text_input("Community/Population Center Name:")

st.write("Numbers will be provided by the Projections Database.")

# values
st.subheader("District Information:")
population_of_district = st.number_input(f"Projected Population of District in {year}:")
dem_election_turnout_of_district = st.number_input(f"Projected Democratic Election Turnout in percentage of {district} in {year}:")
#total_election_turnout_of_district = st.number_input(f"Projected Total Election Turnout in percentage of {district} in {year}:")


st.subheader("Community Information:")
population_of_city = st.number_input(f"Projected Population of {city} in {year}:")
dem_election_turnout_of_city = st.number_input(f"Projected Democratic Election Turnout {city} in {year}:")
#total_election_turnout_of_city = st.number_input(f"Projected Total Election Turnout {city} in {year}:")


st.subheader("District Strategic Win Target")
district_strategic_win = st.selectbox(f"Select a District Strategic Win Number:", ["50%(Projected Democratic Vote Total) + 1 person", "53%(Projected Democratic Vote Total)"])

dem_district_turnout = 0
dem_city_turnout = 0
dem_voting_share_of_city = 0
voters_needed_from_elsewhere = 0

# calculator 
if st.button("Calculate Impact:"):
   #total_district_turnout = population_of_district * (total_election_turnout_of_city / 100) 
    dem_district_turnout = population_of_district * (dem_election_turnout_of_district / 100)

    #total_city_turnout = population_of_city * (total_election_turnout_of_city / 100)
    dem_city_turnout = population_of_city * (dem_election_turnout_of_city / 100)

    dem_voting_share_of_city = (dem_city_turnout/dem_district_turnout) * 100 if dem_district_turnout > 0 else 0
   
    if district_strategic_win == "50%(Projected Vote Total) + 1 person":
        win_threshold = (dem_district_turnout / 2) + 1
    else:
        win_threshold = dem_district_turnout * 0.53
    voters_needed_from_elsewhere = max(0, win_threshold - dem_city_turnout)

st.subheader("Results:")
st.write(f"**Projected Democratic District Turnout in {year}:** {dem_district_turnout:.0f} voters")
st.write(f"**Projected Democratic Community Turnout in {year}:** {dem_city_turnout:.0f} voters")
st.write(f"**Your Community's Share of District Democratic Win Target:** {dem_voting_share_of_city:.2f}%")
st.write(f"**Democratic Votes Needed from Other Parts of the District to Win:** {voters_needed_from_elsewhere:.0f} votes")