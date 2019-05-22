from snc.api import AbstractApi


class VKAPI(AbstractApi):
    """
        Minimal realization of VK API
    """

    default_kwargs = {
        'access_token': None,
        'v': '5.95',
    }
    _API_URL = 'https://api.vk.com/method/%s'
    last_request = 0
    request_rate = 0.4

    def _request(self, api_method, params=None, http_method='GET'):
        print(api_method, self.cfg)
        if self.cfg['access_token'] is None:
            raise ValueError('access_token is not set')
        if params is None:
            params = {}

        params.update(
            {
                'access_token': self.cfg['access_token'],
                'v': self.cfg['v'],
            }
        )
        return super()._request(
            url=self._API_URL % api_method,
            params=params,
            http_method=http_method,
        )

    def set_access_token(self, access_token):
        """
            set new access_token
        """
        if not isinstance(access_token, str):
            raise TypeError('access_token must be isinstance of str')
        self.cfg['access_token'] = access_token

    def account_getProfileInfo(self):
        return self._request('account.getProfileInfo')

    def friends_get(self, user_id, count=5000, offset=0, order='name'):
        return self._request(
            'friends.get',
            {
                'user_id': user_id,
                'count': count,
                'offset': offset,
                'order': order,
            }
        )

    def groups_get(self, user_id, count=1000, offset=0):
        return self._request(
            'groups.get',
            {
                'user_id': user_id,
                'count': count,
                'offset': offset,
            }
        )

    def users_get(self, user_ids, fields=None):
        """
            possible fields:
            photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50,
            photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig,
            online, domain, has_mobile, contacts, site, education, universities, schools,
            status, last_seen, followers_count, common_count, occupation, nickname,
            relatives, relation, personal, connections, exports, activities, interests,
            music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts,
            can_see_audio, can_write_private_message, can_send_friend_request, is_favorite,
            is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, is_friend,
            friend_status, career, military, blacklisted, blacklisted_by_me
        """
        args = {
            'user_ids': user_ids,
        }
        if fields is not None:
            args['fields'] = fields
        return self._request('users.get', args)
