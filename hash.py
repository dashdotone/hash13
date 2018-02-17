#!/usr/bin/env python

from __future__ import print_function

import urllib, urllib2, cookielib
import hashlib
import re

from datetime import datetime

log_url = 'https://ringzer0team.com/login'
ch_url = 'https://ringzer0team.com/challenges/13'
uname = 'user'
passwd = 'pass'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'username':uname,'password':passwd})
opener.open(log_url,login_data)
resp = opener.open(ch_url)
starttime = datetime.now()
text = resp.read().strip().splitlines()
msg = text[text.index('\t\t----- BEGIN MESSAGE -----<br />')+1].replace('<br />','').strip()
hash_msg = hashlib.sha512(msg).hexdigest()
resp = opener.open(ch_url+'/'+hash_msg)
print(datetime.now()-starttime)
print(resp.read().splitlines()[70])
