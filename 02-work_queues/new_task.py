import pika
import sys

conn = pika.BlockingConnection(pika.URLParameters(
    'amqp://guest:guest@localhost:25672/%2F'))
channel = conn.channel()


channel.queue_declare(queue="task_queue", durable=True)

message = " ".join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange="",
    routing_key="task_queue",
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    )
)
print(" [x] Sent %r" % message)
conn.close()