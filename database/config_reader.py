from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8')

    name_db: str
    password: SecretStr
    user: str
    host: str
    port: str


config = Settings()  # type: ignore
