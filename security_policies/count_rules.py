import json
from jsonpath_ng import jsonpath, parse


def count_policy_rules(source_file):

    json_data = json.loads(source_file)

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

    except IndexError:
        print("Oops!  That was no valid value.  Try again...")
    return total_rule_count
