import count_rules
import security_policies


def main():

    all_policies = security_policies.get_all_policies()

    # rules_count = count_rules.count_policy_rules(
    #     '/Users/ukatsir/projects/cloud-armor/supporting_files/all_policies.json')

    rules_count = count_rules.count_policy_rules(all_policies)

    fff = ''


main()
