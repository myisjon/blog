import hug


@hug.get('/', output=hug.output_format.text)
@hug.directive()
def echo_ip(request=None, **kwargs):
    really_ip = request.headers.get('X-FORWARDED-FOR')
    really_ip = really_ip if really_ip else request.headers.get('X-REAL-IP')
    return really_ip

@hug.not_found(output=hug.output_format.text)
def not_found_handler():
    return 'not found'
