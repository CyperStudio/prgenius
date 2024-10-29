import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as patches
import streamlit as st

# Streamlit file uploader
st.title("Twitter Analytics Report")
uploaded_file = st.file_uploader("Upload an Excel file", type="xlsx")

if uploaded_file:
    # Load data
    sheet_name = 'Nudge Reporting'  # Adjust if needed
    df = pd.read_excel(uploaded_file, sheet_name=sheet_name)

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Define metrics and calculations
    metrics = {
        "Retweets": int(df['No. RT'].sum()),
        "Favorites": int(df['No. Likes'].sum()),
        "Impressions": int(df['No. Impressions p/Tweet'].sum()),
        "Followers": int(df['No. Followers'].max()),
        "Comments": int(df['No. Comments'].sum())
    }

    # Define icon colors for each metric
    icon_colors = {
        "Retweets": "cornflowerblue",
        "Favorites": "salmon",
        "Impressions": "seagreen",
        "Followers": "orange",
        "Comments": "purple"
    }

    # Define icon positions on the plot
    metrics_positions = {
        "Retweets": (0.65, 0.6),
        "Favorites": (0.65, 0.4),
        "Impressions": (0.85, 0.6),
        "Followers": (0.85, 0.4),
        "Comments": (0.75, 0.2)
    }

    # Plotting
    fig = plt.figure(figsize=(14, 10))
    fig.suptitle("Twitter Analytics Report", fontsize=20, weight='bold')

    # Plot "Retweets over time"
    ax1 = fig.add_subplot(221)
    ax1.plot(df['Date'], df['No. RT'], color='black', linewidth=2)
    ax1.set_title("Retweets over time", fontsize=14, weight='bold')
    ax1.set_ylim(0, max(df['No. RT']) * 1.2)
    ax1.set_ylabel("Retweets")
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
    ax1.grid(axis='y', linestyle='--', alpha=0.7)

    # Plot "Engagement rate over time" as a stacked bar chart for Comments, Likes, and Retweets
    ax2 = fig.add_subplot(223)
    ax2.bar(df['Date'], df['No. Comments'], label='Comments', color='skyblue')
    ax2.bar(df['Date'], df['No. Likes'], bottom=df['No. Comments'], label='Likes', color='blue')
    ax2.bar(df['Date'], df['No. RT'], bottom=df['No. Comments'] + df['No. Likes'], label='Retweets', color='navy')
    ax2.set_title("Engagement rate over time", fontsize=14, weight='bold')
    ax2.set_ylabel("Engagement")
    ax2.legend(loc='upper right')
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
    ax2.grid(axis='y', linestyle='--', alpha=0.7)

    # Add metric icons with colored rectangles and text
    for label, pos in metrics_positions.items():
        color = icon_colors[label]
        # Draw rectangle as an icon
        rect = patches.Rectangle((pos[0]-0.025, pos[1]-0.05), 0.05, 0.05, color=color, transform=fig.transFigure, clip_on=False)
        fig.patches.append(rect)
        # Add text for each metric
        fig.text(pos[0], pos[1], f"{label}\n{metrics[label]:,}", ha='center', fontsize=12, weight='bold', color=color)

    # Display plot in Streamlit
    st.pyplot(fig)
