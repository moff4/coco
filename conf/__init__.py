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


def set_conf(d):
    global conf
    conf = d


def save_conf(f, d=None):
    json.dump(d or get_conf(), f)
