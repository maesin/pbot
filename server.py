import os
import random
import time


def run():
    pid = os.getpid()

    print('start {0}'.format(pid))

    time.sleep(random.randint(4, 16))

    print('fin {0}'.format(pid))
