from bottle import route, run
import subprocess, os, json, sys

CONFIG_FILE = 'config.json'

"""
Open and load a file at the json format
"""

def open_and_load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as config_file:
            return json.loads(config_file.read())
    else:
        print "File [%s] doesn't exist, aborting." % (CONFIG_FILE)
        sys.exit(1)


@route('/')
def hello():
    return "Plex API"
