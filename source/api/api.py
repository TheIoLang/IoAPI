from flask import Flask, request, render_template # Add more functions to import
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
  return "IoAPI"
