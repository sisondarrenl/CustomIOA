import os
from falconpy import CustomIOA

CLIENT_ID = "input"
CLIENT_SECRET = "input"

# Do not hardcode API credentials!
falcon = CustomIOA(client_id=CLIENT_ID,
                   client_secret=CLIENT_SECRET
                   )

id_list = '13'  # Can also pass a list here: ['ID1', 'ID2', 'ID3']

response = falcon.get_rules(ids=id_list)
print(response)