import json

from spyne import ServiceBase, rpc, Double
from spyne import Integer, Unicode, String


class User(object):
    def __init__(self, age, user_name):
        self.age = age
        self.user_name = user_name
        self.sex = 0

    def get_user_list(self, current_page, page_size):
        l = []
        for i in range(10):
            l.append({'age': self.age, 'sex': self.sex, 'user_name': self.user_name})
        return l


user_mgr = User(18, 'Tom')


class PyWebService(ServiceBase):
    ...

    @rpc(_returns=Unicode)
    def get_version(self):
        """
        获取系统版本
        :return:
        """
        return json.dumps({'version': 1.0})

    @rpc(Integer, Integer, _returns=Unicode)
    def get_user_list(self, current_page, page_size):
        """
        获取用户列表
        :return:
        """
        return json.dumps(user_mgr.get_user_list(current_page, page_size))
