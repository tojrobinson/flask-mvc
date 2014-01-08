from flask import Blueprint, request, render_template, abort

main = Blueprint('main', __name__, template_folder='views')

@main.route('/')
def index():
   return render_template("index.html")
