from app import add


result = add.delay(10, 15)


print(result.id)