import os
from .factory import FlaskFactory
from .views import obx
from .models import db


def get_aws_keys():
    import hvac
    client = hvac.Client(
                url=os.environ['VAULT_ADDR'],
                token=os.environ['VAULT_TOKEN'],
                )
    creds = client.read('aws/creds/{}'.format(os.environ['VAULT_ROLE']))
    return {k: v for k, v in creds['data'] if 'key' in k}


def get_app():
    factory = FlaskFactory()
    
    blueprint_dicts = [
            dict(
                bp=obx,
            )
        ]
    
    app = factory.initiallize_flask(db, blueprint_dicts)
    app.config.update(get_aws_keys())
    return app
