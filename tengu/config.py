import os
from fluentmetrics import FluentMetric


class FlaskDevelopmentConfig:
    ENV_NAME = 'dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class FlaskTestingConfig:
    ENV_NAME = 'test'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

def get_config_by_env(env):

    envs = [
        FlaskTestingConfig,
        FlaskDevelopmentConfig,
        ]

    envs_dict = {e.ENV_NAME: e for e in envs}

    return envs_dict[env]

def get_cloudwatch_logger():
    return FluentMetric().with_namespace('Application/Tengu')
