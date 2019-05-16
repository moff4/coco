#!/usr/bin/env python3
import json

conf = None


def get_conf(filename=None):
    global conf
    if filename is None and conf is None:
        raise ValueError('config not loaded')
    if filename is not None:
        with open(filename, 'r') as f:
            conf = json.load(f)
    return conf


def save_conf(f):
    json.dump(get_conf(), f)
