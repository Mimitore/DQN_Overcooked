class GameObject:
    def __init__(self, type_id):
        self.type_id = type_id

    def getState(self):
        return [self.type_id]