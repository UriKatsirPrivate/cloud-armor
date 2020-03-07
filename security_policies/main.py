import count_rules
import list_all_policies


def main():

    all_policies = list_all_policies.get_all_policies()

    # rules_count = count_rules.count_policy_rules(
    #     '/Users/ukatsir/projects/cloud-armor/supporting_files/all_policies.json')

    rules_count = count_rules.count_policy_rules(all_policies)

    fff = ''


main()
