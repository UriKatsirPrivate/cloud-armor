import count_rules
import security_policies
import manage_rules

PROJECT_NAME = 'uri-test'
POLICY_NAME = 'armor-policy2'


def main():

    # rules_work = security_policies.patch_one_rule(
    #     PROJECT_NAME, POLICY_NAME, 55)

    # all_policies = security_policies.get_all_policies(PROJECT_NAME)

    # rules_count = count_rules.count_policy_rules(
    #     '/Users/ukatsir/projects/cloud-armor/supporting_files/all_policies.json')

    # rules_count = count_rules.count_policy_rules(all_policies)

    one_policy = security_policies.get_one_policy(
        PROJECT_NAME, POLICY_NAME)

    allow_no_preview_list = manage_rules.create_lists(one_policy)

    rules = manage_rules.combine_rules(allow_no_preview_list)

    rules_to_patch= rules[0]
    rules_to_discard = rules[1]

    fff = ''


# main()

# Main function calling
if __name__ == "__main__":
    main()
