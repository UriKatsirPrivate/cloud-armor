import json

from jsonpath_ng import jsonpath, parse

MAX_NUMBER_IPS_PER_RULE = 5


def create_lists(one_policy):

    allow_preview_list = []
    allow_no_preview_list = []
    deny_preview_list = []
    deny_no_preview_list = []

    # with open('/Users/ukatsir/projects/cloud-armor/supporting_files/one_policy_scattered_odd.json') as f:
    # with open('/Users/ukatsir/projects/cloud-armor/supporting_files/one_policy_scattered_even.json') as f:
    # with open('/Users/ukatsir/projects/cloud-armor/supporting_files/one_ip_even.json') as f:
    # with open('/Users/ukatsir/projects/cloud-armor/supporting_files/one_ip_odd.json') as f:
    # json_data = json.load(f)
    json_data = json.loads(one_policy)

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
            allow_no_preview_list[(current_rule_index-1)
                                  ]['processed'] = 'false'
            allow_no_preview_list[(current_rule_index-1)]['discard'] = 'false'
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

    # stop_here = ''
    return (allow_no_preview_list)
    # combine_rules(allow_no_preview_list)


def combine_rules(input_list):
    # json_list = json.dumps(input_list)
    # print (json_list)
    patch_allow_preview_list = []
    discard_allow_preview_list = []
    i = 0
    while i < len(input_list):
        discard = input_list[i]['discard']
        processed_i = input_list[i]['processed']
        number_of_ips_i = input_list[i]['number_of_ips']
        rule_priority_i = input_list[i]['priority']

        if processed_i == 'false':  # skip processed and discarded rules
            # find match
            j = i
            # run on the rest of the list starting at position i
            while j < (len(input_list)-1):
                number_of_ips_j = input_list[j+1]['number_of_ips']
                rule_priority_j = input_list[j+1]['priority']
                processed_j = input_list[j+1]['processed']
                # Found a match of an unprocessed rule
                if ((number_of_ips_j <= (MAX_NUMBER_IPS_PER_RULE-number_of_ips_i)) and processed_j == 'false'):
                    patch_allow_preview_list.append(
                        [rule_priority_i, rule_priority_j])
                    # add the higher rule number to the discard list
                    if rule_priority_i > rule_priority_j:
                        discard_allow_preview_list.append(rule_priority_i)
                    else:
                        discard_allow_preview_list.append(rule_priority_j)

                    # update both rules as processed
                    input_list[i]['processed'] = 'true'
                    input_list[j+1]['processed'] = 'true'
                    break
                j = j+1

        # update processed value to true
        input_list[i]['processed'] = 'true'

        i = i+1
    # stop_here = ''
    return patch_allow_preview_list,discard_allow_preview_list

# create_lists()
