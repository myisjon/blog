import hug

from .utils import get_ip_detail


@hug.get('/', output=hug.output_format.text)
@hug.directive()
def echo_ip(request=None, **kwargs):
    really_ip = request.headers.get('X-FORWARDED-FOR')
    really_ip = really_ip if really_ip else request.headers.get('X-REAL-IP')
    ip_detail = get_ip_detail(really_ip)
    if ip_detail.get('code') != 0 or not ip_detail.get('data'):
        return really_ip

    ip_detail = ip_detail['data']
    content = []
    data_format = {
        "ip": "ip",
        "country": "国家",
        "area": "大区",
        "region": "省会",
        "city": "城市",
        "county": "区县",
        "isp": "运营商",
    }
    content = ['{}: {}'.format(value, ip_detail[key]) for key, value in data_format.items() if ip_detail.get(key)]
    return '  '.join(content)

@hug.not_found(output=hug.output_format.text)
def not_found_handler():
    return 'not found'
