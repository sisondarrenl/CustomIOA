from falconpy import CustomIOA

CLIENT_ID = "input"
CLIENT_SECRET = "input"

# Do not hardcode API credentials!
falcon = CustomIOA(client_id=CLIENT_ID,
                   client_secret=CLIENT_SECRET
                   )

id_list = '8'  # Can also pass a list here: ['ID1', 'ID2', 'ID3']
rulegroup_id = '20c7ee33459348c9b616f6393e1b01c7'
comment = ''

response = falcon.delete_rules(rule_group_id=rulegroup_id, comment=comment, ids=id_list)
print(response)