from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json

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
