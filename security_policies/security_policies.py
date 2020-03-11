from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
import sys

flow = InstalledAppFlow.from_client_secrets_file(
    'supporting_files/client_secret_960394617171.json',
    scopes=['https://www.googleapis.com/auth/cloud-platform'])

credentials = flow.run_local_server()
# credentials = flow.run_console()

security_policy_service = build('compute', 'v1', credentials=credentials)


def get_all_policies(project_name):

    policies = security_policy_service.securityPolicies().list(
        project=project_name).execute()

    all_policies = json.dumps(policies)

    id = policies['items'][0]['id']

    return all_policies


def get_one_policy(project_name, policy_name):
    policies = security_policy_service.securityPolicies().get(
        project=project_name, securityPolicy=policy_name).execute()

    one_policy = json.dumps(policies)

    name = policies['name']
    return one_policy


def get_one_rule(project_name, policy_name, rule_priority):
    rule = security_policy_service.securityPolicies().getRule(
        project=project_name, securityPolicy=policy_name, priority=rule_priority).execute()

    return rule


def patch_one_rule_new(project_name, policy_name, rule_priority, body, rule0, rule1):
    # print body
    # str(rule0['match']['config']['srcIpRanges']).replace(']', ',', 1).replace('u', '')

    # Gather IPs from both rules
    ips = []
    i = 0
    while i < len(rule0['match']['config']['srcIpRanges']):
        ips.append(rule0['match']['config']['srcIpRanges'][i])
        i = i+1

    j = 0
    while j < len(rule1['match']['config']['srcIpRanges']):
        ips.append(rule1['match']['config']['srcIpRanges'][j])
        j = j+1

    # Concat descriptions
    description = rule0['description'] + '~' + rule1['description']
    try:
        patched_rule_result = security_policy_service.securityPolicies().patchRule(
            project=project_name, securityPolicy=policy_name, body={
                'kind': 'compute#securityPolicyRule',
                'priority': str(rule0['priority']),
                'action': 'allow',
                'description': description,
                'preview': False,
                'match': {
                    'config': {
                        'srcIpRanges':
                            ips
                    },
                    'versionedExpr': 'SRC_IPS_V1'
                }
            }, priority=rule_priority).execute()
    except Exception as e:
        print "Unexpected error:", e
    except:
        print "Unexpected error:", sys.exc_info()[0]
    hello = ''

    return patched_rule_result


def patch_one_rule(project_name, policy_name, rule_priority):

    try:
        patched_rule = security_policy_service.securityPolicies().patchRule(
            project=project_name, securityPolicy=policy_name, body={'kind': 'compute#securityPolicyRule',
                                                                    'priority': 55,
                                                                    'action': 'allow',
                                                                    'preview': False,
                                                                    'match': {
                                                                        'config': {
                                                                            'srcIpRanges': [
                                                                                '194.30.2.0/24',
                                                                                '195.20.100.0/24',
                                                                                '10.1.115.0/24',
                                                                                '10.2.3.0/24',
                                                                                '10.23.36.0/24'
                                                                            ]

                                                                        },
                                                                        'versionedExpr': 'SRC_IPS_V1'
                                                                    }
                                                                    }, priority=rule_priority).execute()

    except Exception as e:
        print "Unexpected error:", e
    # except NameError as err:
    #     print "Unexpected error:", err
    # except TypeError as err1:
    #     print "Unexpected error:", err1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    hello = ''


def removeRule(project_name, policy_name, rule_priority):
    response = security_policy_service.securityPolicies().removeRule(
        project=project_name, securityPolicy=policy_name, priority=rule_priority).execute()

    return response
