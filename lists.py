# [
# (lengtha,[ipi,..,ipk],[desci,..,desck],priority,preview,allow/deny),
# (lengthb,[ipl,..,ipm],[descl,..,descm],priority,preview,allow/deny)
# ]

# [([1, 2, 3], 1), ([2, 3, 4], 2), ([3, 4, 5], 3)]
import json
import operator

from jsonpath_ng import jsonpath, parse


def create_lists():

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
        number_of_ips = len(rule.value['match']['config']['srcIpRanges'])

        if action == 'allow' and preview == 'True':
            allow_preview_list.append(rule.value)
            current_rule_index = len(allow_preview_list)
            allow_preview_list[(current_rule_index-1)
                               ]['number_of_ips'] = number_of_ips
        elif action == 'allow' and preview == 'False':
            allow_no_preview_list.append(rule.value)
            current_rule_index = len(allow_no_preview_list)
            allow_no_preview_list[(current_rule_index-1)
                                  ]['number_of_ips'] = number_of_ips
        elif 'deny' in action and preview == 'True':
            deny_preview_list.append(rule.value)
            current_rule_index = len(deny_preview_list)
            deny_preview_list[(current_rule_index-1)
                              ]['number_of_ips'] = number_of_ips

        elif 'deny' in action and preview == 'False':
            deny_no_preview_list.append(rule.value)
            current_rule_index = len(deny_no_preview_list)
            deny_no_preview_list[(current_rule_index-1)
                                 ]['number_of_ips'] = number_of_ips

    # sorted_allow_no_preview_list = sorted(
    #     allow_no_preview_list, key='number_of_ips')

    stop_here = ''
    combine_rules(allow_no_preview_list,1)


def combine_rules(input_list,number_of_ips_to_match):
    json_list = json.dumps(input_list)
    # print (json_list)
    


create_lists()
