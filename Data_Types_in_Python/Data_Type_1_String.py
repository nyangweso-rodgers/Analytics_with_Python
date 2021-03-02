# String
## Generating unique string using UUID
'''
UUID, Universal Unique Identifier, is a python library which helps in generating random objects of 128 bits as ids. 
It provides the uniqueness as it generates ids on the basis of time, Computer hardware (MAC etc.).

## Advantages of UUID :
* Can be used as general utility to generate unique random id.
* Can be used in cryptography and hashing applications.
* Useful in generating random documents, addresses etc.


'''
import uuid
# print(dir(uuid))

print ("The random id using uuid1() is :", uuid.uuid1()) 
#print (uuid.uuid1())

print(str(uuid.uuid4())) # 67da5ae4-1af9-4aa4-8552-4fa63fabc97c
print(type(uuid.uuid4())) # <class 'uuid.UUID'>