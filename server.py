#!/usr/bin/env python
import pika
import sys


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    color_channel = connection.channel()
    color_channel.queue_declare(queue='/queue/colorQueue')

    color_statistics_channel = connection.channel()
    color_statistics_channel.queue_declare(queue='/queue/colorStatistics')

    messages = []
    def callback(ch, method, properties, body):
        messages.append(body)
        print(
            f"""Statistics:
            - RED: {len([c for c in messages if c == b"RED"])}
            - BLUE: {len([c for c in messages if c == b"BLUE"])}
            - GREEN: {len([c for c in messages if c == b"GREEN"])}
            """
        )

        color_approval = ""
        if len([c for c in messages if c == b"RED"]) == 10:
            color_approval = "RED"
        elif len([c for c in messages if c == b"BLUE"]) == 10:
            color_approval = "BLUE"
        elif len([c for c in messages if c == b"GREEN"]) == 10:
            color_approval = "GREEN"
        if color_approval != "":
            color_statistics_channel.basic_publish(
                exchange='',
                routing_key='/queue/colorStatistics',
                body=color_approval
                )


            for item in messages:
                if (item == color_approval):
                    messages.remove(color_approval)
            print(len(messages))
        #messages.clear()


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

