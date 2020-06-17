from get_stock_info import get_stock_info

from collections import deque
from log_config import get_logger

logger = get_logger('trader')

frames = deque()

# for i in range(10):
#     frames.appendleft(get_stock_info('MSFT'))
#     print(frames)


