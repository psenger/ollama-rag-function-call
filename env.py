import os
from dotenv import load_dotenv

load_dotenv()

env_vars = {
    "API_URL": None,
    "AI_MODEL": None
}

missing_vars = []

for var in env_vars.keys():
    env_vars[var] = os.getenv(var)
    if env_vars[var] is None:
        missing_vars.append(var)

if missing_vars:
    raise ValueError("The following environment variables are not set: " + ", ".join(missing_vars))

API_URL = os.getenv("API_URL", None)
AI_MODEL = os.getenv("AI_MODEL", None)