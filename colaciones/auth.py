from __future__ import annotations

from flask import Blueprint, redirect, render_template, request, session, url_for

from .models import Colaciones

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/inicio", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        if username:
            session["username"] = username
            return redirect(url_for("colaciones.selector"))

    return render_template("auth/login.html")


@bp.route("/administrador")
def admin():
    return render_template("auth/administrador.html")


@bp.route("/revisar")
def revisar():
    selections = session.get("selections", {})
    menu = {item.dia: item for item in Colaciones.query.order_by(Colaciones.id).all()}
    return render_template("auth/revisar.html", selections=selections, menu=menu)


@bp.route("/registrar")
def registrar():
    return render_template("auth/registrar.html")
