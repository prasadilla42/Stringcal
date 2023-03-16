from flask import Flask, render_template, request, jsonify
from flask.helpers import flash, redirect, url_for
from src.exception import NegativeErrorException
from src.utils import Handlers
from src.logger import logging

app = Flask(__name__)

app.config['SECRET_KEY'] = "5352f0346e9abed77a57864b4c84a6657be157ab6aff39b7"

@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html',name='index')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):        
        text = request.form['inputStringBox']
        logging.info("text is entered")
        handler=Handlers()
        try: 
            numbers=handler.handle_input_string(text)
            logging.info("numbers are identified")
        except NegativeErrorException as e:
            flash('Error {} occured,Do not enter negative numbers'.format(e.message))
            return redirect(url_for('home_page'))            
        if len(numbers) == 1:
            flash('Enter minimum 2 numbers in the text')
            return redirect(url_for('home_page'))
        result = sum(numbers)
        logging.info("Result obtained")
        return render_template('results.html',result=result)
    

if __name__ == '__main__':
    app.run(debug=True)