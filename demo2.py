from visa.logger import logging
from visa.exception import CustomException
from flask import Flask
import os, sys


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        logging.info('starting demo 2 files for demo')
        return "Hello, world!"
    except Exception as e:
        raise CustomException(e,sys)
        logging.info(visa.error_message)
        logging.info("we are testing logging function")

if __name__ == '__main__':
    app.run(debug=True)
    
