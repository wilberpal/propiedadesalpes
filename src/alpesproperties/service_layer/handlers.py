# pylint: disable=unused-argument
from __future__ import annotations
from dataclasses import asdict
from typing import List, Dict, Callable, Type, TYPE_CHECKING
from alpesproperties.domain import commands, events, model
from alpesproperties.domain.model import OrderLine

if TYPE_CHECKING:
    from alpesproperties.adapters import notifications
    from . import unit_of_work


# TODO