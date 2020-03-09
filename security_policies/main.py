import count_rules
import security_policies

PROJECT_NAME = 'uri-test'
POLICY_NAME = 'armor-policy1'


def main():

    rules_work = security_policies.patch_one_rule(
        PROJECT_NAME, POLICY_NAME, 66)

    all_policies = security_policies.get_all_policies(PROJECT_NAME)

    # rules_count = count_rules.count_policy_rules(
    #     '/Users/ukatsir/projects/cloud-armor/supporting_files/all_policies.json')

    rules_count = count_rules.count_policy_rules(all_policies)

    one_policy = security_policies.get_one_policy(
        PROJECT_NAME, POLICY_NAME)

    fff = rules_count


main()
