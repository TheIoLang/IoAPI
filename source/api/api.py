from flask import Flask, render_template, send_from_directory, url_for, request, redirect
import os
import json
import requests

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def index():
  return "IoAPI"

@app.route('/api')
def api_route():
  syntax = request.args.get('syntax')
  visualizer = request.args.get('visualizer')
  syntax = syntax.lower()

  if syntax == "true" or syntax == "yes":
    return render_template("syntax.html")
  elif visualizer == "true" or syntax == "yes":
    return render_template("visualizer.html")