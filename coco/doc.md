Module main
===========

Functions
---------

    
`main()`
:   Application for generation simple relevante passwords depends on known information about user


Module interface
================

Sub-modules
-----------
* interface.app

Classes
-------

`APP(P, **kwargs)`
:   Class for collecting user's input
    
    Construct a frame widget with the parent MASTER.
    
    Valid resource names: background, bd, bg, borderwidth, class,
    colormap, container, cursor, height, highlightbackground,
    highlightcolor, highlightthickness, relief, takefocus, visual, width.

    ### Ancestors (in MRO)

    * tkinter.Frame
    * tkinter.Widget
    * tkinter.BaseWidget
    * tkinter.Misc
    * tkinter.Pack
    * tkinter.Place
    * tkinter.Grid

    ### Methods

    `export_button_click(self)`
    :   Export button click handler

    `import_button_click(self)`
    :   Import button click handler

    `initUI(self)`
    :   Initialize user interface

    `start_button_click(self)`
    :   Start button click handler


Module snc
==========
Social network crawler
Has already made API for VK

Sub-modules
-----------
* snc.api
* snc.vk_api

Classes
-------

`VKAPI(**kwargs)`
:   Minimal realization of VK API
    
    :param kwargs: default arguments for API

    ### Ancestors (in MRO)

    * snc.api.AbstractApi

    ### Class variables

    `default_kwargs`
    :

    `last_request`
    :

    `request_rate`
    :

    ### Methods

    `account_getProfileInfo(self)`
    :   Return info about current's user's profile
        :return: dict with user info

    `friends_get(self, user_id, count=5000, offset=0, order='name')`
    :   Return info about user's friends
        :return: dict with user friends' info

    `groups_get(self, user_id, count=1000, offset=0)`
    :   Return info about user's groups
        :param user_id:
        :param count: number of user groups
        :param offset: group list offset
        :return: dict with group info

    `set_access_token(self, access_token)`
    :   Set new access_token
        :param access_token:

    `users_get(self, user_ids, fields=None)`
    :   Return info about user
        :param fields:
            photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50,
            photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig,
            online, domain, has_mobile, contacts, site, education, universities, schools,
            status, last_seen, followers_count, common_count, occupation, nickname,
            relatives, relation, personal, connections, exports, activities, interests,
            music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts,
            can_see_audio, can_write_private_message, can_send_friend_request, is_favorite,
            is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, is_friend,
            friend_status, career, military, blacklisted, blacklisted_by_me
        :return: given fields with completed info


Module generator
================

Sub-modules
-----------
* generator.brick
* generator.mutation
* generator.passwords
