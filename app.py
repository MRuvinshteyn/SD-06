#!/usr/bin/python

"""
Michael Ruvinshteyn
SoftDev1 pd7
HW06 -- Echo Echo Echo
2017 - 10 - 2
"""

from flask import Flask, render_template, redirect, url_for, request
import random

app = Flask(__name__)

@app.route('/')
def render_query():
    return render_template('input.html')

@app.route('/greet')
def render_response():
    diag()

    greets = ["Hey", "Hello", "Nice to see you", "Fancy meeting you here",
              "Wonderful weather we're having here", "Long time no see",
              "Pleased to meet you"]
    form = request.args
    username = form['username']
    greeting = random.choice(greets)
    method = request.method
    return render_template('response.html',UN = username, GR = greeting,
                           MT = method)
    
def diag():
    print "\n\n\n"
    print "app:"
    print app
    print "\nrequest.headers:"
    print request.headers
    print "\nrequest.method:"
    print request.method
    print "\nrequest.args:"
    print request.args
    print "\nrequest.args['username']:"
    print request.args['username']


if __name__ == '__main__':
    app.debug = True
    app.run()
