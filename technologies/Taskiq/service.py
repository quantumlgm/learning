from taskiq import TaskiqMiddleware


class FakeDatabaseConnection:
    is_connected: bool = True

    @staticmethod
    async def commit():
        print("[DB] Изменения применены")

    @staticmethod
    async def rollback():
        print("[DB] Изменения зафиксированы")

    async def close(self):
        self.is_connected = False
        print("[DB] Соединение закрыто")


class LoggingMidlware(TaskiqMiddleware):
    async def pre_send(self, message):
        print(f"[PRODUCER]: Готовимся к отправке - {message.task_name}")

    async def post_send(self, message):
        print(f"[PRODUCER]: Сообщение отправлено в сеть - {message.task_name}")

    async def pre_execute(self, message):
        print(f"[CONSUMER]: Начало выполнения задачи - {message.task_name}")

    async def post_execute(self, message, result):
        print(f"[CONSUMER]: Задача выполнена штатно - {message.task_name} за {result.execution_time}с")

    async def on_error(self, message, result, exception):        
        print(f"[CONSUMER]: Заджача выполнена с ошибкой - {message.task_name} за {result.execution_time}с. Ошибка: {exception}")
        