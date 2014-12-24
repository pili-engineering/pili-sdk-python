class APIError(RuntimeError):
    def __init__(self, code, message):
        self.code = code
        self.message = message
    def __str__(self):
        return "Error %d: %s" % (self.code, self.message)
    def __repr__(self):
        return self.__str__()

