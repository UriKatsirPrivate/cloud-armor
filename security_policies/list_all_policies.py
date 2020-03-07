from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json


def get_all_policies():

    flow = InstalledAppFlow.from_client_secrets_file(
        'supporting_files/client_secret_960394617171.json',
        scopes=['https://www.googleapis.com/auth/cloud-platform'])

    credentials = flow.run_local_server()
    # credentials = flow.run_console()

    security_policy_service = build('compute', 'v1', credentials=credentials)

    policies = security_policy_service.securityPolicies().list(
        project='uri-test').execute()

    ff = json.dumps(policies)

    id = policies['items'][0]['id']

    return ff

    ddd = ""
