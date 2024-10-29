import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import streamlit as st

# Streamlit Layout
st.title("Twitter Analytics Report")

# Side panel information
col1, col2 = st.columns([1, 3])

# Left side with additional details
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/en/6/60/Twitter_Logo_as_of_2021.svg", width=50)  # Twitter logo
    st.markdown("### Date period:\n Last 30 days", unsafe_allow_html=True)
    st.markdown("### Compared:\n Previous period", unsafe_allow_html=True)

# Main report title and subtitle on the right
with col2:
    st.subheader("Retweets over time")

# Generate example data if needed
# df = pd.read_excel(uploaded_file, sheet_name=sheet_name) # Uncomment this to use actual data
dates = pd.date_range(start="2023-10-01", end="2023-10-30")
data = {
    'Date': dates,
    'Retweets': [50 + i*2 for i in range(len(dates))],
    'Likes': [60 + i*3 for i in range(len(dates))],
    'Comments': [20 + i for i in range(len(dates))],
}
df = pd.DataFrame(data)

# Plot 1: Retweets over time
fig1, ax1 = plt.subplots(figsize=(6, 3))
ax1.plot(df['Date'], df['Retweets'], color='black', linewidth=2)
ax1.fill_between(df['Date'], df['Retweets'], color='lightgrey', alpha=0.3)
ax1.set_title("Retweets over time", fontsize=14, weight='bold')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
ax1.grid(axis='y', linestyle='--', alpha=0.5)
ax1.set_yticks([])  # Remove y-axis ticks for simplicity
ax1.set_xticks(df['Date'][::4])  # Set fewer x-ticks for readability

# Display the chart in Streamlit
st.pyplot(fig1)

# Plot 2: Engagement rate over time as a stacked bar chart
fig2, ax2 = plt.subplots(figsize=(6, 3))
ax2.bar(df['Date'], df['Comments'], label='Comments', color='skyblue')
ax2.bar(df['Date'], df['Likes'], bottom=df['Comments'], label='Likes', color='blue')
ax2.bar(df['Date'], df['Retweets'], bottom=df['Comments'] + df['Likes'], label='Retweets', color='navy')
ax2.set_title("Engagement rate over time", fontsize=14, weight='bold')
ax2.set_yticks([])  # Remove y-axis ticks for simplicity
ax2.set_xticks(df['Date'][::4])  # Set fewer x-ticks for readability
ax2.grid(axis='y', linestyle='--', alpha=0.5)
ax2.legend(loc='upper right')

# Display the chart in Streamlit
st.pyplot(fig2)

# Metric cards with icons
col3, col4, col5, col6 = st.columns(4)

# Retweets Metric Card
with col3:
    st.markdown("#### Retweets")
    st.markdown("5,753")  # Example metric value
    st.markdown("+4.49%", unsafe_allow_html=True)

# Favorites Metric Card
with col4:
    st.markdown("#### Favorites")
    st.markdown("11,783")  # Example metric value
    st.markdown("+8.90%", unsafe_allow_html=True)

# Engagement Rate Metric Card
with col5:
    st.markdown("#### Engagement rate")
    st.markdown("38.6%")  # Example metric value
    st.markdown("+1.98%", unsafe_allow_html=True)

# Impressions Metric Card
with col6:
    st.markdown("#### Impressions")
    st.markdown("20,683")  # Example metric value
    st.markdown("+7.98%", unsafe_allow_html=True)
