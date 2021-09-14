import uuid

from Services.DataServices.MongoDBTable import MongoDBTable

class ForumsService():

    default_data_service_info = None

    def __init__(self, forum_name, config_info=None, key_columns=None):

        if config_info is None or config_info.get("db_connect_info", None) is None:

            # DFF TODO
            # The default connection information should come from environment information.
            self._db_connect_info = {
                "HOST": "localhost",
                "PORT": 27017,
                "DB": "Forums"
            }
        else:
            self._db_connect_info = config_info.get("db_connect_info")

        self._data_service = MongoDBTable(
            forum_name,
            self._db_connect_info,
            key_columns=key_columns
        )

    def insert_forum(self, forum_dto):
        post_id = uuid.uuid1()
        forum_dto['post_id'] = str(post_id)
        res = self._data_service.insert(forum_dto)
        return res

    def insert_comment(self, comment_dto, post_id):

        template = {"post_id": post_id}
        forum = self._data_service.find_by_template(template)
        forum_children = forum[0]['children']

        comment_id = uuid.uuid1()
        comment_dto['comment_id'] = str(comment_id)
        comment_dto['parent_id'] = post_id

        forum_children.append(comment_dto)
        res = self._data_service.update_forum(template, {"children" : forum_children})
        return res

    def find_by_template(self, template, fields=None):
        res = self._data_service.find_by_template(template, fields)
        return res

    def find_comments(self, template, columns, fields=None):
        res = self._data_service.find_by_query(template, columns, fields)
        return res

    def find_comment_by_id(self, template, comment_id, fields=None):
        res = self._data_service.find_by_template(template, fields)
        if res:
            res = res[0]['children']
            for r in res:
                if r['comment_id'] == comment_id:
                    res = r
        return res