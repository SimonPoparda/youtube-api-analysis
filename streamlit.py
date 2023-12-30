import streamlit as st
import pandas as pd
import seaborn as sns
from googleapiclient.discovery import build

# Function to get YouTube channel statistics
def get_channel_stats(youtube, channel_ids):
    all_data = []
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=','.join(channel_ids)
    )
    response = request.execute()

    for i in range(len(response['items'])):
        data = dict(Channel_name=response['items'][i]['snippet']['title'],
                    Subscribers=response['items'][i]['statistics']['subscriberCount'],
                    Views=response['items'][i]['statistics']['viewCount'],
                    Total_videos=response['items'][i]['statistics']['videoCount'])
        all_data.append(data)

    return all_data

# Streamlit App
def main():
    st.title("YouTube Channel Statistics")

    # API Configuration
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "YOUR_API_KEY"  # Replace with your actual API key

    # Get credentials and create an API client
    youtube = build(api_service_name, api_version, developerKey=api_key)

    # Input for Channel IDs
    channel_ids = st.text_area("Enter YouTube Channel IDs (comma-separated):").split(',')

    if st.button("Get Statistics"):
        # Get channel statistics
        channel_statistics = get_channel_stats(youtube, channel_ids)
        channels_data_df = pd.DataFrame(channel_statistics)

        # Change data types
        channels_data_df['Subscribers'] = pd.to_numeric(channels_data_df['Subscribers'])
        channels_data_df['Views'] = pd.to_numeric(channels_data_df['Views'])
        channels_data_df['Total_videos'] = pd.to_numeric(channels_data_df['Total_videos'])

        # Display Data
        st.subheader("Channel Statistics")
        st.write(channels_data_df)

        # Visualize
        st.subheader("Visualize Subscribers")
        sns.set(rc={'figure.figsize': (10, 8)})
        ax = sns.barplot(x='Channel_name', y='Subscribers', data=channels_data_df)
        st.pyplot()

if __name__ == "__main__":
    main()
