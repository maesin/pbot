#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import datetime
import server

from bottle import abort, request, route, run, template
from easydict import EasyDict as ezdict
from multiprocessing import Process


def params():
    p = {}

    if request.query is not None:
        p.update(request.query)

    if request.json is not None:
        p.update(request.json)

    elif request.forms is not None:
        p.update(request.forms)

    return ezdict(p)


def summon(args):
    server.run()


@route('/')
def index():
    return 'Hello, world!'


@route('/', method='POST')
def receive():
    p = params()

    proc = Process(target=summon, args=(p,))
    proc.start()

    result = ezdict()

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
