# pylint: disable=too-few-public-methods
from dataclasses import dataclass


class Event:
    pass

@dataclass
class ObtenerPropiedad(Event):
    propertyid: str