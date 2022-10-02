import xmlrpc.server as server
import time 

class data_on_server:
    def __init__(self):
        self.__data = 0

    def set_data(self, new_data):
        self.__data = new_data
    
    def get_data(self):
        #time.sleep(2)
        return self.__data

server = server.SimpleXMLRPCServer(("localhost", 8088), allow_none=True)
# 将实例注册给rpc server
server.register_instance(data_on_server())

print("Listening on port 8088")
server.serve_forever()

