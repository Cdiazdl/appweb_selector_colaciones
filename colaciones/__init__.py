from __future__ import annotations

import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app() -> Flask:
    """Application factory used by the development server."""

    app = Flask(__name__, instance_relative_config=True)

    database_path = os.path.join(app.instance_path, "selector_colaciones.db")

    # Ensure the instance folder exists so SQLite can create the database file.
    os.makedirs(app.instance_path, exist_ok=True)

    # Application configuration
    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY="contrasena",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{database_path}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)

    # Blueprints keep the views organised by responsibility.
    from .colaciones import bp as colaciones_bp
    from .auth import bp as auth_bp

    app.register_blueprint(colaciones_bp)
    app.register_blueprint(auth_bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    with app.app_context():
        db.create_all()

        from .models import Colaciones

        if not Colaciones.query.first():
            sample_menu = [
                Colaciones(
                    dia="Lunes",
                    fruta="Manzana",
                    postre="Yogur natural",
                    opcion1="Pechuga de pollo con arroz integral",
                    opcion2="Pasta con salsa de tomate",
                    hipocalorico="Ensalada de atún",
                    ensalada="Ensalada verde",
                    sopa="Crema de zapallo",
                ),
                Colaciones(
                    dia="Martes",
                    fruta="Plátano",
                    postre="Gelatina de frutas",
                    opcion1="Tortilla de verduras",
                    opcion2="Carne al jugo con puré",
                    hipocalorico="Pavo con ensalada",
                    ensalada="Ensalada de porotos",
                    sopa="Sopa de verduras",
                ),
                Colaciones(
                    dia="Miércoles",
                    fruta="Pera",
                    postre="Mousse de chocolate",
                    opcion1="Lasaña de espinaca",
                    opcion2="Pescado al horno con papas",
                    hipocalorico="Tazón de quinoa",
                    ensalada="Ensalada de garbanzos",
                    sopa="Caldo de pollo",
                ),
                Colaciones(
                    dia="Jueves",
                    fruta="Naranja",
                    postre="Flan casero",
                    opcion1="Pollo al curry",
                    opcion2="Guiso de lentejas",
                    hipocalorico="Budín de verduras",
                    ensalada="Ensalada César",
                    sopa="Sopa de tomate",
                ),
                Colaciones(
                    dia="Viernes",
                    fruta="Manzana verde",
                    postre="Tarta de frutas",
                    opcion1="Filete de merluza con ensalada",
                    opcion2="Pizza vegetal",
                    hipocalorico="Wrap de pollo",
                    ensalada="Ensalada griega",
                    sopa="Sopa minestrone",
                ),
            ]

            db.session.add_all(sample_menu)
            db.session.commit()

    return app
