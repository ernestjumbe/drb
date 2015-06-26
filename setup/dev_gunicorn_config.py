command = '/opt/drbenv/bin/gunicorn'
pythonpath = '/opt/drbenv/detrundebord'
bind = '46.101.255.172:8001'
logfile = "/var/www/drb/logs/gunicorn.log"
workers = 3
user = 'nobody'
timeout = 120