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

