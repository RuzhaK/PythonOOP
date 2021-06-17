# class HDMICapable:
#     pass
# class PowerSocketCapable:
#     pass
# class EthernetCapable:
#     pass
#
# class Televison(HDMICapable,PowerSocketCapable<EthernetCapable):
#     pass
# 2ри вариант с композиция:
class Connector:
    def connect(self,other):
        pass
class HDMIConnector(Connector):
    pass
class PowerSocketConnector(Connector):
    pass
class EthernetConnector(Connector):
    pass

class Televison:
    def __init__(self):
        self.hdmi_connector=HDMIConnector()
        self.power_connector=PowerSocketConnector()
        self.ethernet_connector=EthernetConnector()

class GameConsole:
    def __init__(self):
        self.hdmi_connector=HDMIConnector()
        self.power_connector=PowerSocketConnector()
        self.ethernet_connector=EthernetConnector()

class Router:
    def __init__(self):

        self.power_connector=PowerSocketConnector()
        self.ethernet_connector=EthernetConnector()

tv=Televison()
game_console=GameConsole()
tv.hdmi_connector.connect(game_console.hdmi_connector)