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

def patch_one_rule(project_name, policy_name, rule_priority):

    try:
        patched_rule = security_policy_service.securityPolicies().patchRule(
            project=project_name, securityPolicy=policy_name, body={
                'kind': 'compute#securityPolicyRule',
                'priority': 55,
                'action': 'allow',
                'preview': False,
                'match': {
                    'config': {
                        'srcIpRanges': [
                            '192.30.2.0/24',
                            '198.20.100.0/24',
                            '10.1.113.0/24'
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