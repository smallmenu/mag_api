#!/usr/bin/env python
import logging
import os, errno,stat,traceback, sys, re
import subprocess
from collections import OrderedDict
from datetime import datetime
from subprocess import Popen, PIPE
import configparser
from random import randint

abspath = os.path.abspath(os.path.dirname(__file__))
middleware = os.path.dirname(abspath)
parent = os.path.dirname(middleware)
sys.path.append(parent)

from flask import Flask, abort, request, jsonify, g, url_for, render_template, escape
from flask_cors import CORS
import json

def run_query(query):
    query_id = 12
    return query_id

# initialization
app = Flask(__name__,
            static_folder="../../frontend/dist/assets",
            template_folder="../../frontend/dist")
CORS(app)
app.config['SECRET_KEY'] = 'test key'

logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def get_search():
    logger.info('Trying /search endpoint...')
    return_type = request.json.get('return_type')
    years = request.json.get('years')
    title = request.json.get('title')

    query_id = run_query("some query")
    return jsonify({'query_id': query_id}), 202

@app.route('/results/<query_id>', methods=['GET'])
def get_results(query_id):
    logger.info('Trying /results/' + query_id + ' endpoint...')

    #check filesystem for query_ids[query_id].json

    return 501

@app.route('/references/<paper_id>', methods=['GET'])
def get_references(paper_id):
    logger.info('Trying /references/' + paper_id + ' endpoint...')

    query_id = run_query("some query")
    return jsonify({'query_id': query_id}), 202

@app.route('/citations/<paper_id>', methods=['GET'])
def get_citations(paper_id):
    logger.info('Trying /citations/' + paper_id + ' endpoint...')

    query_id = run_query("some query")
    return jsonify({'query_id': query_id}), 202

@app.route('/paper/<paper_id>', methods=['GET'])
def get_paper(paper_id):
    logger.info('Trying /paper/' + paper_id + ' endpoint...')

    query_id = run_query("some query")
    return jsonify({'query_id': query_id}), 202

@app.route('/papers', methods=['POST'])
def get_multiple_papers():
    logger.info('Trying /papers endpoint...')
    papers_array = request.json.get('paper_ids')

    query_id = run_query("some query")
    return jsonify({'query_id': query_id}), 202
