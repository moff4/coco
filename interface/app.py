
from tkinter import (
    Frame,
    BOTH,
    Button,
    Label,
    Checkbutton,
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
        btns = [
            {
                'text': 'Import',
            },
            {
                'text': 'Start',
            },
            {
                'text': 'Export',
            },
            {
                'text': 'Quit',
                'command': self.quit,
            },
        ]
        self.buttons = [
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
                    'text': 'use VK',
                }
            },
        ]
        self.checkboxes = {
            chckboxes[i]['key']:
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
        }
