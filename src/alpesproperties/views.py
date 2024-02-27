from alpesproperties.service_layer import unit_of_work


def properties(propertyid: str, uow: unit_of_work.SqlAlchemyUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM properties WHERE propertyid = :propertyid
            """,
            dict(orderid=orderid),
        )
    return [dict(r) for r in results]
