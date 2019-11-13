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
            aws_access_key_id=app.config['access_key'],
            aws_secret_access_key=app.config['secret_key'],
            aws_region=app.config['aws_region'],
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
