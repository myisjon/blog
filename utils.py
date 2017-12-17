import ssl
import json
from urllib import request


APPCODE = 'APPCODE'
HOST = 'https://dm-81.data.aliyun.com'
PATH = '/rest/160601/ip/getIpInfo.json'
QUERYS = 'ip={ip}'

try:
    from config import *
except Exception:
    pass

def get_ip_detail(ip, uri=''):
    """
    return ip address detail
    - code: error code, 0 or 1, 0 is ok
    - data: ip address
    - country: country
    - area: area
    - region: province
    - city: city
    - county: county seat
    - isp: internet service provider
    - country_id: country id
    - area_id: area id
    - region_id: region id
    - city_id: city id
    - county_id: county id
    - isp_id: isp id
    eg:
	{
	  "code": 0,
	  "data": {
	    "ip": "210.75.225.254",
	    "country": "中国",
	    "area": "华北",
	    "region": "北京市",
	    "city": "北京市",
	    "county": "",
	    "isp": "电信",
	    "country_id": "86",
	    "area_id": "100000",
	    "region_id": "110000",
	    "city_id": "110000",
	    "county_id": "-1",
	    "isp_id": "100017"
	  }
	}
    """
    if not uri:
        uri = '{}{}?{}'.format(HOST, PATH, QUERYS.format(ip=ip))
    req = request.Request(uri)
    req.add_header('Authorization', 'APPCODE {}'.format(APPCODE))
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    resp = request.urlopen(req, context=ctx)

    content = json.loads(resp.read().decode('utf-8'))
    return content
