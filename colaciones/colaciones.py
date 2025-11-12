from flask import Blueprint

bp = Blueprint("colaciones", __name__, url_prefix="/colaciones")


@bp.route("/selector")
def selector():
    return "Selecciona tu colacion: "