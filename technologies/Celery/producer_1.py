from tasks import add


result_fast = add.delay(10, 15)
result_delayed = add.apply_async(args=(10, 15), queue="celery")


print("Результат отложенной задачи:", result_delayed.get(timeout=15))
print("Статус после выполнения:", result_delayed.state)
