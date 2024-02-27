# pylint: disable=too-few-public-methods
from datetime import date
from typing import Optional
from dataclasses import dataclass


class Command:
    pass

@dataclass
class CrearPropiedad(Command):
    id: str
    ubicacion: str
    valorMercado: int
    estadoActual: str
    tipo: str