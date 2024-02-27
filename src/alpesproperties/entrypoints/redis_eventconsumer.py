import redis
import json
import logging


from alpesproperties import bootstrap, config
from alpesproperties.domain import commands

logger = logging.getLogger(__name__)

r = redis.Redis(**config.get_redis_host_and_port())


def main():
    logger.info("Redis pubsub starting")
    bus = bootstrap.bootstrap()
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe("crear_propiedad")

    for m in pubsub.listen():
        handle_crear_propiedad(m, bus)


def handle_crear_propiedad(m, bus):
    logger.info("handling %s", m)
    data = json.loads(m["data"])
    cmd = commands.CrearPropiedad()
    bus.handle(cmd)


if __name__ == "__main__":
    main()
