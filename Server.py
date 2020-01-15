import socket
from contextlib import closing
from threading import Thread
import R64.GPIO as GPIO
from flask import Flask
from flask_restful import Resource, Api, abort, reqparse

HOST = '0.0.0.0'

app = Flask('Sofia')
api = Api(app)

devices = []

class DeviceList(Resource):
    def get(self):
        return map(lambda dev: dev.serialize(), devices)

class Device(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('cmd')

    def get(self, dev_id):
        if not int(dev_id) in map(lambda dev: dev.id, devices):
            abort(404, message="Device {} doesn't exist".format(dev_id))
        else:
            return devices[int(dev_id)].serialize_long()

    def post(self, dev_id):
        device = devices[int(dev_id)]
        if not device:
            abort(404, message="Device {} doesn't exist".format(dev_id))

        args = self.parser.parse_args()
        return device.parse_cmd(args['cmd'])

class Server:
    def __init__(self, elements=[]):
        global devices

        devices = elements

        api.add_resource(DeviceList, '/devices')
        api.add_resource(Device, '/devices/<dev_id>')

        app.run(host=HOST, debug=False)

