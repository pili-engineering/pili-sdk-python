class APIError(RuntimeError):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return "%s" % (self.message)
    def __repr__(self):
        return self.__str__()

