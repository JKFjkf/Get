import json

with open('items.json') as f:
    rownum = 0
    new_list = json.load(f)
    for i in new_list:
        rownum += 1
        print("""video_title{}:  video_rating:{},  video_name:{}, video_alias{},video_director = {},video_actor = {},video_length = {},video_language = {},video_year = {},video_type = {},video_color = {},video_area = {},video_voice = {},video_summary = {},video_url = {}.""".format(rownum,
                                                                                                                                                                                                                                                                                          i['video_title'][0],
                                                                                                                                                                                                                                                                                          i['video_rating'][0],
                                                                                                                                                                                                                                                                                          i['video_name'][0]))