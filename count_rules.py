import json

from jsonpath_ng import jsonpath, parse


with open('/Users/ukatsir/projects/cloud-armor/all_policies.json') as f:
    json_data = json.load(f)

try:
    rules = json.dumps(json_data).find('rules')

    if rules > -1:
        jsonpath_expression = parse('$.items[*].rules')
        matchs = jsonpath_expression.find(json_data)

        total_rule_count = 0
        i = 0

        while i < len(matchs):
            all_rules = matchs[i].value
            total_rule_count += len(all_rules)
            i += 1

        # for i=0;i< len(matchs);i++:
        #     all_rules = match[i].value
        #     rules_count = len(all_rules)
        sss = ''


except IndexError:
    print("Oops!  That was no valid value.  Try again...")
cc = ""
