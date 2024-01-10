from app.config.amqp import AMQPProvider
from app.models.notification.notification import Notification

def send(notification:Notification):
    provider = AMQPProvider(
            exchange='exchange.taco.api.notification',
            queue='queue.taco.api.notification')
    try:
        message = notification.to_json()
        provider.publish(message)
    except:
        print("[notification_service#send] >>> ERRO durante envio de mensagem ao RabbitMQ")
    finally:
        provider.channel.close()        