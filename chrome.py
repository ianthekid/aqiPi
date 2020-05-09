#!/usr/bin/python -u
import os, subprocess
new_env = dict(os.environ)
new_env['DISPLAY'] = ':0'
FNULL = open(os.devnull, 'w')

url = "http://localhost"
p = subprocess.Popen(["chromium-browser", "--kiosk", "--incognito", "--disable-infobars", url], stdout=FNULL, stderr=subprocess.STDOUT, env=new_env)