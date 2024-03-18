# from pydantic_settings import BaseSettings, SettingsConfigDict
# from pydantic import SecretStr
#
#
# class BotConfig(BaseSettings):
#     model_config = SettingsConfigDict(env_file='.env',
#                                       env_file_encoding='utf-8')
#     bot_api_key: SecretStr
#
#
# bot_config = BotConfig()

import os

bot_api_key = os.getenv("BOT_API_KEY")
