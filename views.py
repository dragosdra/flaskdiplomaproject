from flask import Blueprint,render_template, request

views = Blueprint(__name__,"views")

#configuring routes for web app
@views.route("/register")
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
@views.route('/register' ,methods=['GET','POST'])
def register():
    if request.method == 'POST':
        #handle request
        pass
    return render_template(register.html)
@views.route('/login' ,methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #handle request
        pass
    return render_template(login.html)