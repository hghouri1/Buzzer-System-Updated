# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 01:29:53 2020

@author: hassa
"""

from flask import Flask, abort , jsonify , render_template
from multiprocessing import cpu_count
import jinja2
app = Flask(__name__)

myFlag = True
teamName = "No Team"
@app.route('/')
def hello_world():
   return render_template("Reset.html")

@app.route('/<name>')
def teamA(name):
    global myFlag, teamName
    if myFlag:
        if name == "TeamA":
            myFlag = False
            teamName = "Team 1"
            return "on"
        elif name == "TeamB":
            myFlag = False
            teamName = "Team 2"
            return "on"
        elif name == "TeamC":
            myFlag = False
            teamName = "Team 3"
            return "on"  
        elif name == "TeamD":
            myFlag = False
            teamName = "Team 4"
            return "on"
        elif name == "TeamE":
            myFlag = False
            teamName = "Team 5"
            return "on"
        elif name == "TeamF":
            myFlag = False
            teamName = "Team 6"
            return "on"
        elif name == "TeamG":
            myFlag = False
            teamName = "Team 7"
            return "on"
        if name == "TeamBackup":
            myFlag = False
            teamName = "Team Backup"
            return "on"
        elif name == "getTeamName":
            return jsonify(Name=teamName)
        else:
            return "off"
    elif name == "reset":
        myFlag = True
        return "Reset Success"
    elif name == "getTeamName":
        return jsonify(Name=teamName)
    else:
        return "off"
        
   
# @app.route('/quiz/getTeamName')
# def teamName():
#     return teamName

# @app.route('/quiz/reset')
# def reset():
#     myFlag = True
#     return "Reset Successful"

if __name__ == '__main__':
   app.run("192.168.1.108","8080",threaded=True)