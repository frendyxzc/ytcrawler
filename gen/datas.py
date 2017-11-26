# -*- coding: utf-8 -*-
import json

def gen_default_config():
    ret = {}

    ret["home"] = gen_home()
    # 相关列表
    ret["list"] = gen_list()

    return ret


"""
Home
"""

def gen_home():
    home = {}
    home["content"] = gen_home_detail("home_content")

    return home

def gen_home_detail(file_name):
    home_content = []

    file = "./data/" + file_name
    content = open(file)

    for line in content:
        data = line.replace("\n", "").split(",")
        object = {}
        object["id"] = data[0]
        object["name"] = data[1]
        object["dataType"] = data[2]
        object["maxNum"] = data[3]
        object["itemNum"] = data[4]
        object["image"] = data[5]
        object["viewType"] = data[6]
        object["actionType"] = data[7]
        home_content.append(object)

    return home_content


def gen_content_detail(ID, NAME):
    genres_content = []

    for index, id in enumerate(ID):
        object = {}
        object["id"] = ID[index]
        object["name"] = NAME[index]
        genres_content.append(object)

    return genres_content


"""
Play List
"""

PLAY_LIST = "PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI"

def gen_list():
    all_list = {}

    list = PLAY_LIST.split(",")
    # dataType 0
    all_list["menuList"] = gen_menu_list("menu_list")
    # dataType 1
    all_list["playList"] = gen_play_list(list)
    all_list["menuItem"] = gen_menu_item()

    return all_list

def gen_play_list(LIST_ID):
    play_list = []

    for id in LIST_ID:
        object = {}
        object["id"] = id
        object["list"] = read_file(id)
        play_list.append(object)

    return play_list

def gen_menu_list(file_name):
    menu_list = []

    file = "./data/" + file_name
    content = open(file)

    for line in content:
        data = line.replace("\n", "").split(",")
        ID = read_file_to_list(data[0] + "_id")
        NAME = read_file_to_list(data[0] + "_name")

        object = {}
        object["id"] = data[0]
        object["dataType"] = data[1]
        object["list"] = gen_content_detail(ID, NAME)
        menu_list.append(object)

    return menu_list

def gen_menu_item():
    MENU_ITEM_LIST = "banner_item"
    LIST = MENU_ITEM_LIST.split(",")
    menu_item_list = []

    for list_file in LIST:
        object = {}
        object["id"] = list_file.replace("_item", "")
        object["items"] = read_menu_item(list_file)
        menu_item_list.append(object)

    return menu_item_list

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

def read_menu_item(file_name):
    list = []
    file = "./data/" + file_name
    content = open(file)

    for line in content:
        data = line.replace("\n", "").split(",")
        object = {}
        object["id"] = data[0]
        object["name"] = data[1]
        object["image"] = data[2]
        object["dataType"] = data[3]
        list.append(object)

    return list
