import streamlit as st
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import numpy as np
from PIL import Image
from datetime import datetime

df = pd.read_csv("victor.csv")
# Configure the page   
st.set_page_config(
    page_title="My Colorful App",
    layout="wide",   # makes the app use the full browser width
    initial_sidebar_state="expanded"
)

import streamlit as st

# Page Config
st.set_page_config(
    page_title="Beautiful Streamlit App",
    layout="wide",
)

# Custom HTML + CSS + Bootstrap
st.markdown("""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">

<style>

/* Animated Gradient Background */
.stApp {
    background: linear-gradient(-45deg, #ff6b6b, #6a11cb, #2575fc, #00c9a7);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    overflow: hidden;
}

/* Gradient Animation */
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Bubble Container */
.bubbles {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    overflow: hidden;
    z-index: 0;
}

/* Bubble Style */
.bubbles span {
    position: absolute;
    bottom: -150px;
    width: 40px;
    height: 40px;
    background: rgba(255,255,255,0.25);
    border-radius: 50%;
    animation: rise 20s infinite ease-in;
}

/* Bubble Animation */
@keyframes rise {
    0% {
        transform: translateY(0) scale(1);
        opacity: 0.8;
    }
    100% {
        transform: translateY(-1200px) scale(1.5);
        opacity: 0;
    }
}

/* Random Bubble Positions */
.bubbles span:nth-child(1) {left: 10%; width: 30px; height: 30px; animation-duration: 12s;}
.bubbles span:nth-child(2) {left: 20%; animation-duration: 18s;}
.bubbles span:nth-child(3) {left: 35%; width: 50px; height: 50px; animation-duration: 22s;}
.bubbles span:nth-child(4) {left: 50%; animation-duration: 16s;}
.bubbles span:nth-child(5) {left: 65%; width: 25px; height: 25px; animation-duration: 14s;}
.bubbles span:nth-child(6) {left: 75%; animation-duration: 20s;}
.bubbles span:nth-child(7) {left: 85%; width: 60px; height: 60px; animation-duration: 25s;}
.bubbles span:nth-child(8) {left: 95%; animation-duration: 17s;}

/* Glassmorphism Cards */
.block-container {
    position: relative;
    z-index: 1;
    padding-top: 2rem;
}

div[data-testid="stMetric"], 
div[data-testid="stDataFrame"], 
div[data-testid="stChart"] {
    background: rgba(255,255,255,0.15);
    border-radius: 20px;
    padding: 15px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 32px rgba(0,0,0,0.2);
}

/* Header Styling */
h1, h2, h3 {
    color: white !important;
    text-shadow: 2px 2px 10px rgba(0,0,0,0.4);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(0,0,0,0.3);
    backdrop-filter: blur(10px);
}

</style>

<div class="bubbles">
    <span></span><span></span><span></span><span></span>
    <span></span><span></span><span></span><span></span>
</div>
""", unsafe_allow_html=True)



















# ================= SIDEBAR =================
import streamlit as st
import streamlit as st

with st.sidebar:

    st.markdown("""
    <style>
    .profile-card{
        background: rgba(255,255,255,0.10);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 12px;
        text-align: center;
        color: white;
    }

    .avatar{
        width:55px;
        height:55px;
        border-radius:50%;
        border:2px solid white;
        margin-bottom:6px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="profile-card">
        <img class="avatar" src="my_image.png">
        <div><b>JEGEDE INIOLUWA</b></div>
        <div style="font-size:12px;">Data Analyst</div>
        <div class="status">🟢 Online</div>
    </div>
    """, unsafe_allow_html=True)


#####


df = df.copy()
df['Start date'] = pd.to_datetime(df['Start date'], errors='coerce')

# Create Year + Month columns
df['Year'] = df['Start date'].dt.year
df['Month'] = df['Start date'].dt.month_name()

# Filters
state_filter = st.sidebar.multiselect(
    "State",
    sorted(df['State'].dropna().unique()),
    default=[]
)

incident_filter = st.sidebar.multiselect(
    "Incident",
    sorted(df['Incident'].dropna().unique()),
    default=[]
)

year_filter = st.sidebar.multiselect(
    "Year",
    sorted(df['Year'].dropna().unique()),
    default=[]
)

