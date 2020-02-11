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

@route('/load')
def load():
    return "%s, %s, %s" % os.getloadavg()

@route('/<key>/reboot')
def pull(key):
    if (key != config["key"]):
        return "ko"
    os.chdir(config["path"]);
    subprocess.call(["/sbin/reboot"])
    return "ok"

@route('/<key>/restart')
def restart(key):
    if (key != config["key"]):
        return "ko"
    os.chdir(config["path"]);
    subprocess.call(["/usr/sbin/service", "plexmediaserver", "restart"])
    return "ok"

@route('/<key>/update')
def update(key):
    if (key != config["key"]):
        return "ko"
    os.chdir(config["path"]);
    subprocess.call(["/bin/sh", "update.sh"])
    return "ok"

if __name__ == "__main__":
    config = open_and_load_config()
    run(host=config["host"], port=config["port"], debug=config["debug"])
