__author__ = "Poojitha Vijayanarasimha"
__email__ = "poojitha.vijayanarasimha@sap.com"
__version__ = "1.0"

import requests

from flask import Flask
from flask import request

from definition import SSL_CERT, SSL_KEY, SERVER_NAME, MAIN_SERVER_PORT, URL

from password_strength_checker import PasswordStrengthChecker

flask_app = Flask(__name__)

SERVER_PORT = '5001'
#flask_app.config['SERVER_NAME'] = URL + SERVER_PORT


class PasswordStrength:
    def __init__(self):

        # Tuple of SSL cert & key
        self.ssl_credentials = (SSL_CERT, SSL_KEY)

        # Enable serving multiple request simultaneously
        self.multi_threaded = True

        # Alert messages
        self.alert_msg = "Service 2: Password strength is "

    def check_password_strength(self, password):

        # Score values are referred from UIC & Wolfram Alpha
        password_strength_checker = PasswordStrengthChecker(password)
        strength_score = password_strength_checker.check_password_strength()

        return self.alert_msg + strength_score
        

@flask_app.route('/', methods=['GET', 'POST'])
def receive_password():
    if request.method == 'POST':
        received_password = request.json['password']

        repeated_password = PasswordStrength()
        result = repeated_password.check_password_strength(received_password)

        response = requests.post(url = 'https://' + URL + ':' + MAIN_SERVER_PORT + \
                                    '/service_2', json={'reply':result}, verify=False)

        return 'JSON Posted'

  

if __name__ == '__main__':
    repeated_password = PasswordStrength()
    flask_app.run(ssl_context=repeated_password.ssl_credentials, threaded=repeated_password.
                    multi_threaded, debug = True, host=SERVER_NAME, port=SERVER_PORT)
