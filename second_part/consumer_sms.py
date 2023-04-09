import pika

from database import connect
from database.models import User

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials))
channel = connection.channel()

users = User.objects()

channel.queue_declare(queue="sms_queue")


def callback(ch, method, properties, body):
    uuid = body.decode()
    user = User.objects(id=uuid)
    user.update(delivered=True)
    print(f"{body}")


channel.basic_consume(queue="sms_queue", on_message_callback=callback, auto_ack=True)
print("[*] Waiting for message")
channel.start_consuming()
