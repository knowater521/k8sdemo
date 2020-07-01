# -*- coding: UTF-8 -*-
import math
import json
import copy
import collections
import os
import cv2
import time
import traceback
import pika

def callback(ch, method, properties, body):
    print('received a message:' + body.decode('utf-8'))

def consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare('hello')
    channel.basic_consume(on_message_callback=callback, queue='hello',auto_ack=True)

    channel.start_consuming()

if __name__ == "__main__":
    consumer()