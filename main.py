# import count_rules
import security_policies
import manage_rules

PROJECT_NAME = 'uri-test'
POLICY_NAME = 'armor-policy1'


def main():

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

    fff = ''

    # rules_work = security_policies.patch_one_rule(
    #     PROJECT_NAME, POLICY_NAME, 55)

    # all_policies = security_policies.get_all_policies(PROJECT_NAME)

    # rules_count = count_rules.count_policy_rules(
    #     '/Users/ukatsir/projects/cloud-armor/supporting_files/all_policies.json')

    # rules_count = count_rules.count_policy_rules(all_policies)


# Main function calling
if __name__ == "__main__":
    main()