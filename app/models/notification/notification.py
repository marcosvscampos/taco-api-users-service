import json

class Notification:

    def __init__(self, to:str, type:str, content):
        self.to = to
        self.type = type
        self.content = content

    def to_json(self):
        dict = {
            'type': self.type,
            'content': vars(self.content)
        }
        return json.dumps(dict)    