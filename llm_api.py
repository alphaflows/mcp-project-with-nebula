from dotenv import load_dotenv
import os

load_dotenv()

LLM_API = {
    "api_url": os.getenv("LLM_API_URL"),
    "api_key": os.getenv("LLM_API_KEY"),
    "model": os.getenv("LLM_MODEL"),
}