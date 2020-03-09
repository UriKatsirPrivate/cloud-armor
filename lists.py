# [
# (lengtha,[ipi,..,ipk],[desci,..,desck],priority,preview,allow/deny),
# (lengthb,[ipl,..,ipm],[descl,..,descm],priority,preview,allow/deny)
# ]

# [([1, 2, 3], 1), ([2, 3, 4], 2), ([3, 4, 5], 3)]
import json

from jsonpath_ng import jsonpath, parse

listoflists = []
allow_preview_list = []
allow_no_preview_list = []
deny_preview_list = []
deny_no_preview_list = []

with open('/Users/ukatsir/projects/cloud-armor/supporting_files/one_policy.json') as f:
    json_data = json.load(f)

# rules = json.dumps(json_data).find('rules')

jsonpath_expression = parse('$.rules[*]')
match = jsonpath_expression.find(json_data)
# rules= match[0].value

for rule in match:
    # print (rule.value)
    # print (rule.value['action'])
    # print (rule.value['preview'])
    action = str((rule.value['action']))
    preview = str((rule.value['preview']))

    if action == 'allow' and preview == 'True':
        allow_preview_list.append(rule)
    elif action == 'allow' and preview == 'False':
        allow_no_preview_list.append(rule)
    elif 'deny' in action and preview == 'True':
        deny_preview_list.append(rule)
    elif 'deny' in action and preview == 'False':
        deny_no_preview_list.append(rule)

# print allow_preview_list
# print allow_no_preview_list
# print deny_no_preview_list
# print allow_no_preview_list

for rule1 in deny_no_preview_list:
    print(rule1.value)





stop_here=''