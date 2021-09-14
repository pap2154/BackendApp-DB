import json

from Services.DataServices.MongoDBTable import MongoDBTable
from Services.ForumsService.ForumService import ForumsService


c_info = {
    "db_connect_info": {
        "HOST": "localhost",
        "PORT": 27017,
        "DB": "new_forum"
    }
}

o_info = {
    "db_connect_info": {
        "HOST": "localhost",
        "PORT": 27017,
        "DB": "classic_models"
    }
}


def t1():
    mt = MongoDBTable("got_forums", c_info["db_connect_info"], key_columns=["forum_id"])
    forum_dto = {
        "forum_id": "1234",
        "forum_name": "Cool"
    }
    fs = ForumsService("GotForums", c_info)
    fs.insert_forum(forum_dto)


def t2():
    mt = MongoDBTable("forum", c_info["db_connect_info"], key_columns=["post_id"])
    fs = ForumsService("forum", c_info, key_columns=["post_id"])

    res = mt.find_by_template({'post_id': '00014f99-a9cc-47ba-9370-a26936aa44f5'},
                                ["postdate", "folders"])
    for r in res:
        print(json.dumps(r, indent=2, default=str))


def t3():
    #mt = MongoDBTable("forum", c_info["db_connect_info"], key_columns=["post_id"])
    fs = ForumsService("forum", c_info, key_columns=["post_id"])

    res = fs.find_by_template({'post_id': "00014f99-a9cc-47ba-9370-a26936aa44f5"})
    for r in res:
        print(json.dumps(r, indent=2, default=str))

#t1()
#t2()
#t3()