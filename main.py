# import count_rules
import os
import security_policies
import manage_rules
import json

# Local Testing
# PROJECT_NAME = 'uri-test'
# POLICY_NAME = 'armor-policy2'
# ----------------------------

# using Environment Variables
PROJECT_NAME = os.environ.get('project_name')
POLICY_NAME = os.environ.get('policy_name')
# ----------------------------------------------

# def combine_security_rules(): # use this definition when running locally


# use this definition when deploying to GCP
def combine_security_rules(request):

    list_patched_and_discarded_rules = []

    # Get the policy we want to modify
    one_policy = security_policies.get_one_policy(
        PROJECT_NAME, POLICY_NAME)

    # Get the list of rules that are 'Allow' and 'No Preview'
    allow_no_preview_list = manage_rules.create_lists(one_policy)

    # Create a list od rules to combine and rules to discard
    rules = manage_rules.combine_rules(allow_no_preview_list)

    rules_to_patch = rules[0]
    for rule in rules_to_patch:
        rule.sort()
    rules_to_discard = rules[1]

    # Patch rules
    patch_rules_result = manage_rules.patch_rules(
        rules_to_patch, PROJECT_NAME, POLICY_NAME)

    # Discard rules
    manage_rules.discard_rules(rules_to_discard, PROJECT_NAME, POLICY_NAME)

    # fff = ''
    list_patched_and_discarded_rules.append(rules_to_patch)
    list_patched_and_discarded_rules.append(rules_to_discard)
    return json.dumps(list_patched_and_discarded_rules)

    # rules_work = security_policies.patch_one_rule(
    #     PROJECT_NAME, POLICY_NAME, 55)

    # all_policies = security_policies.get_all_policies(PROJECT_NAME)

    # rules_count = count_rules.count_policy_rules(
    #     '/Users/ukatsir/projects/cloud-armor/supporting_files/all_policies.json')

    # rules_count = count_rules.count_policy_rules(all_policies)


# Main function calling
if __name__ == "__main__":
    combine_security_rules()
