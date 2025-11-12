"""Database models used by the application."""

from __future__ import annotations

from colaciones import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    rut = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, username: str, rut: str) -> None:
        self.username = username
        self.rut = rut

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"<User {self.username}>"


class Colaciones(db.Model):
    """Weekly menu options available for selection."""

    id = db.Column(db.Integer, primary_key=True)
    dia = db.Column(db.String(100), nullable=False)
    fruta = db.Column(db.Text, nullable=True)
    postre = db.Column(db.Text, nullable=True)
    opcion1 = db.Column(db.Text, nullable=True)
    opcion2 = db.Column(db.Text, nullable=True)
    hipocalorico = db.Column(db.Text, nullable=True)
    ensalada = db.Column(db.Text, nullable=True)
    sopa = db.Column(db.Text, nullable=True)
    state = db.Column(db.Boolean, default=False)

    def __init__(
        self,
        dia: str,
        fruta: str | None = None,
        postre: str | None = None,
        opcion1: str | None = None,
        opcion2: str | None = None,
        hipocalorico: str | None = None,
        ensalada: str | None = None,
        sopa: str | None = None,
        state: bool = False,
    ) -> None:
        self.dia = dia
        self.fruta = fruta
        self.postre = postre
        self.opcion1 = opcion1
        self.opcion2 = opcion2
        self.hipocalorico = hipocalorico
        self.ensalada = ensalada
        self.sopa = sopa
        self.state = state

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"<Colaciones {self.dia}>"
