# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Posts(TeambitionAPI):

    def get(self, id=None, project_id=None):
        """
        获取分享列表

        :param id: 可选，分享 ID
        :param project_id: 可选，项目 ID
        :return: 返回的 JSON 数据包
        """
        if id:
            endpoint = 'api/posts/{0}'.format(id)
        elif project_id:
            endpoint = 'api/projects/{0}/posts'.format(project_id)
        return self._get(endpoint)

    def create(self, project_id, title, content, post_mode=None,
               visiable='members', involve_members=None,
               tag_ids=None, attachments=None):
        """
        新建分享

        :param project_id: 项目 ID
        :param title: 标题
        :param content: 内容
        :param post_mode: 可选，分享模式
        :param visiable: 可选，可见范围，默认为 members，可选 involves
        :param involve_members: 可选，参与者 ID 列表
        :param tag_ids: 可选，标签 ID 列表
        :param attachments: 可选，附件 ID 列表
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            _projectId=project_id,
            title=title,
            content=content,
            postMode=post_mode,
            visiable=visiable,
            involveMembers=involve_members,
            tagIds=tag_ids,
            attachments=attachments
        )
        return self._post(
            'api/posts',
            data=data
        )

    def delete(self, id):
        """
        删除分享

        :param id: 分享 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/posts/{0}'.format(id))

    def update(self, id, title=None, content=None, post_mode=None,
               attachments=None, pin=None):
        """
        更新分享

        :param id: 分享 ID
        :param title: 可选，标题
        :param content: 可选，内容
        :param post_mode: 可选，分享模式
        :param attachments: 可选，附件 ID 列表
        :param pin: 可选，置顶状态，True/False
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            title=title,
            content=content,
            postMode=post_mode,
            attachments=attachments,
            pin=pin
        )
        return self._put(
            'api/posts/{0}'.format(id),
            data=data
        )

    def like(self, id):
        """
        赞分享

        :param id: 分享 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/posts/{0}/like'.format(id))

    def update_members(self, id, members):
        """
        更新分享参与者

        :param id: 分享 ID
        :param members: 参与者 ID 列表
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/post/{0}'.format(id),
            data={
                'involveMembers': members
            }
        )

    def archive(self, id):
        """
        归档分享

        :param id: 分享 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/posts/{0}/archive'.format(id))

    def unarchive(self, id):
        """
        取消归档分享

        :param id: 分享 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/posts/{0}/archive'.format(id))

    def update_tags(self, id, tag_ids):
        """
        更新分享标签

        :param id: 分享 ID
        :param tags: 标签 ID 列表
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/posts/{0}/tagIds'.format(id),
            data={
                'tagIds': tag_ids
            }
        )

    def get_tags(self, id):
        """
        获取分享标签列表

        :param id: 分享 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/posts/{0}/tags'.format(id))

    def create_tag(self, id, name):
        """
        新建标签

        :param id: 分享 ID
        :param name: 标签名称
        :return: 返回的 JSON 数据包
        """
        return self._post(
            'api/posts/{0}/tags'.format(id),
            data={
                'name': name
            }
        )

    def add_tag(self, id, tag_id):
        """
        关联标签

        :param id: 分享 ID
        :param tag_id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._put('api/posts/{0}/tags/{1}'.format(id, tag_id))
