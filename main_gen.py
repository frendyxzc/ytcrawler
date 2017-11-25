#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json

from gen.datas import gen_default_config

FILE_NAME = "./gen/default_config.json"

data = gen_default_config()

with open(FILE_NAME,"w") as dump:
    json.dump(data, dump)

# with open(FILE_NAME,'rb') as data:
#     print(json.load(data))