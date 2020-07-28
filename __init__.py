import os
from bluelog.settings import config
from flask import Flask

app = Flask('bluelog')
config_name = os.getenv('FLASK_CONFIG', 'development')
app.config.from_object(config[config_name])
