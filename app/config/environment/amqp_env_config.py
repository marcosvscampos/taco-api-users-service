import os
from app.config.environment.env_config import EnvConfig

class AMQPEnvConfig(EnvConfig):

    def __init__(self):
        self.vhost = os.environ.get("AMQP_VHOST")
        super().__init__(
            host=os.environ.get("AMQP_HOST"),
            username=os.environ.get("AMQP_USERNAME"),
            password=os.environ.get("AMQP_PASSWORD")
        )