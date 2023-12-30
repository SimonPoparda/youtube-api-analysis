import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Multiple App',
    page_icon='👋',
)

st.title('YouTube API Data Analysis')
st.sidebar.success('Data Analysis of YT Channels')

st.markdown('<p style="font-size:20px;">📊 Basic Statistics for each channel</p>', unsafe_allow_html=True)

channels_data_df = pd.read_csv('channels_data_df.csv')

st.markdown('<p style="font-size:20px;">📈 Visualization</p>', unsafe_allow_html=True)
selected_chart = st.selectbox("Select Visualization", ["Total Subscribers", "Total Views", "Total Videos"])

if selected_chart == "Total Subscribers":
    st.bar_chart(channels_data_df.set_index('Channel_name')['Subscribers'])
    st.title("Total Subscribers")
elif selected_chart == "Total Views":
    st.bar_chart(channels_data_df.set_index('Channel_name')['Views'])
    st.title("Total Views")
else:
    st.bar_chart(channels_data_df.set_index('Channel_name')['Total_videos'])
    st.title("Total Videos")
