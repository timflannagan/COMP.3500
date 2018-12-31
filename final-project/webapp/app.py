from flask import Flask
from flask import flash, redirect, render_template, request, session, abort
import os
import sys
import example_search

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('index.html')

@app.route('/login')
def login(name=None):
    if (example_search.search() == True):
	return render_template('login.html', name=name)
    else:
	return render_template('invalid.html')
    
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='192.168.1.3', port=4000)
