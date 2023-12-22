from app.config.amqp import AMQPProvider
from app.models.notification import Notification

def send(notification:Notification):
    provider = AMQPProvider(
            exchange='exchange.taco.api.notification',
            queue='queue.taco.api.notification')
    try:
        message = notification.to_json()
        print(f"{message}")
        provider.publish(message)
    except:
        print(">>> ERRO durante envio de mensagem ao RabbitMQ")
    finally:
        provider.channel.close()        