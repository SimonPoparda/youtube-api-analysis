import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title='Multiple App',
    page_icon='👋',
)

st.title('YouTube API Data Analysis')
st.sidebar.success('Data Analysis of YT Channels')

st.markdown('<p style="font-size:20px;">📊 Basic Statistics for each channel</p>', unsafe_allow_html=True)

channels_data_df = pd.read_csv('channels_data_df.csv')
 # Selectbox for choosing the visualization
st.markdown('<p style="font-size:20px;">📈 Visualization</p>', unsafe_allow_html=True)
selected_chart = st.selectbox("Select Visualization", ["Total Subscribers", "Total Views", "Total Videos"])

sns.set(rc={'figure.figsize': (10, 8)})
if selected_chart == "Total Subscribers":
    ax = sns.barplot(x='Channel_name', y='Subscribers', data=channels_data_df)
    ax.set_title("Total Subscribers")  # Set the title for the bar plot
elif selected_chart == "Total Views":
    ax = sns.barplot(x='Channel_name', y='Views', data=channels_data_df)
    ax.set_title("Total Views")  # Set the title for the bar plot
else:
    ax = sns.barplot(x='Channel_name', y='Total_videos', data=channels_data_df)
    ax.set_title("Total Videos")  # Set the title for the bar plot

st.pyplot(fig=ax.get_figure())
