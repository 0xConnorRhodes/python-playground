# This is a bit harder, but worth trying a bit: The pickle module lets you turn data structures into bytestrings, and back. 
# That’s normally used for storing data on disk and then retrieving it later. 
# You take a data structure and turn it into a bytestring with pickle.dumps, which returns a bytestring. You can then take a bytestring and turn it back into data with pickle.loads. 
#Create a dict in which the keys are strings and the values are ints, strings, and lists (not too many). Use pickle.dumps to turn it into a bytestring. Then turn it back into a data structure… are they the same?

import pickle

data = {
        'key1': 1,
        'key2': 'value2',
        'key3': [1, 2, 'three']
       }

print(data)

bytestring = pickle.dumps(data)
print(bytestring)

converted = pickle.loads(bytestring)
print(converted)

