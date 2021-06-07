__author__ = "Poojitha Vijayanarasimha"
__email__ = "poojitha.vijayanarasimha@sap.com"
__version__ = "1.0"

import requests

from flask import Flask
from flask import request

from hashlib import sha512

from definition import SSL_CERT, SSL_KEY, URL

flask_app = Flask(__name__)

SERVER_PORT = '5002'
flask_app.config['SERVER_NAME'] = URL + SERVER_PORT

previous_passwords = []

class RepeatedPassword:
    def __init__(self):

        # Tuple of SSL cert & key
        self.ssl_credentials = (SSL_CERT, SSL_KEY)

        # Enable serving multiple request simultaneously
        self.multi_threaded = True

        # Alert messages
        self.alert_msg_not_found = "Service 3: Last 10 API calls did not contain " \
                                    "the entered password"
        self.alert_msg_found = "Service 3: Last 10 API calls contained the entered " \
                                "password"

    def check_repeated_passwords(self, password):

        # Hash the password before saving
        hashed_password = sha512(password.encode('utf-8')).hexdigest()

        if not previous_passwords:
            previous_passwords.insert(0, hashed_password)
            return self.alert_msg_not_found

        else:

            # Check last 10 entries in the hashed password list
            for each_password in previous_passwords[0:10]:

                if hashed_password == each_password:
                    previous_passwords.insert(0, hashed_password)
                    return self.alert_msg_found
            
            # If password does not match with any passwords in the common passwords list
            previous_passwords.insert(0, hashed_password)
            return self.alert_msg_not_found

@flask_app.route('/', methods=['GET', 'POST'])
def receive_password():
    if request.method == 'POST':
        received_password = request.json['password']

        repeated_password = RepeatedPassword()
        result = repeated_password.check_repeated_passwords(received_password)

        response = requests.post(url = 'https://' + URL + '5000' + '/service_3', 
                                    json={'reply':result}, verify=False)

        return 'JSON Posted'

  

if __name__ == '__main__':
    repeated_password = RepeatedPassword()
    flask_app.run(ssl_context=repeated_password.ssl_credentials, threaded=repeated_password.
                    multi_threaded, debug = True)
