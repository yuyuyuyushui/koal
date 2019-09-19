from core.rest_client import RestClient


class RoleManage(RestClient):
    def __init__(self, api_url, **kwargs):
        super(RoleManage, self).__init__(api_url, **kwargs)

    def add_role(self, **kwargs):
        """
        增加角色
        :param kwargs:
        :return:
        """
        return self.post("/v1/role", **kwargs)

    def update_role(self,roleid, **kwargs):
        """
        修改角色
        :return:
        """
        return self.put('/v1/role/{}'.format(roleid), **kwargs)

    def delete_role(self,roleid, **kwargs):
        """
        删除角色
        :param roleid:
        :param kwargs:
        :return:
        """
        return self.delete("/v1/role/{}".format(roleid),**kwargs)

    def query_function_menu(self, role_id, **kwargs):
        """
        检索权限功能菜单
        :param role_id:
        :param kwargs:
        :return:
        """
        return self.get('/v1/role/menuList/{}'.format(role_id), **kwargs)

    def system_role_list(self,**kwargs):
        """
        系统角色列表
        :param kwargs:
        :return:
        """
        return self.get('/v1/role/list', **kwargs)

    def role_user_list(self,**kwargs):
        """
        角色用户列表
        :param kwargs:
        :return:
        """
        return self.get('/v1/role/userList',**kwargs)

    def role_permissin_settings(self, role_id, **kwargs):
        """
        角色权限设置
        :param role_id:
        :param kwargs:
        :return:
        """
        return self.post('/v1/role/verb/{}'.format(role_id), **kwargs)

    def remove_role_user(self,**kwargs):
        """
        移除角色下的用户
        :param kwargs:
        :return:
        """
        return self.put("/v1/role/removeUser",**kwargs)

    def query_system_role(self,roleid,**kwargs):
        """
        查看系统角色
        :param roleid:
        :param kwargs:
        :return:
        """
        return self.get('/v1/role/{}'.format(roleid), **kwargs)
