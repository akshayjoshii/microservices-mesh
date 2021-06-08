import os
import requests
import socket

requests.packages.urllib3.disable_warnings()

# Root path of the repo
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# Path to self-signed SSL Certificate/Private Key
SSL_CERT = os.path.join(ROOT_PATH, 'static', 'ssl_certificate', 'cert.pem')
SSL_KEY = os.path.join(ROOT_PATH, 'static', 'ssl_certificate', 'key.pem')

SERVER_NAME = '0.0.0.0'

"""
# Due to limitations with Docker Desktop for Windows, I have practically no solution to get this 
# address automatically. Without this address, the containers cannot communiacte with 
# each other. Please change this address according to the IP address of your pc.
Command: ipconfig
"""
URL = '192.168.56.1' 

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