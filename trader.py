from get_stock_info import get_stock_info

from collections import deque
import logging

logging.basicConfig(level=logging.INFO)
frames = deque()

for i in range(10):
    frames.appendleft(get_stock_info('MSFT'))
    print(frames)


