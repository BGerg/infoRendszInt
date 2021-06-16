#!/usr/bin/env python
import pika
import sys


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    color_statistics_channel = connection.channel()
    color_statistics_channel.queue_declare(queue='/queue/colorStatistics')




    def callback(ch, method, properties, body):
        print(f"10 '{body}' messages has been processed")


    color_statistics_channel.basic_consume(
        queue='/queue/colorStatistics',
        on_message_callback=callback,
        auto_ack=True
    )
    print(' [*] Waiting for messages. To exit press CTRL+C')
    color_statistics_channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            sys.exit(0)

