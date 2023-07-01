#!/usr/bin/python3
"""Fetches https://intranet.alxswe.com/status."""
import urllib.request

with urllib.request.urlopen('https://intranet.alxswe.com/status') as url:
    s = url.read()
    req = "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
    print(req.format(type(s), s, s.decode('utf-8')))
