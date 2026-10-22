import random

from tasks import show_info, slow_task


result_fast = show_info.apply_async(args=(10,))
print(result_fast.get(timeout=10))


result_slow = slow_task.delay("TEST")
print(result_slow.get(timeout=4))


results_slow = [slow_task.delay(i) for i in range(0, 4)]
