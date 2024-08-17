import json
import os

#ex1


# data = list(filter(lambda x: x, range(1, 1_000_000, 2)))
# change = list(filter(lambda x: x, range(0, 1_000_000, 3)))
# with open('data.json', 'r+') as file:
#     json.dump(data, file)
#     with open('data.json', 'w') as f:
#         json.dump(change, f)
#


#ex2

d = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
new = {}
for k, v in d.items():
    new[v] = len(v)

# print(new)


#ex3

message = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
message_2 = {}

for k, v in message.items():
    message_2[k] = list(filter(lambda x: x % 2 != 0, v))

# print(message_2)
