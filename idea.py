from random import randint
import time
import math

data = [x.rstrip() for x in open("idea.dat",'r').readlines()]

def get_key () :
    result = ''
    choose = []
    KEY =5
    while len(choose) <= KEY :
        index = randint(0, len(data))
        if index not in choose :
            choose.append(index)

    for i in range(len(choose)) :
        if i == 0 :
            result += "$$ " + data[choose[i]] + " $$ <br>"
        else :
            result += "   " +  data[choose[i]] + "<br>"
    
    return result
#===================

from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET']) 
def get() :
    return app.send_static_file('idea.html') 


@app.route('/', methods=['POST']) 
def get_dat() :
    out = open('today').read()
    if out == '' :
        out = get_key()
        with open('today','w') as fout :
            fout.write(out)
        return out
    return out


@app.route('/get', methods=['POST']) 
def g() :
    out = get_key()
    with open('today','w') as fout :
        fout.write(out)
    return out


app.run(host='0.0.0.0', port='8000')
