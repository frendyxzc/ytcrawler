import json

def gen_default_config():
    ret = {}

    ret["home"] = gen_home()
    ret["genres"] = gen_genres()
    ret["list"] = gen_list()

    return ret


"""
Home
"""

HOME_CONTENT_ID = "PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI,category_1"
HOME_CONTENT_NAME = "HOT,NEW"
HOME_CONTENT_IMAGE = ","
HOME_CONTENT_VIEW_TYPE = "0,1"
HOME_CONTENT_ACTION_TYPE = "1,0"
HOME_CONTENT_ITEM_NUM = "5,5"

def gen_home():
    home = {}

    home["banner"] = gen_home_detail(
        HOME_CONTENT_ID, HOME_CONTENT_NAME, HOME_CONTENT_IMAGE,
        HOME_CONTENT_VIEW_TYPE, HOME_CONTENT_ACTION_TYPE, HOME_CONTENT_ITEM_NUM)
    home["menu"] = gen_home_detail(
        HOME_CONTENT_ID, HOME_CONTENT_NAME, HOME_CONTENT_IMAGE,
        HOME_CONTENT_VIEW_TYPE, HOME_CONTENT_ACTION_TYPE, HOME_CONTENT_ITEM_NUM)
    home["content"] = gen_home_detail(
        HOME_CONTENT_ID, HOME_CONTENT_NAME, HOME_CONTENT_IMAGE,
        HOME_CONTENT_VIEW_TYPE, HOME_CONTENT_ACTION_TYPE, HOME_CONTENT_ITEM_NUM)

    return home

def gen_home_detail(ID, NAME, IMAGE, VIEW_TYPE, ACTION_TYPE, ITEM_NUM):
    home_content = []

    contents_id = ID.split(",")
    contents_name = NAME.split(",")
    contents_image = IMAGE.split(",")
    contents_view_type = VIEW_TYPE.split(",")
    contents_action_type = ACTION_TYPE.split(",")
    contents_item_num = ITEM_NUM.split(",")

    for index, id in enumerate(contents_id):
        object = {}
        object["id"] = contents_id[index]
        object["name"] = contents_name[index]
        object["image"] = contents_image[index]
        object["viewType"] = contents_view_type[index]
        object["actionType"] = contents_action_type[index]
        object["itemNum"] = contents_item_num[index]
        home_content.append(object)

    return home_content


"""
Genres
"""

def gen_genres():

    GENRES_ID = read_file_to_list("genres_id")
    GENRES_NAME = read_file_to_list("genres_name")
    GENRES_IMAGE = []

    return gen_genres_detail(GENRES_ID, GENRES_NAME, GENRES_IMAGE)

def gen_genres_detail(ID, NAME, IMAGE):
    genres_content = []

    for index, id in enumerate(ID):
        object = {}
        object["id"] = ID[index]
        object["name"] = NAME[index]
        if index < len(IMAGE):
            object["image"] = IMAGE[index]
        else:
            object["image"] = ""
        genres_content.append(object)

    return genres_content


"""
Play List
"""

PLAY_LIST = "PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI,PLFgquLnL59akA2PflFpeQG9L01VFg90wS"

def gen_list():
    list = PLAY_LIST.split(",")

    return gen_play_list(list)

def gen_play_list(LIST):
    play_list = []

    for list in LIST:
        object = {}
        object[list] = read_file(list)
        play_list.append(object)

    return play_list


"""
Read File
"""

def read_file(file_name):
    file = "./data/" + file_name

    with open(file, 'rb') as data:
        return json.load(data)

def read_file_to_list(file_name):
    list = []
    file = "./data/" + file_name
    content = open(file)

    for line in content:
        list.append(line.replace("\n", ""))

    return list