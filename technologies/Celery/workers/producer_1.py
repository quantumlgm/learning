from tasks import add, divide


result_add = add.apply_async(args=(10, 15))


print("Результат отложенной задачи:", result_add.get(timeout=15))
print("Статус после выполнения:", result_add.state)


result_divide = divide.apply_async(args=(10, 0))
print(result_divide)
