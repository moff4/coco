from snc.api import AbstractApi


class FacebookAPI(AbstractApi):
    __default_kwargs = {
        'access_token': None,
        'v': '2.9'
    }
    _API_URL = 'https://graph.facebook.com/v'
    request_rate = 1
    last_request = 0

    @staticmethod
    def merge_params(parameters, new):
        if new:
            parameters.update(new)
        return parameters

    def api_call(self, edge, params):
        url = '%s%s/%s' % (
            self._API_URL,
            self.cfg['v'],
            edge
        )
        return self._request(
            url=url,
            params=params,
            http_method='GET',
        )

    def node_edge(self, node, edge, fields=None, params=None):

        """

        :param node:
        :param edge:
        :param fields:
        :param params:
        :return:
        """
        if fields:
            fields = ','.join(fields)

        parameters = {
            'fields': fields,
        }
        parameters = self.merge_params(parameters, params)

        return self.api_call('%s/%s' % (node, edge), parameters)

    def post(self, post_id, fields=None, **params):

        """

        :param post_id:
        :param fields:
        :param params:
        :return:
        """
        if fields:
            fields = ','.join(fields)

        parameters = {
            'fields': fields,
        }
        parameters = self.merge_params(parameters, params)

        return self.api_call('%s' % post_id, parameters)

    def page_posts(self, page_id, after='', post_type='posts', include_hidden=False, fields=None, **params):

        """

        :param page_id:
        :param after:
        :param post_type: Can be 'posts', 'feed', 'tagged', 'promotable_posts'
        :param include_hidden:
        :param fields:
        :param params:
        :return:
        """
        parameters = {
            'after': after,
            'include_hidden': include_hidden
        }
        if fields is not None:
            parameters['fields'] = ','.join(fields)
        parameters = self.merge_params(parameters, params)

        return self.api_call('%s/%s' % (page_id, post_type), parameters)

    def post_comments(self, post_id, after='', order='chronological', filter='stream', fields=None, **params):

        """

        :param post_id:
        :param after:
        :param order: Can be 'ranked', 'chronological', 'reverse_chronological'
        :param filter: Can be 'stream', 'toplevel'
        :param fields: Can be 'id', 'application', 'attachment', 'can_comment',
        'can_remove', 'can_hide', 'can_like', 'can_reply_privately', 'comments',
        'comment_count', 'created_time', 'from', 'likes', 'like_count',
        'live_broadcast_timestamp', 'message', 'message_tags', 'object',
        'parent', 'private_reply_conversation', 'user_likes'
        :param params:
        :return:
        """
        if fields:
            fields = ','.join(fields)

        parameters = {
            'after': after,
            'order': order,
            'fields': fields,
            'filter': filter
        }
        parameters = self.merge_params(parameters, params)

        return self.api_call('%s/comments' % post_id, parameters)
