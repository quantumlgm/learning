import random

from tasks import show_info, slow_task


result_fast = show_info.apply_async(args=(10,))
print(result_fast.get(timeout=10))
