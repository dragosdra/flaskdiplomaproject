from flask import Blueprint,render_template

views = Blueprint(__name__,"views")


@views.route("/")
def home():
    return render_template("index.html")
@views.route("/products")
def products():
    return render_template("products.html")
@views.route("/darkroom")
def darkroom():
    return render_template("darkroom.html")
