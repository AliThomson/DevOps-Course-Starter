import os


class Config:
    def __init__(self):
        """Base configuration variables."""
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        self.LOGGLY_TOKEN = os.environ.get('LOGGLY_TOKEN')
