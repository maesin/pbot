import os
import random
import time

try:
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection

pid = os.getpid()

print('start {0}'.format(pid))

time.sleep(random.randint(4, 16))

conn = HTTPConnection('d1oja6z4qyotti.cloudfront.net')
conn.request('GET', '/server.json')

res = conn.getresponse()

if res.status != 200:
    print('error {0}: {1} {2}'.format(pid, res.status, res.reason))


print('fin {0}'.format(pid))
