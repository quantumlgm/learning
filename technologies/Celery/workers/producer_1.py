from tasks import add


result = add.apply_async(args=(10, 15))


print("Результат отложенной задачи:", result.get(timeout=15))
print("Статус после выполнения:", result.state)
