#init file
from flask import Flask

app = Flask(__name__)

#Specify nameof config file
app.config.from_object('config')
from app import views
