# YouTube API Analysis

In this project I performed exploratory data analysis on YouTube data that I extracted using API




## Objectives

- Extract data from YouTube channels using API
- Transform it from JSON file to Pandas Dataframe
- Clean data (change formats, etc.)
- Create Visualizations




## Deployment

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

## Authors

- [@Szymon Poparda](https://www.github.com/octokatherine)

