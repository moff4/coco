from snc import VKAPI
from generator.brick import (
    Word,
    Date,
    NickName,
    Name,
)


class GeneratePassword():

    brick_map = {
        'vk_bdate': Date,
        'vk_first_name': Name,
        'vk_last_name': Name,
        'vk_domain': NickName,
        'u_age': Date,
        'u_first_name': Name,
        'u_family_name': Name,
    }

    def __init__(self, input):
        self.info = {k: input[k] for k in input if k.startswith('u_')} if input['users'] else {}
        self.info.update(
            {
                f'vk_{key}': item[key]
                for item in VKAPI(
                    access_token=input['vk_token'],
                    fields={
                        'domain',
                        'bdate',
                    }
                ).users_get(
                    input['vk_id']
                ).get(
                    'response',
                    [],
                )
                for key in {'first_name', 'last_name', 'bdate', 'domain'}
                if key in item
            }
            if input['vk'] else
            {}
        )

    def pswd(self):
        for key, var in self.info.items():
            if key in self.brick_map:
                try:
                    yield from self.brick_map[key](var).mutate()
                except (AssertionError, AttributeError) as e:
                    print(e)
