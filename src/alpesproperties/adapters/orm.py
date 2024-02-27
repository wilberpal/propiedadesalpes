import logging
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
from sqlalchemy.orm import mapper, relationship

from allocation.domain import model

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


def start_mappers():
    logger.info("Starting mappers")
    lines_mapper = mapper(model.OrderLine, order_lines)
    batches_mapper = mapper(
        model.Batch,
        batches,
        properties={
            "_properties": relationship(
                lines_mapper,
                secondary=allocations,
                collection_class=set,
            )
        },
    )
    mapper(
        model.Product,
        products,
        properties={"batches": relationship(batches_mapper)},
    )


@event.listens_for(model.Product, "load")
def receive_load(product, _):
    product.events = []
