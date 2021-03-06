#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import datetime
import subprocess

from bottle import abort, request, route, run, template
from easydict import EasyDict as ezdict

command = 'python server.py'


def params():
    p = {}

    if request.query is not None:
        p.update(request.query)

    if request.json is not None:
        p.update(request.json)

    elif request.forms is not None:
        p.update(request.forms)

    return ezdict(p)


@route('/')
def index():
    return 'Hello, world!'


@route('/', method='POST')
def receive():
    p = params()

    proc = subprocess.Popen(command.split(' '))

    result = ezdict()
    result.pid = proc.pid

    return result


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Run server.')

    parser.add_argument(
        '--port',
        '-p',
        nargs='?',
        help='Port (default: 8080)',
        default=8080)

    args = parser.parse_args()

    run(host='0.0.0.0', port=args.port, reloader=True, debug=True)
