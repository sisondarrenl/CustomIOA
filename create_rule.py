from falconpy import CustomIOA
import json
import os

CLIENT_ID = "input"
CLIENT_SECRET = "input"

# Do not hardcode API credentials!
falcon = CustomIOA(client_id=CLIENT_ID,
                   client_secret=CLIENT_SECRET
                   )

script_path = os.path.dirname(os.path.abspath(__file__))
json_filename = 'rule_data.json'
json_file_path = os.path.join(script_path, json_filename)

with open(json_file_path, 'r') as file:
    json_data = json.load(file)


create = falcon.create_rule(
      comment = json_data['comment'],
      description = json_data['description'],
      disposition_id = json_data['disposition_id'],
      field_values=json_data['field_values'],
      pattern_severity = json_data['pattern_severity'],
      name = json_data['name'],
      rulegroup_id = json_data['rulegroup_id'],
      ruletype_id = json_data['ruletype_id']
)

print (create)