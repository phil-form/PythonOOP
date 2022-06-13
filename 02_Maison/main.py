from audioop import add
from Models.Address import Address
from Models.Home import Home

address = Address("test", 13, "test", 123)
print(address.__dict__)
home = Home(address, 15, 5, 2)
print(address)