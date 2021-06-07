__author__ = "Poojitha Vijayanarasimha"
__email__ = "poojitha.vijayanarasimha@sap.com"
__version__ = "1.0"

import requests

from flask import Flask
from flask import request, render_template, redirect

from definition import *

flask_app = Flask(__name__)

SERVER_PORT = '5000'
#flask_app.config['SERVER_NAME'] = SERVER_NAME + ':' + SERVER_PORT


class EnterPassword:
    def __init__(self):
        # Tuple of SSL cert & key
        self.ssl_credentials = (SSL_CERT, SSL_KEY)

        # Enable serving multiple request simultaneously
        self.multi_threaded = True
    
    @flask_app.route('/')
    def index():
        return render_template('login_page.html', title='Welcome')

    @flask_app.route('/service_2', methods=['GET', 'POST'])
    def check_password_strength():
        if request.method == 'POST':
            
            received_resp = request.json['reply']

            global SERVICE_REPLY_2
            SERVICE_REPLY_2 = received_resp
        
        return STATUS
    
    @flask_app.route('/service_3', methods=['GET', 'POST'])
    def check_repeated_password():
        if request.method == 'POST':
            
            received_resp = request.json['reply']

            global SERVICE_REPLY_3
            SERVICE_REPLY_3 = received_resp
        
        return STATUS

    @flask_app.route('/service_4', methods=['GET', 'POST'])
    def check_common_password():
        if request.method == 'POST':
            
            received_resp = request.json['reply']

            global SERVICE_REPLY_4
            SERVICE_REPLY_4 = received_resp
        
        return STATUS

    @flask_app.route('/result')
    def print_result():
        
        # Add all the service responses to a list
        all_responses = [SERVICE_REPLY_1, SERVICE_REPLY_2, SERVICE_REPLY_3, SERVICE_REPLY_4]

        # Render the result page
        return render_template('result.html', all_responses=all_responses)

    @flask_app.route('/handler', methods=['GET', 'POST'])
    def orchestrate_services():
        if request.method == 'POST':
            login_details = request.form['password']

            global SERVICE_REPLY_1
            SERVICE_REPLY_1 = 'Service 1: Password entered is ' + login_details

            # Send password to service 2
            req_status_2 = requests.post(url = 'https://' + SERVER_NAME + ':' + '5001', 
                                        json={'password':login_details}, verify=False)

            # Send password to service 3
            req_status_3 = requests.post(url = 'https://' + SERVER_NAME + ':' + '5002', 
                                        json={'password':login_details}, verify=False)

            # Send password to service 4
            req_status_4 = requests.post(url = 'https://' + SERVER_NAME + ':' + '5003', 
                                        json={'password':login_details}, verify=False)
                                    

            return redirect('https://' + SERVER_NAME + ':' + MAIN_SERVER_PORT + '/result', code=302)
      
    
if __name__ == '__main__':
    main_service = EnterPassword()
    flask_app.run(ssl_context=main_service.ssl_credentials, threaded=main_service.
                    multi_threaded, debug = True, host=SERVER_NAME, port=SERVER_PORT)