month_filter = st.sidebar.multiselect(
    "Month",
    ["January","February","March","April","May","June",
     "July","August","September","October","November","December"],
    default=[]
)

# ================= FILTER DATA =================
filtered_df = df.copy()

if state_filter:
    filtered_df = filtered_df[filtered_df['State'].isin(state_filter)]

if incident_filter:
    filtered_df = filtered_df[filtered_df['Incident'].isin(incident_filter)]

if year_filter:
    filtered_df = filtered_df[filtered_df['Year'].isin(year_filter)]

if month_filter:
    filtered_df = filtered_df[filtered_df['Month'].isin(month_filter)]

# No data selected
if filtered_df.empty:
    st.warning("Select filters from sidebar")
    st.stop()


#### liechat
import streamlit as st

# ---------------- CHAT MEMORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- CHAT DISPLAY ----------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div style="text-align:right;">
                <div style="display:inline-block;
                background:#d1f7c4;
                padding:10px;
                border-radius:10px;
                margin:5px;">
                {msg['content']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="text-align:left;">
                <div style="display:inline-block;
                background:#eee;
                padding:10px;
                border-radius:10px;
                margin:5px;">
                {msg['content']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- INPUT ----------------
user_input = st.chat_input("Message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # simple response (replace later with AI)
    st.session_state.messages.append(
        {"role": "assistant", "content": user_input}
    )

    st.rerun()
    
###q1
###q1
st.subheader("1. Trend in Total Deaths Over Time")

# Use filtered_df instead of df
df_year = filtered_df.groupby(filtered_df['Start date'].dt.year)['Number of deaths'].sum().reset_index()
df_year.columns = ['Year', 'Total Deaths']

fig, ax = plt.subplots(figsize=(12, 7))
sns.lineplot(data=df_year, x='Year', y='Total Deaths', marker='o', markersize=8, linewidth=3.5, color='#ff4757')

ax.set_title("Annual Total Deaths Trend (Filtered)", fontsize=18, pad=25, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Total Number of Deaths", fontsize=14)
ax.grid(True, linestyle='--', alpha=0.7)
plt.xticks(df_year['Year'], rotation=45)
plt.tight_layout()

st.pyplot(fig, use_container_width=True)
st.markdown("**Summary:** Annual deaths show clear long-term trends, with noticeable spikes in certain years.")






###q2
st.subheader("2. Top 10 States by Total Deaths")

state_deaths = filtered_df.groupby('State')['Number of deaths'].sum()
fig, ax = plt.subplots()
sns.barplot(x=state_deaths.values, y=state_deaths.index, palette="viridis")
ax.set_title("Top 10 States by Cumulative Deaths", fontsize=16)
ax.set_xlabel("Total Deaths")
plt.tight_layout()
st.pyplot(fig)
st.markdown("**Summary:** These states account for the highest cumulative deaths, highlighting regional severity.")



st.subheader("3. Average Deaths by Incident Type")

incident_avg = filtered_df.groupby('Incident')['Number of deaths'].mean().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=incident_avg.values, y=incident_avg.index, palette="magma", ax=ax)

ax.set_title("Top 10 Most Lethal Incident Types (Avg Deaths)", fontsize=16)
ax.set_xlabel("Average Number of Deaths")
plt.tight_layout()
st.pyplot(fig)
st.markdown("**Summary:** Certain incident types are consistently more lethal, averaging higher deaths per event.")






####Q4
st.subheader("4. Monthly Seasonality of Deaths")

df['Month'] = df['Start date'].dt.month_name()
monthly_deaths = filtered_df.groupby('Month')['Number of deaths'].sum()
fig, ax = plt.subplots()
sns.barplot(x=monthly_deaths.index, y=monthly_deaths.values, palette="coolwarm")
ax.set_title("Total Deaths by Month of the Year", fontsize=16)
plt.xticks(rotation=45)
st.pyplot(fig)
st.markdown("**Summary:** This shows how deaths fluctuate seasonally, revealing which months have the highest fatality counts.")


###Q5   
###Q5
st.subheader("5. States with Longest Average Incident Duration")

# Use filtered_df instead of df
df_dur = filtered_df.copy()

df_dur['Start date'] = pd.to_datetime(df_dur['Start date'], errors='coerce')
df_dur['End date']   = pd.to_datetime(df_dur['End date'], errors='coerce')

df_dur['Duration_days'] = (df_dur['End date'] - df_dur['Start date']).dt.days

df_clean = df_dur.dropna(subset=['Duration_days'])
df_clean = df_clean[df_clean['Duration_days'] >= 0]

if len(df_clean) > 0:
    state_duration = df_clean.groupby('State')['Duration_days'].mean().sort_values(ascending=False).head(10)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x=state_duration.values, y=state_duration.index, palette="plasma", ax=ax)
    
    ax.set_title("Top 10 States by Average Incident Duration (Days)", fontsize=18, pad=25, fontweight='bold')
    ax.set_xlabel("Average Duration (Days)", fontsize=14)
    ax.set_ylabel("State", fontsize=14)
    
    # Add value labels on bars
    for i, v in enumerate(state_duration.values):
        ax.text(v + 0.5, i, f"{v:.1f}", va='center', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    
    st.caption(f"Based on {len(df_clean)} valid incidents with proper start and end dates.")
else:
    st.error("❌ No valid duration data available. Please check your Start date and End date columns.")

st.markdown("**Summary:** Some states experience longer incidents on average, suggesting slower resolution times.")





####q6
st.subheader("6. Top 10 Deadliest Single Incidents")

top_incidents = filtered_df.nlargest(10, 'Number of deaths')[['Identifier','Incident','State','Start date','Number of deaths']]

fig, ax = plt.subplots()
sns.barplot(data=top_incidents, y='Incident', x='Number of deaths', hue='State', dodge=False, palette="rocket")
ax.set_title("Top 10 Deadliest Incidents", fontsize=16)
ax.set_xlabel("Number of Deaths")
plt.tight_layout()
st.pyplot(fig)
st.markdown("**Summary:** The deadliest single incidents stand out, underscoring the most tragic events recorded.")



#####q7
st.subheader("7. Most Volatile States (Highest Variation in Deaths)")

state_std = filtered_df.groupby('State')['Number of deaths'].std().sort_values(ascending=False).head(10)

fig, ax = plt.subplots()
sns.barplot(x=state_std.values, y=state_std.index, palette="cubehelix")
ax.set_title("Top 10 Most Volatile States (Std Dev of Deaths)", fontsize=16)
ax.set_xlabel("Standard Deviation of Deaths")
plt.tight_layout()
st.pyplot(fig)
st.markdown("**Summary:** These states show the widest variation in deaths, indicating highly volatile incident patterns.")



#####q8
st.subheader("8. Average Deaths per Incident by State")

pivot = filtered_df.pivot_table(values='Number of deaths', index='State', aggfunc='mean')
pivot = pivot.sort_values(by='Number of deaths', ascending=False).head(15)

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(pivot, annot=True, fmt=".1f", cmap="YlOrRd", linewidths=0.5)
ax.set_title("Average Deaths per Incident by State", fontsize=16)
st.pyplot(fig)
st.markdown("**Summary:** Average deaths per incident differ by state, with some consistently more deadly than others.")



#####q9
st.subheader("9. Cumulative Deaths Trend - Top 5 States")

top_states = filtered_df.groupby('State')['Number of deaths'].sum().nlargest(5).index
cumulative = filtered_df[filtered_df['State'].isin(top_states)].copy()
cumulative = cumulative.sort_values('Start date')
cumulative['Cumulative_Deaths'] = cumulative.groupby('State')['Number of deaths'].cumsum()

fig, ax = plt.subplots()
for state in top_states:
    state_data = cumulative[cumulative['State'] == state]
    sns.lineplot(data=state_data, x='Start date', y='Cumulative_Deaths', label=state, linewidth=2.5)

ax.set_title("Cumulative Deaths Over Time (Top 5 States)", fontsize=16)
ax.set_ylabel("Cumulative Number of Deaths")
plt.xticks(rotation=45)
plt.legend(title="State")
st.pyplot(fig)
st.markdown("**Summary:** Cumulative deaths reveal how the top five states have built up fatalities over time.")
