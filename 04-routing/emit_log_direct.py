import pika
import sys

conn = pika.BlockingConnection(pika.URLParameters('amqp://guest:guest@localhost:25672/%2F'))
channel = conn.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(
    exchange='direct_logs', routing_key=severity, body=message
)
print(f" [*] Sent {severity}:{message}")
conn.close()