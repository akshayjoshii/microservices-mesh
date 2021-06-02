__author__ = "Poojitha Vijayanarasimha"
__email__ = "poojitha.vijayanarasimha@sap.com"
__version__ = "1.0"

from flask import Flask
from flask import request, render_template

from definition import ROOT_PATH, SSL_CERT, SSL_KEY, SERVER_NAME

flask_app = Flask(__name__)
flask_app.config['SERVER_NAME'] = SERVER_NAME

class EnterPassword:
    def __init__(self):
        # Tuple of SSL cert & key
        self.ssl_credentials = (SSL_CERT, SSL_KEY)

        # Enable serving multiple request simultaneously
        self.multi_threaded = True
    
    @flask_app.route('/')
    def index():
        return render_template('login_page.html')
    
    @flask_app.route('/result', methods=['GET', 'POST'])
    def receive_password():
        if request.method == 'POST':
            login_details = request.form['password']
            return render_template('result.html', login_details=login_details)
        
    
if __name__ == '__main__':
    main_service = EnterPassword()
    flask_app.run(ssl_context=main_service.ssl_credentials, threaded=main_service.
                    multi_threaded, debug = True)