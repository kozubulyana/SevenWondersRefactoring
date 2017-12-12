from flask import Flask, Blueprint, render_template, json, request
import json
import pika
import uuid
import threading
from time import sleep
from flask import Flask
from flask import jsonify

class RpcClient(object):
    """Asynchronous Rpc client."""
    internal_lock = threading.Lock()
    queue = {}

    def __init__(self, rpc_queue):
        """Set up the basic connection, and start a new thread for processing.
            1) Setup the pika connection, channel and queue.
            2) Start a new daemon thread.
        """
        self.rpc_queue = rpc_queue
        self.connection = pika.BlockingConnection()
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        thread = threading.Thread(target=self._process_data_events)
        thread.setDaemon(True)
        thread.start()

    def _process_data_events(self):
        """Check for incoming data events.
        We do this on a thread to allow the flask instance to send
        asynchronous requests.
        It is important that we lock the thread each time we check for events.
        """
        self.channel.basic_consume(self._on_response, no_ack=True,
                                   queue=self.callback_queue)
        while True:
            with self.internal_lock:
                self.connection.process_data_events()
                sleep(0.1)

    def _on_response(self, ch, method, props, body):
        """On response we simply store the result in a local dictionary."""
        self.queue[props.correlation_id] = body

    def send_request(self, payload):
        """Send an asynchronous Rpc request.
        The main difference from the rpc example available on rabbitmq.com
        is that we do not wait for the response here. Instead we let the
        function calling this request handle that.
            corr_id = rpc_client.send_request(payload)
            while rpc_client.queue[corr_id] is None:
                sleep(0.1)
            return rpc_client.queue[corr_id]
        If this is a web application it is usually best to implement a
        timeout. To make sure that the client wont be stuck trying
        to load the call indefinitely.
        We return the correlation id that the client then use to look for
        responses.
        """
        corr_id = str(uuid.uuid4())
        self.queue[corr_id] = None
        with self.internal_lock:
            self.channel.basic_publish(exchange='',
                                       routing_key=self.rpc_queue,
                                       properties=pika.BasicProperties(
                                           reply_to=self.callback_queue,
                                           correlation_id=corr_id,
                                       ),
                                       body='hello')
        return corr_id

    def get_data(self, requestName):
        corrid = rpcClientOut.send_request(requestName)
        while rpcClientOut.queue[corrid] is None:
            sleep(0.1)
        data = rpcClientOut.queue[corrid].decode('utf-8')
        newdata = json.loads(data)
        result = jsonify(newdata)
        return result

rpcClientOut = RpcClient('rpc_queue') 