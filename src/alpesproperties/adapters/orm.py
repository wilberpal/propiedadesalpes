from sqlalchemy.orm import mapper, relationship
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    event,
)
import logging

from alpesproperties.domain import model

logger = logging.getLogger(__name__)

metadata = MetaData()

batches = Table(
    "batches",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("reference", String(255)),
    Column("sku", ForeignKey("products.sku")),
    Column("_purchased_quantity", Integer, nullable=False),
    Column("eta", Date, nullable=True),
)

properties = Table(
    "properties",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("ubicacion", String(255)),
    Column("valorMercado", Integer, nullable=False),
    Column("estadoActual", String(255)),
    Column("tipo", String(255)),
)


@event.listens_for(model.Product, "load")
def receive_load(product, _):
    product.events = []
