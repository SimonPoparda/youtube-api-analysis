import streamlit as st
import pandas as pd
from googleapiclient.discovery import build
import seaborn as sns

st.set_page_config(
    page_title='Multiple App',
    page_icon='👋',
)

st.title('YouTube API Data Analysis')
st.sidebar.success('Data Analysis of YT Channels')

st.markdown('<p style="font-size:20px;">📊 Basic Statistics for each channel</p>', unsafe_allow_html=True)

api_key = 'AIzaSyCzltnXE_nObh4xlw0331YmKDi8vqjYtyk'
channel_ids = ['UCnUrMqV57fp3uPddvmDpTaA','UC7RswyY8VfbSdikz_8wdp3w', 
'UCZ7KWO9E51KNtkDN_TfA69Q', 'UC-Q7kWPVNqMsCyy4ZgGE6MA']

api_service_name = "youtube"
api_version = "v3"

# Get credentials and create an API client
youtube = build(
    api_service_name, api_version, developerKey=api_key)

def get_channel_stats(youtube, channel_ids):
    all_data = []
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=','.join(channel_ids)
    )
    response = request.execute()

    for i in range(len(response['items'])):
        data = dict(Channel_name = response['items'][i]['snippet']['title'],
                    Subscribers = response['items'][i]['statistics']['subscriberCount'],
                    Views = response['items'][i]['statistics']['viewCount'],
                    Total_videos = response['items'][i]['statistics']['videoCount'])
        all_data.append(data)
        
    return all_data

channel_statistics = get_channel_stats(youtube, channel_ids)
channel_statistics = get_channel_stats(youtube, channel_ids)
channels_data_df = pd.DataFrame(channel_statistics)
st.write(channels_data_df)

channels_data_df['Subscribers'] = pd.to_numeric(channels_data_df['Subscribers'])
channels_data_df['Views'] = pd.to_numeric(channels_data_df['Views'])
channels_data_df['Total_videos'] = pd.to_numeric(channels_data_df['Total_videos'])

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

# Visualize
# st.markdown('<p style="font-size:20px;">📈 Visualisation</p>', unsafe_allow_html=True)
# sns.set(rc={'figure.figsize': (10, 8)})

# ax_1 = sns.barplot(x='Channel_name', y='Subscribers', data=channels_data_df)
# ax_1.set_title("Total Subsribers")  # Set the title for the bar plot
# st.pyplot(fig=ax_1.get_figure())

# ax_2 = sns.barplot(x='Channel_name', y='Views', data=channels_data_df)
# ax_2.set_title("Total Views")  # Set the title for the bar plot
# st.pyplot(fig=ax_2.get_figure())

# ax_3 = sns.barplot(x='Channel_name', y='Total_videos', data=channels_data_df)
# ax_3.set_title("Total videos")  # Set the title for the bar plot
# st.pyplot(fig=ax_3.get_figure())