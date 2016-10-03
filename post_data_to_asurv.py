#!/usr/bin/python

import requests
import base64
import json
import datetime
from requests.auth import HTTPBasicAuth
from requests_ntlm import HttpNtlmAuth
from datetime import datetime, timedelta

d = datetime.today() - timedelta(days=1)
old_date = d.strftime('%Y-%m-%d')

string='<toggl_api_key>'+':api_token'
workspace=<toggl_workspace_id>
uapi='api_test'
proxies = {
  "http": "<proxy_ip>:<proxy_port>",
  "https": "<proxy_ip>:<proxy_port>",
}

headers={'Authorization':'Basic '+base64.b64encode(string)}
params={'workspace_id': workspace, 'since': old_date, 'until': old_date, 'user_agent': uapi}
url='https://toggl.com/reports/api/v2/details?'

r = requests.get(url, headers=headers, params=params, proxies=proxies)

json_data = r.json()

import datetime

request = u"""<?xml version="1.0" encoding="utf-8"?>"""

for i in json_data['data']:
    if i['user'] == '<toggl_user_name>':
        time = (i['dur'])
        start_time= (i['start'])
        task = (i['task'])
        client = (i['client'])
        project = (i['project'])
        description = (i['description'])
        d = (time/1000)
        hours, remainder = divmod(d, 3600)
        minutes, seconds = divmod(remainder, 60)
        hh = ("%d" % (hours))
        mm = ("%d" % (minutes))
        request = u"""<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
              <soap:Body>
                <Insert xmlns="http://tempuri.org/">
                  <emailcreator><email sender aka name@domain.com></emailcreator>
                  <workdate>{start_time}</workdate>
                  <customer>{client}</customer>
                  <project>{project}</project>
                  <workname>{description}</workname>
                  <hours>{hh}</hours>
                  <minutes>{mm}</minutes>
                  <comments></comments>
                  <worktype>1</worktype>
                </Insert>
              </soap:Body>
            </soap:Envelope>""".format(start_time=start_time, client=client, project=project, description=description, hh=hh, mm=mm)
        encoded_request = request.encode('utf-8')

        authenticationHeader = {
        "Host": "<hostname (dns fqnd)>",
        "Content-Type": "text/xml; charset=UTF-8",
        "Content-Length": len(encoded_request)
        }

        response = requests.post(url="http://<to asmx page>",
        auth=HttpNtlmAuth('<domain>\\<user>','<password>'),
        headers = authenticationHeader,
        data = encoded_request,
        verify=False)