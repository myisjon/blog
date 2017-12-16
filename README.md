#### 返回请求ip地址

使用hug

### 部署使用uwsgi
uwsgi --http 127.0.0.1:8000 --wsgi-file echo_ip.py --callable __hug_wsgi__ --enable-threads
