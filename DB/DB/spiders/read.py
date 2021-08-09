import json
import pandas as pd
with open('review.json') as f:
    frame = pd.DataFrame(json.load(f))
    frame.rename(columns={'review_title':'评审标题','review_content':'查看内容','review_author':'评论人','review_music':'音乐','review_time':'时间','review_url':'连接'})
    #print(frame.to_csv('歌曲.csv'))
    print(frame)
