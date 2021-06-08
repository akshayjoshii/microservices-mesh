__author__ = "Poojitha Vijayanarasimha"
__email__ = "poojitha.vijayanarasimha@sap.com"
__version__ = "1.0"

import requests

from flask import Flask
from flask import request

from definition import COMMON_PASSWORDS_FILE, SSL_CERT, SSL_KEY, SERVER_NAME, \
                        MAIN_SERVER_PORT, URL

flask_app = Flask(__name__)

SERVER_PORT = '5003'
#flask_app.config['SERVER_NAME'] = URL + SERVER_PORT

class CommonPassword:
    def __init__(self):

        # Tuple of SSL cert & key
        self.ssl_credentials = (SSL_CERT, SSL_KEY)

        # Enable serving multiple request simultaneously
        self.multi_threaded = True

        self.common_password_list = open(COMMON_PASSWORDS_FILE, 'r').read().split()

    def check_common_passwords(self, password):
        
        # Check in the password list
        for each_password in self.common_password_list:

            if password == each_password:
                alert_msg = "Service 4: Entered password is found in a common passwords " \
                            "list on the Internet!"

                return alert_msg
            
        # If password does not match with any passwords in the common passwords list
        alert_msg = "Service 4: Entered password is not found in a common passwords " \
                    "list on the Internet!"

        return alert_msg

@flask_app.route('/', methods=['GET', 'POST'])
def receive_password():
    if request.method == 'POST':
        received_password = request.json['password']

        common_password = CommonPassword()
        result = common_password.check_common_passwords(received_password)

        response = requests.post(url = 'https://' + URL + ':' + MAIN_SERVER_PORT + \
                                    '/service_4', json={'reply':result}, verify=False)

        return 'JSON Posted'

  

if __name__ == '__main__':
    common_password = CommonPassword()
    flask_app.run(ssl_context=common_password.ssl_credentials, threaded=common_password.
                    multi_threaded, debug = True, host=SERVER_NAME, port=SERVER_PORT)
