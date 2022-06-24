import http.client
import json
import os


class StaticEntryPusher(object):

    def __init__(self, server):
        self.server = server

    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])

    def Set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200

    def remove(self, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200

    def rest_call(self, data, action):
        path = '/wm/staticentrypusher/json'
        header = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }

        body = json.dumps(data)
        Conn = http.client.HTTPConnection(self.server, 8080)
        Conn.request(action, path, body, header)
        response = Conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print(ret)
        Conn.close()
        return ret


pusher = StaticEntryPusher('127.0.0.1')
file_path = os.getcwd() + "/flows.json"
f = open(file_path)
data = json.load(f)
for i in data:
    pusher.Set(data[i])
f.close()
