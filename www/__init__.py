#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
import sys
import asyncio
from models import User, Blog, Comment
@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop = loop,host='127.0.0.1',port=3306,user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()

if loop.is_closed():
    sys.exit(0)