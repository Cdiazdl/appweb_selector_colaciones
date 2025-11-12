from flask import Blueprint, render_template
from . import models

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/inicio")
def inicio():
    return render_template("auth/login.html", methods = "POST")

@bp.route("/administrador")
def admin():
    return render_template("auth/administrador.html")

@bp.route("/revisar")
def revisar():
    return render_template("auth/revisar.html")

@bp.route("/registrar")
def registrar():
    return render_template("auth/registrar.html")