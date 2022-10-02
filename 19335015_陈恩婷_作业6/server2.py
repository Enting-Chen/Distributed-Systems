import xmlrpc.server as server

class data_on_server:
    def __init__(self):
        self.__data = 0

    def set_data(self, new_data):
        self.__data = new_data

    def get_data(self):
        return self.__data

server = server.SimpleXMLRPCServer(("localhost", 8089), allow_none=True)
# 将实例注册给rpc server
server.register_instance(data_on_server())

print("Listening on port 8089")
server.serve_forever()
