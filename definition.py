import os
import requests

requests.packages.urllib3.disable_warnings()

# Root path of the repo
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# Path to self-signed SSL Certificate/Private Key
SSL_CERT = os.path.join(ROOT_PATH, 'static', 'ssl_certificate', 'cert.pem')
SSL_KEY = os.path.join(ROOT_PATH, 'static', 'ssl_certificate', 'key.pem')

SERVER_NAME = 'localhost'
URL = SERVER_NAME + ':'

COMMON_PASSWORDS_FILE = os.path.join(ROOT_PATH, "static", "common_passwords.txt")

# Service Replies
SERVICE_REPLY_2 = ''
SERVICE_REPLY_3 = ''
SERVICE_REPLY_4 = ''

# Status message
STATUS = "Success"