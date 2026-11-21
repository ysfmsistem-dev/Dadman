from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Dadman"
    demo_mode: bool = True
    llm_base_url: str = ""
    llm_api_key: str = ""
    llm_model: str = ""
    system_prompt: str = (
        "تو دستیار حقوقی فارسی دادمان هستی. پاسخ‌ها را روشن، محتاطانه و به زبان فارسی ارائه کن. "
        "قانون یا رأی قضایی را جعل نکن و در صورت نبود منبع معتبر، صریحاً اعلام کن."
    )
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", case_sensitive=False)

settings = Settings()
