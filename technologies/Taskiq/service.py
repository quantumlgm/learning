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