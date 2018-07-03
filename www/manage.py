#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging; logging.basicConfig(level=logging.INFO)

import asyncio
import os
import json
import time

from datetime import datetime
from aiohttp import web

#请求响应
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

host = '127.0.0.1'
port = 9000
@asyncio.coroutine
#初始化本地服务
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    server = yield from loop.create_server(app.make_handler(), host, port)
    logging.info("server started at http://127.0.0.1:9000...")
    return server

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
