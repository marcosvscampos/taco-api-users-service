import pika
from app.config.environment.amqp_env_config import AMQPEnvConfig

class AMQPProvider:

    __exchange_name:str = None
    __queue_name:str = None

    def __init__(self, exchange:str, queue:str, type:str = 'fanout'):
        config = AMQPEnvConfig()
        url: str = f'amqps://{config.username}:{config.password}@{config.host}/{config.vhost}'
        parameters = pika.URLParameters(url)
        connection = pika.BlockingConnection(parameters)
        self.__channel = connection.channel()
        self.__init_exchange(exchange, type)
        self.__init_queue(queue)
        self.__init_binding()

    def __init_exchange(self, name:str, type:str):
        self.__exchange_name = name
        self.__channel.exchange_declare(exchange=name, exchange_type=type)

    def __init_queue(self, name:str):
        self.__queue_name = name
        self.__channel.queue_declare(queue=name)
    
    def __init_binding(self):
        self.__channel.queue_bind(exchange=self.__exchange_name, queue=self.__queue_name)

    def publish(self, message:str):
        self.__channel.basic_publish(exchange=self.__exchange_name, routing_key='', body=message)

    @property
    def channel(self):
        return self.__channel