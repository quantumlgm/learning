from tasks import slow_task


result = slow_task.delay(10)


print(result.get(10))