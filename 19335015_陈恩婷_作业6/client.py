import xmlrpc.client as client

class Client:
    def __init__(self):
        self.server1 = client.ServerProxy('http://localhost:8088')
        self.server2 = client.ServerProxy('http://localhost:8089')
    
    def get_data(self):
        # wait for server for 2 seconds, if get_data does not return in 2 seconds, return Error
        data1 = self.server1.get_data()
        data2 = self.server2.get_data()
        if data1 == data2:
            return data1
        else:
            return "Error, data not the same"        
    
    def set_data(self, data):
        self.server1.set_data(data)
        self.server2.set_data(data)

client = Client()
print("Client:", client.get_data())
data = input("input the number you'd like to save on server: ")
client.set_data(int(data))
print("Client:", client.get_data())