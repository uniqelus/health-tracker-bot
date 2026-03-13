import os
from dotenv import load_dotenv

load_dotenv()

HTTP_LISTEN_HOST = os.environ.get("HTTP_LISTEN_HOST", "0.0.0.0")
HTTP_LISTEN_PORT = os.environ.get("HTTP_LISTEN_PORT", "3000")
