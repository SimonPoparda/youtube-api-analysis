# YouTube API Analysis

In this project I performed exploratory data analysis on YouTube data that I extracted using API




## Objectives

- Extract data from YouTube channels using API
- Transform it from JSON file to Pandas Dataframe
- Clean data (change formats, etc.)
- Create Visualizations



# Deployment
## Getting statistics for the channels

- Generate an API key
  
![](images/yt_api.png)

- Set up an enviroment in Jupyter Notebooks by using "pip install"
  
![](images/yt_docs.png)

- Loading the data
``` python
from googleapiclient.discovery import build
import pandas as pd
from IPython.display import JSON
```

![](images/api_key.png)

``` python
api_service_name = "youtube"
api_version = "v3"

# Get credentials and create an API client
youtube = build(
    api_service_name, api_version, developerKey=api_key)
```

``` python
# view response
request = youtube.channels().list(
    part="snippet,contentDetails,statistics",
    id=','.join(channel_ids)
)
response = request.execute()
print(response)
```

``` python
# put data into a list
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
```

``` python
channel_statistics = get_channel_stats(youtube, channel_ids)
channels_data_df = pd.DataFrame(channel_statistics)
channels_data_df
```

- Change data types
``` python
channels_data_df['Subscribers'] = pd.to_numeric(channels_data_df['Subscribers'])
channels_data_df['Views'] = pd.to_numeric(channels_data_df['Views'])
channels_data_df['Total_videos'] = pd.to_numeric(channels_data_df['Total_videos'])
channels_data_df.dtypes
```

- Visualize
``` python
import seaborn as sns
sns.set(rc={'figure.figsize':(10,8)})
ax = sns.barplot(x='Channel_name', y='Subscribers', data=channels_data_df)
```

## Getting statistics for the videos

- Choosing the channel that I want to analyse
``` python
choose_channel = 'Szymon mówi'
chosen_channel_ID = channels_data_df.loc[channels_data_df['Channel_name']==choose_channel]['Playlist_id'].iloc[0]
chosen_channel_ID
```

- Collecting video_ids
``` python
def get_video_ids(youtube, chosen_channel_ID):
    request = youtube.playlistItems().list(
    part="contentDetails",
    playlistId=chosen_channel_ID,
    maxResults=50
    )
    response = request.execute()

    video_ids = []

    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])

    #NEXT PAGE TOKEN
    next_page_token = response.get('nextPageToken')
    more_pages = True

    while more_pages == True:
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                part="contentDetails",
                playlistId=chosen_channel_ID,
                maxResults=50,
                pageToken= next_page_token
            )
            response = request.execute()

            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])

            next_page_token = response.get('nextPageToken')

    return video_ids
  ```
- Getting the video details
``` python
def get_video_details(youtube, video_ids):
    all_video_stats = []

    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=",".join(video_ids[i:i+50]) #bierze po 50 itemów z listy, bo więcej się nie dało
        )
        response = request.execute()

        for i in range(len(response['items'])):
            video_stats = dict(
                Title=response['items'][i]['snippet']['title'],
                Published_date=response['items'][i]['snippet']['publishedAt'],
                Duration=response['items'][i]['contentDetails']['duration'],
                Views=response['items'][i]['statistics']['viewCount'],
                Likes=response['items'][i]['statistics']['likeCount'],
                Comments=response['items'][i]['statistics']['commentCount']
            )
            all_video_stats.append(video_stats)

    return all_video_stats
```

``` python
videos_data_df = pd.DataFrame(video_details)
videos_data_df
```

## Authors

- [@Szymon Poparda](https://www.github.com/octokatherine)

