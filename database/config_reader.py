from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8')

    name_db: str
    password_db: SecretStr
    user_db: str
    host_db: str
    port_db: str


config = Settings()  # type: ignore
