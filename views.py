from flask import Blueprint,render_template

views = Blueprint(__name__,"views")

#configuring routes for web app
@views.route("/")
def home():
    return render_template("index.html")
@views.route("/products")
def products():
    return render_template("products.html")
@views.route("/canonae1program")
def canonae1progam():
    return render_template("canonae1program.html")
@views.route("/contaxt2")
def contaxt2():
    return render_template("contaxt2.html")
@views.route("/xpan")
def xpan():
    return render_template("xpan.html")
@views.route("/mamiya7")
def mamiya7():
    return render_template("mamiya7.html")
@views.route("/pentax6x7")
def pentax6x7():
    return render_template("pentax6x7.html")
@views.route("/ilfordhp5")
def ilfordhp5():
    return render_template("ilfordhp5.html")
@views.route("/ilfordxp2")
def ilfordxp2():
    return render_template("ilfordxp2.html")
@views.route("/vision350d")
def vision350d():
    return render_template("kodak50d.html")
@views.route("/vision3250d")
def vision3250d():
    return render_template("kodak250d.html")
@views.route("/vision3200t")
def vision3200t():
    return render_template("kodak200t.html")
@views.route("/vision3500t")
def vision3500t():
    return render_template("kodak500t.html")
@views.route("/kodakgold200")
def kodakgold200():
    return render_template("kodakgold200.html")
@views.route("/darkroom")
def darkroom():
    return render_template("darkroom.html")
@views.route("/contact")
def contact():
    return render_template("contact.html")
@views.route("/signup")
def register():
    return render_template("signup.html")
@views.route("/login", methods=["POST","GET"])
def login():
    return render_template("login.html")




