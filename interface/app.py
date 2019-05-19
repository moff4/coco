
from tkinter import (
    Frame,
    BOTH,
    Button,
    Label,
    Checkbutton,
    IntVar,
    StringVar,
    Entry,
)
from tkinter.filedialog import (
    askopenfilename,
    asksaveasfile,
)

from conf import (
    get_conf,
    save_conf,
)

DEFAULT_BACKGROUND_COLOR = '#DFFFDF'

TypeMap = {
    'label': Label,
    'entry': Entry,
    'checkbutton': Checkbutton,
    'button': Button,
}


def merge(d1, d2):
    for i in d2:
        if isinstance(d2[i], dict):
            d1[i] = merge(d1.get(i, {}), d2[i])
        if i not in d1:
            d1[i] = d2[i]
    return d1


class APP(Frame):

    defaults = {
        'window': {
            'title': 'title',
            'width': 350,
            'height': 400,
            'offset_x': 200,
            'offset_y': 150,
            'background': DEFAULT_BACKGROUND_COLOR,
        },
        'button': {
            'background': DEFAULT_BACKGROUND_COLOR,
        },
        'label': {
            'background': DEFAULT_BACKGROUND_COLOR,
        },
        'checkbutton': {
            'foreground': 'black',
            'background': DEFAULT_BACKGROUND_COLOR,
        },
        'entry': {
        },
    }

    def __init__(self, P, **kwargs):
        self.cfg = merge(kwargs, self.defaults)
        Frame.__init__(self, P, background=self.cfg['window']['background'])
        self.P = P
        self.initUI()

    def initUI(self):
        self.P.title(self.cfg['window']['title'])
        self.P.geometry('{width}x{height}+{offset_x}+{offset_y}'.format(**self.cfg['window']))
        self.pack(fill=BOTH, expand=1)

        # that's chackbox variables
        # use them to ckeck if checkbox is active
        self.input_variables = {
            'vk': IntVar(),
            'vk_id': StringVar(),
            'vk_token': StringVar(),
            'google': IntVar(),
            'users': IntVar(),
            'first_name': StringVar(),
            'family_name': StringVar(),
            'age': StringVar(),
        }

        objs = [
            [
                TypeMap[obj['type']](
                    self,
                    **obj['prop'],
                    **self.cfg[obj['type']],
                )
            ]
            if isinstance(obj, dict) else [
                TypeMap[_obj['type']](
                    self,
                    **_obj['prop'],
                    **self.cfg[_obj['type']],
                )
                for _obj in obj
            ]
            for obj in [
                {
                    'type': 'label',
                    'prop': {
                        'text': 'Engines',
                    }
                },
                {
                    'type': 'checkbutton',
                    'prop': {
                        'text': 'Use VK',
                        'variable': self.input_variables['vk'],
                    }
                },
                [
                    {
                        'type': 'label',
                        'prop': {
                            'text': 'Vk user id: ',
                        }
                    },
                    {
                        'type': 'entry',
                        'prop': {
                            'textvariable': self.input_variables['vk_id']
                        }
                    },
                ],
                [
                    {
                        'type': 'label',
                        'prop': {
                            'text': 'Vk token: ',
                        }
                    },
                    {
                        'type': 'entry',
                        'prop': {
                            'textvariable': self.input_variables['vk_token']
                        }
                    },
                ],
                {
                    'type': 'checkbutton',
                    'prop': {
                        'text': 'Google search',
                        'variable': self.input_variables['google'],
                    }
                },
                {
                    'type': 'checkbutton',
                    'prop': {
                        'text': 'User input',
                        'variable': self.input_variables['users'],
                    }
                },
                [
                    {
                        'type': 'label',
                        'prop': {
                            'text': 'First name: ',
                        }
                    },
                    {
                        'type': 'entry',
                        'prop': {
                            'textvariable': self.input_variables['first_name']
                        }
                    },
                ],
                [
                    {
                        'type': 'label',
                        'prop': {
                            'text': 'Family name: ',
                        }
                    },
                    {
                        'type': 'entry',
                        'prop': {
                            'textvariable': self.input_variables['family_name']
                        }
                    },
                ],
                [
                    {
                        'type': 'label',
                        'prop': {
                            'text': 'Age: ',
                        }
                    },
                    {
                        'type': 'entry',
                        'prop': {
                            'textvariable': self.input_variables['age']
                        }
                    },
                ],
                [
                    {
                        'type': 'button',
                        'prop': {
                            'text': 'Import',
                            'command': lambda *a, **b: get_conf(askopenfilename())
                        },
                    },
                    {
                        'type': 'button',
                        'prop': {
                            'text': 'Start',
                            # FIXME
                            # add button handler
                            # 'command': lambda *a, **b: True,
                        },
                    },
                    {
                        'type': 'button',
                        'prop': {
                            'text': 'Export',
                            'command': lambda *a, **b: save_conf(asksaveasfile())
                        },
                    },
                    {
                        'type': 'button',
                        'prop': {
                            'text': 'Quit',
                            'command': self.quit,
                        },
                    },
                ],
            ]
        ]
        for i in range(len(objs)):
            for j in range(len(objs[i])):
                objs[i][j].place(
                    x=(
                        (self.cfg['window']['width'] / len(objs[i])) * j
                    ) + (
                        self.cfg['window']['width'] / len(objs[i]) * 0.1
                    ),
                    y=(self.cfg['window']['height'] * i / len(objs)),
                    height=25,
                    width=(self.cfg['window']['width'] / max(2, len(objs[i])) * 0.8),
                )
