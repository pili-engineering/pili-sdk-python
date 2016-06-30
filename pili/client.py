from .hub import Hub

class Client(object):
    def __init__(self, mac):
        self.__mac__ = mac

    def hub(self, hub):
        return Hub(self.__mac__, hub)
