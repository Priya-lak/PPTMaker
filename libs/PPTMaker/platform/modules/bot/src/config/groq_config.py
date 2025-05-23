from os import path

from dotenv import dotenv_values

env_path = ".env"

if not path.exists(env_path):
    raise Exception(".env file not found")

config = dotenv_values(env_path)

GROQ_API_KEY = config["GROQ_API_KEY"]


MODEL_NAME = config.get("MODEL_NAME", "meta-llama/llama-4-maverick-17b-128e-instruct")
MAX_TOKENS = int(config.get("MAX_TOKENS", 2000))
