import requests, json, os, re
import pywidevine.clients.appletv.config as aptv_cfg
import urllib.parse
import sys

currentFile = 'appletv'
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)
cookies_file = dirPath + '/cookies/' + 'cookies_aptv.txt'

def parseCookieFile(file_path):
    cookies = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            lineFields = line.strip().split('\t')
            if len(lineFields) >= 7:
                cookies[lineFields[5]] = lineFields[6]
    return cookies

def get_auth_headers(content_url):

    def urldecode(str_val):
        return urllib.parse.unquote(str_val)

    COOKIES = parseCookieFile(cookies_file)
    COMMOM_HEADERS = aptv_cfg.COMMOM_HEADERS
    COMMOM_HEADERS["media-user-token"] = COOKIES["media-user-token"]

    while 1:
        html_data = requests.get(url=content_url, headers=COMMOM_HEADERS, timeout=15)
        if html_data.ok:
            break

    html_data = html_data.text.replace('\r\n', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('  ', '')
    html_data_list = re.split('(?i)(</div>)', html_data)

    json_web = []
    AUTH_TOKEN = None
    for div in html_data_list:
        rg = re.compile('(<meta name="web-tv-app/config/environment" content=")(.*)("><!-- EMBER_CLI_FASTBOOT_TITLE --)')
        m = rg.search(div)
        if m:
            AUTH_TOKEN = json.loads(urldecode(m[2]))["MEDIA_API"]["token"]

    if not AUTH_TOKEN:
        print("Error: Could not extract Apple TV authorization token from webpage HTML.")
        sys.exit(1)

    COMMOM_HEADERS["authorization"] = "Bearer %s" % (AUTH_TOKEN)

    return {"wvHeaders": COMMOM_HEADERS}, COOKIES