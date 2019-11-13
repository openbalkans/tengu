# -*- coding: utf-8 -*-

import os

from .app import get_app
import boto3


"""Top-level package for Tengu."""

__author__ = """Barak Avrahami"""
__email__ = 'barak1345@gmail.com'
__version__ = '0.1.10'

app = get_app()

def page_view_log_count():
    client = boto3.client(
            'cloudwatch',
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
            aws_region=os.environ['AWS_REGION'],
            )

    response = client.put_metric_data(
        Namespace='Application',
        MetricData=[
            {
                'MetricName': 'ViewCount',
                'Value': 1.0,
                'Unit': 'Count',
            },
        ]
    )

    return response
