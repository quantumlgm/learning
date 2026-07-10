from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    DB_PASSWORD: str
    DB_USER: str

    def DB_URL_psycopg(self):
        return f'postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}//{self.DB_NAME}'
    
    def DB_URL_psycopg(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}//{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()