from __future__ import annotations

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from .models import Colaciones

bp = Blueprint("colaciones", __name__, url_prefix="/colaciones")


@bp.route("/selector", methods=["GET", "POST"])
def selector():
    menu = Colaciones.query.order_by(Colaciones.id).all()

    if request.method == "POST":
        dia = request.form.get("dia")
        opcion = request.form.get("opcion")

        if dia and opcion:
            selections = session.get("selections", {})
            selections[dia] = opcion
            session["selections"] = selections
            flash(f"Guardaste tu elección para {dia}.", "success")
        else:
            flash("Selecciona una opción válida antes de guardar.", "danger")

        return redirect(url_for("colaciones.selector"))

    selections = session.get("selections", {})
    return render_template("colaciones/selector.html", menu=menu, selections=selections)
