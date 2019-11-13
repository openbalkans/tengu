import json
import socket
from flask import Blueprint, request
from .config import get_cloudwatch_logger


cloudwatch_logger = get_cloudwatch_logger()

obx = Blueprint('obx', __name__)


@obx.route('/')
def root_view():
    cloudwatch_logger.log(MetricName='ViewCount', value='1', Unit='Count')
    return 'Hello World ' + socket.gethostname()
