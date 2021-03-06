import os
import requests

requests.packages.urllib3.disable_warnings()

# Root path of the repo
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# Path to self-signed SSL Certificate/Private Key
SSL_CERT = os.path.join(ROOT_PATH, 'static', 'ssl_certificate', 'cert.pem')
SSL_KEY = os.path.join(ROOT_PATH, 'static', 'ssl_certificate', 'key.pem')

SERVER_NAME = '0.0.0.0'

# Kubernetes DNS will automatically resolve the exact pod details using the pod name, 
# so no need to hardcode or use any kind of direct IP/Host addresses.
URL = 'service-' 

# Port address of service_1
MAIN_SERVER_PORT = '5000'

COMMON_PASSWORDS_FILE = os.path.join(ROOT_PATH, "static", "common_passwords.txt")

# Service Replies
SERVICE_REPLY_1 = ''
SERVICE_REPLY_2 = ''
SERVICE_REPLY_3 = ''
SERVICE_REPLY_4 = ''

# Status message
STATUS = "Success"