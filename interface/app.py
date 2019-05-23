
from tkinter import (
    Frame,
    BOTH,
    Button,
    Label,
    Checkbutton,
    IntVar,
    StringVar,
    Entry,
    messagebox,
)
from tkinter.filedialog import (
    askopenfilename,
    asksaveasfile,
)

from conf import (
    get_conf,
    save_conf,
)

import os
from generator.passwords import GeneratePassword
import gettext
_ = gettext.gettext

en = gettext.translation('base', localedir=os.path.join('locales'), languages=['en'])
en.install()
_ = en.gettext  # English

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
    """
        Class for collecting user's input
    """

    # default interface properties
    __defaults = {
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
        self.cfg = merge(kwargs, self.__defaults)
        Frame.__init__(self, P, background=self.cfg['window']['background'])
        self.P = P
        self.initUI()

    def start_button_click(self):
        """
            Start button click handler
        """
        cfg = {k: self.input_variables[k].get() for k in self.input_variables}
        if cfg['vk']:
            if not cfg['vk_token']:
                return messagebox.showerror(_('Something missing'), _('Please, write VK access_token'))
            if not cfg['vk_id']:
                return messagebox.showerror(_('Something missing'), _('Please, write VK user_id'))
            if not cfg['vk_id'].isdigit():
                return messagebox.showerror(_('Something missing'), _('Please, write valid VK user_id (only digits)'))
            cfg['vk_id'] = int(cfg['vk_id'])

        if cfg['users']:
            if not cfg['u_first_name']:
                return messagebox.showerror(_('Something missing'), _('Please, write users\'s first name'))
            if not cfg['u_family_name']:
                return messagebox.showerror(_('Something missing'), _('Please, write users\'s family name'))
            if not cfg['u_age']:
                return messagebox.showerror(_('Something missing'), _('Please, write users\'s age'))

        out_stream = asksaveasfile()
        if out_stream:
            for i in GeneratePassword(cfg).pswd():
                if i:
                    out_stream.write(''.join([i, '\n']))

        messagebox.showinfo(_('Success!'), _('Passwords saved!'))

    def import_button_click(self):
        """
            Import button click handler
        """
        cfg = get_conf(askopenfilename())
        for k in self.input_variables:
            if k in cfg:
                self.input_variables[k].set(cfg[k])

    def export_button_click(self):
        """
            Export button click handler
        """
        save_conf(
            asksaveasfile(),
            {
                k: self.input_variables[k].get()
                for k in self.input_variables
            }
        )

    def initUI(self):
        """
            Initialize user interface
        """
        self.P.title(self.cfg['window']['title'])
        self.P.geometry('{width}x{height}+{offset_x}+{offset_y}'.format(**self.cfg['window']))
        self.pack(fill=BOTH, expand=1)

        # all user's input
        self.input_variables = {
            'vk': IntVar(),
            'vk_id': StringVar(),
            'vk_token': StringVar(),
            'google': IntVar(),
            'users': IntVar(),
            'u_first_name': StringVar(),
            'u_family_name': StringVar(),
            'u_age': StringVar(),
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
                        'text': _('Engines'),
                    }
                },
                {
                    'type': 'checkbutton',
                    'prop': {
                        'text': _('Use VK'),
                        'variable': self.input_variables['vk'],
                    }
                },
                [
                    {
                        'type': 'label',
                        'prop': {
                            'text': _('Vk user id: '),
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
                            'text': _('Vk token: '),
                        }
                    },
                    {
                        'type': 'entry',
                        'prop': {
                            'textvariable': self.input_variables['vk_token']
                        }
                    },
                ],
                # Decomment after implementation
                # {
                #     'type': 'checkbutton',
                #     'prop': {
                #         'text': 'Google search',
                #         'variable': self.input_variables['google'],
                #     }
                # },
                {
                    'type': 'checkbutton',
                    'prop': {
                        'text': _('User input'),
                        'variable': self.input_variables['users'],
                    }
                },
                [
                    {
                        'type': 'label',
                        'prop': {
                            'text': _('First name: '),
                        }
                    },
                    {
                        'type': 'entry',
                        'prop': {
                            'textvariable': self.input_variables['u_first_name']
                        }
                    },
                ],
                [
                    {
                        'type': 'label',
                        'prop': {
                            'text': _('Family name: '),
                        }
                    },
                    {
                        'type': 'entry',
                        'prop': {
                            'textvariable': self.input_variables['u_family_name']
                        }
                    },
                ],
                [
                    {
                        'type': 'label',
                        'prop': {
                            'text': _('Date of birth: '),
                        }
                    },
                    {
                        'type': 'entry',
                        'prop': {
                            'textvariable': self.input_variables['u_age']
                        }
                    },
                ],
                [
                    {
                        'type': 'button',
                        'prop': {
                            'text': _('Import'),
                            'command': self.import_button_click
                        },
                    },
                    {
                        'type': 'button',
                        'prop': {
                            'text': _('Start'),
                            'command': self.start_button_click,
                        },
                    },
                    {
                        'type': 'button',
                        'prop': {
                            'text': _('Export'),
                            'command': self.export_button_click
                        },
                    },
                    {
                        'type': 'button',
                        'prop': {
                            'text': _('Quit'),
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
