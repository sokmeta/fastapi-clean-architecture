import os


APP_VERSION = os.getenv('APP_VERSION')
SCRET_KEY = os.getenv('SCRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
PREFIX = f"/{APP_VERSION}/api"
