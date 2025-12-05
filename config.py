from enum import Enum
from pathlib import Path
from typing import Self

from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    browser_state_file: FilePath

    def get_base_url(self) -> str:
        return f"{self.app_url}"
    
    def get_image_upload_path(self) -> str:
        return str(self.test_data.image_png_file)

    @classmethod
    def initialize(cls) -> Self:
        videos_dir = Path("./videos")
        tracing_dir = Path("./tracing")
        browser_state_file = Path("browser-state.json")

        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            browser_state_file=browser_state_file
        ) # type: ignore
    
settings = Settings.initialize()