from  flask import Flask
from views import views
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder="templates", static_folder="static")
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True,port=2001)