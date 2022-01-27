import pika
import sys

conn = pika.BlockingConnection(pika.URLParameters('amqp://guest:guest@localhost:25672/%2F'))
channel = conn.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = " ".join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)
print(f" [*] Sent {routing_key}:{message}")
conn.close()