import pika

def connect():
    params = pika.URLParameters('amqp://guest:guest@localhost:25672/%2F')
    return pika.BlockingConnection(params)

def channel(conn):
    return conn.channel()

def declare_q(ch, name):
    ch.queue_declare(queue=name)

def publish(exchange, ch, routing_key, body):
    ch.basic_publish(exchange=exchange, routing_key=routing_key, body=body)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

def consume(q, ch, cb):
    ch.basic_consume(queue=q, auto_ack=True, on_message_callback=cb)
    ch.start_consuming()


def play_consume(conn):
    ch = channel(conn)
    declare_q(ch, "hello")
    consume("hello", ch, callback)

conn = connect()
def play(conn):
    ch = channel(conn)
    declare_q(ch, "hello")

    publish("", ch, "hello", "Hello World!")
    conn.close()

play(conn)

def publish_a_alot(conn):
    for i in range(10):
        import time
        time.sleep(1)
        ch = channel(conn)
        declare_q(ch, "hello")
        publish("", ch, "hello", f"Hello World!{i}")

# conn.close()