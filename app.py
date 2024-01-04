from  flask import Flask, request
from views import views
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__,template_folder="templates", static_folder="static")
app.register_blueprint(views, url_prefix="/")



if __name__ == '__main__':
    app.run(debug=True,port=5000)