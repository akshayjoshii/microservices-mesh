import os

# Root path of the repo
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# Path to self-signed SSL Certificate/Private Key
SSL_CERT = 'static\ssl_certificate\cert.pem'
SSL_KEY = 'static\ssl_certificate\key.pem'

SERVER_NAME = 'localhost:5000'