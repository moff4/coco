
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
        }
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
            'google': IntVar(),
            'users': IntVar(),
            'nick': StringVar()
        }

        btns = [
            {
                'text': 'Import',
                'command': lambda *a, **b: get_conf(askopenfilename())
            },
            {
                'text': 'Start',
                # FIXME
                # add button handler
                # 'command': lambda *a, **b: True,
            },
            {
                'text': 'Export',
                'command': lambda *a, **b: save_conf(asksaveasfile())
            },
            {
                'text': 'Quit',
                'command': self.quit,
            },
        ]
        [
            Button(self, **btns[i], **self.cfg['button']).place(
                x=(self.cfg['window']['width'] / len(btns)) * i + (self.cfg['window']['width'] / len(btns) * 0.1),
                y=(self.cfg['window']['height'] - self.cfg['window']['height'] * 0.1),
                height=25,
                width=(self.cfg['window']['width'] / len(btns) * 0.8),
            )
            for i in range(len(btns))
        ]
        Label(
            self,
            text='Engines',
            **self.cfg['label']
        ).place(
            x=(self.cfg['window']['width'] * 0.1),
            y=(self.cfg['window']['height'] * 0.05),
            height=25,
            width=(self.cfg['window']['width'] / 2 * 0.8),
        )

        chckboxes = [
            {
                'key': 'vk',
                'prop': {
                    'text': 'Use VK',
                    'variable': self.input_variables['vk'],
                }
            },
            {
                'key': 'google',
                'prop': {
                    'text': 'Google search',
                    'variable': self.input_variables['google'],
                }
            },
            {
                'key': 'users',
                'prop': {
                    'text': 'User input',
                    'variable': self.input_variables['users'],
                    'command': lambda: print('checkbutton click: '),
                }
            },
        ]
        [
            Checkbutton(
                self,
                **chckboxes[i]['prop'],
                **self.cfg['checkbutton'],
            ).place(
                x=(self.cfg['window']['width'] * 0.1),
                y=(self.cfg['window']['height'] * (0.15 + 0.1 * i)),
                height=25,
                width=(self.cfg['window']['width'] / 2 * 0.8),
            )
            for i in range(len(chckboxes))
        ]
        Entry(
            self,
            textvariable=self.input_variables['nick'],
        ).place(
            x=(self.cfg['window']['width'] * 0.1),
            y=(self.cfg['window']['height'] * (0.45 + 0.1 * 0)),
            height=25,
            width=(self.cfg['window']['width'] / 2 * 0.8)
        )
