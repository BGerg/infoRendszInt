import pika
import sys

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    color_channel = connection.channel()
    color_channel.queue_declare(queue='/queue/colorQueue')
    color_statistics_channel = connection.channel()
    color_statistics_channel.queue_declare(queue='/queue/colorStatistics')
    messages = {
        b"RED": 0,
        b"BLUE": 0,
        b"GREEN": 0
    }
    def callback(ch, method, properties, body):
        messages[body] += 1
        print(f'Statistics: - RED: {messages[b"RED"]} '
              f'- BLUE: {messages[b"BLUE"]} '
              f'- GREEN: {messages[b"GREEN"]} ', end = '\r')
        cb = lambda x: color_statistics_channel.basic_publish(
            exchange='',
            routing_key='/queue/colorStatistics',
            body=x
        )
        if messages[b"RED"] == 10:
            cb("RED")
            messages[b"RED"] = 0
        elif messages[b"BLUE"] == 10:
            cb("BLUE")
            messages[b"BLUE"] = 0
        elif messages[b"GREEN"] == 10:
            cb("GREEN")
            messages[b"GREEN"] = 0

    color_channel.basic_consume(
        queue='/queue/colorQueue',
        on_message_callback=callback,
        auto_ack=True
    )
    print(' [*] Waiting for messages. To exit press CTRL+C')
    color_channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            sys.exit(0)