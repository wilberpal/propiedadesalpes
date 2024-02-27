from datetime import datetime
from fastapi import FastAPI, Request
from alpesproperties.domain import commands
from alpesproperties.service_layer.handlers import InvalidSku
from alpesproperties import bootstrap, views

app = FastAPI()
bus = bootstrap.bootstrap()


@app.post("/propiedad")
def addProperty_endpoint(request: Request):
    try:
        cmd = commands.CrearPropiedad(
            request.json["orderid"], request.json["sku"], request.json["qty"]
        )
        bus.handle(cmd)
    except InvalidSku as e:
        return {"message": str(e)}, 400

    return "OK", 202


@app.get("/propiedad/{propertyid}")
def property_endpoint(propertyid: int):
    result = views.properties(propertyid, bus.uow)
    if not result:
        return "not found", 404
    return result, 200

