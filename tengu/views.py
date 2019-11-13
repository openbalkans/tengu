import json
import socket
from flask import Blueprint, request
from . import page_view_log_count



obx = Blueprint('obx', __name__)


@obx.route('/')
def root_view():
    page_view_log_count()
    return 'Hello World ' + socket.gethostname()
