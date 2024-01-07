from flask import Blueprint,render_template, request

views = Blueprint(__name__,"views")

#configuring routes for web app
@views.route("/")
def home():
    return render_template("index.html")
@views.route("/products")
def products():
    return render_template("products.html")
@views.route("/darkroom")
def darkroom():
    return render_template("darkroom.html")
@views.route("/contact")
def contact():
    return render_template("contact.html")
@views.route("/signup")
def register():
    return render_template("signup.html")
@views.route("/login")
def login():
    return render_template("login.html")



