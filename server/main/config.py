# project/server/config.py
import os


class BaseConfig:
    """Base configuration."""

    FLASK_APP = "main/__init__.py"
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
    DEBUG = False
    BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAAZSlQEAAAAASSH6b9w8%2FX8aJtuAGblTr4CK1bw%3DKSRLRpEDCSiMkGOkAP5xYMho9z7H5Vtd8yOvgIUGHWLbh3FZtR"


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True
    FLASK_ENV = "development"


class TestingConfig(BaseConfig):
    """Testing configuration."""

    DEBUG = True
    FLASK_ENV = "testing"


class ProductionConfig(BaseConfig):
    """Production configuration."""

    DEBUG = False
    FLASK_ENV = "production"
