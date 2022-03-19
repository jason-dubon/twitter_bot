from random import randint

from googleapiclient.discovery import build

api_key = 'XXXX'


def get_video():
    youtube = build('youtube','v3',developerKey = api_key)

    test = youtube.channels().list(
        part='contentDetails',
        id='XXXX'
    )

    videos = youtube.playlistItems().list(
        part='snippet',
        playlistId='XXX',
        maxResults=12
    )

    my_data = videos.execute()

    #print(test.execute())

    data_list = my_data['items']
    video_id = data_list[0].get("snippet").get("resourceId").get('videoId')
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    #print(data_list[0].get("snippet").get('title'))
    #print(video_id)
    #print(video_url)

    all_video_urls = []

    for i in data_list:
        vidID = i.get("snippet").get("resourceId").get('videoId')
        vid_title = i.get("snippet").get('title')
        new_title = vid_title[:vid_title.find("|")-1]
        all_video_urls.append(f"{new_title}: https://www.youtube.com/watch?v={vidID}")

    num = randint(0, 11) # returns random int to randomly select a video
    #print(all_video_urls)
    return all_video_urls[num]