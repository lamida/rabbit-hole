import pika
import sys

conn = pika.BlockingConnection(pika.URLParameters('amqp://guest:guest@localhost:25672/%2F'))
channel = conn.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(f" [x] Sent {message}")