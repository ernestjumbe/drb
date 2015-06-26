import os
import logging
#logging.basicConfig(level=logging.DEBUG)
#from fabric.api import env
from cuisine import *
from fabric.context_managers import cd, prefix
from fabric.api import env, run, sudo, put, local


env.use_ssh_config = True
#env.ssh_config_path = '~/.ssh/config'
env.hosts = ['drb']
env.disable_known_hosts = True

tmp_dir = "/opt/drbenv/tmp"

ROOT_PATH = os.path.dirname(__file__)

REMOTE_PROJECT_PATH = '/opt/drbenv'

PROJECT_NAME = 'detrundebord'


venv = 'source /opt/drbenv/bin/activate'

def _install_deps():
	with cd('/opt/drbenv/detrundebord'), prefix(venv):
		sudo("pip install -r requirements.txt")

def restart():
	with cd('/opt/drbenv/detrundebord'), prefix(venv):
		sudo("supervisorctl restart gunicorn")
		sudo("service nginx restart")

def _djangoManage(command):
	with cd('/opt/drbenv/detrundebord'), prefix(venv):
		sudo("./manage.py %s --settings=detrundebord.settings.prod" % command)

def _get_code():
	local("git pull")

def _migrate():
	_djangoManage("makemigrations")
	_djangoManage("migrate")

def backup():
	local('pip freeze > requirements.txt')
	local('git pull')
	local('git add .')
	print("Enter your commit message:")
	comment = raw_input()
	local('git commit -m "%s"' % comment)

	local('git push')

def csu():
	_djangoManage("createsuperuser")

def testgunicorn():
	with cd('/opt/drbenv/detrundebord'):
		sudo('/opt/drbenv/bin/gunicorn -c /opt/drbenv/gunicorn_config.py detrundebord.wsgi:application')

def _pack():
	with cd(ROOT_PATH):
		if not file_exists('latest.zip'):
			local('rm latest.zip')

	local('git archive --format zip -o latest.zip HEAD')

def _install_gunicorn():
	with cd('/opt/drbenv/detrundebord'), prefix(venv):
		sudo("pip install gunicorn")

def _collectstatic():
	_djangoManage("collectstatic --noinput")


def _gunicorn():
	put('setup/dev_gunicorn_config.py', '/opt/drbenv/tmp')
	with cd('/opt/drbenv'):
		sudo('cp tmp/dev_gunicorn_config.py gunicorn_config.py')

def _supa_gunicorn():
	put('setup/dev_gunicorn.conf', '/opt/drbenv/tmp')
	with cd('/opt/drbenv'):
		sudo('cp tmp/dev_gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf')
		sudo('supervisorctl reread')
		sudo('supervisorctl update')

def _rmTemp():
	with cd('/opt/drbenv'):
		sudo('rm -rf tmp/')

# def _setEnvVars():
# 	with open("fooplaapi/settings/secrets.py", "rw+") as f:
# 		for line in f:
# 			line = _stripBadCahrs(line)
# 			sudo("export %s" % (line)

# def _stripBadCahrs(line):
# 	for ch in ['\'', ' ', '"', '\n']:
# 		if ch in line:
# 			line=line.replace(ch, "")


def deploy():
	#backup()
	_pack()

	if not dir_exists('/opt/drbenv'):
		sudo('virtualenv --no-site-packages /opt/drbenv')

	with cd('/opt/drbenv'):
		run('mkdir -p detrundebord')
		run('mkdir -p tmp')
	
	put('latest.zip', '/opt/drbenv/detrundebord')

	with cd('/opt/drbenv/detrundebord'):
		sudo('unzip latest.zip')
		sudo('rm latest.zip')

	sudo('mkdir -p /var/www/drb/static')
	sudo('mkdir -p /var/www/drb/media')

	_install_deps()
	_migrate()
	_install_gunicorn()
	_gunicorn()
	_supa_gunicorn()
	_rmTemp()
	_collectstatic()
	restart()

def pdeploy():
	#backup()
	_pack()
	sudo('rm -rf /opt/drbenv/detrundebord/*')
	put('latest.zip', '/opt/drbenv/detrundebord')

	with cd('/opt/drbenv/detrundebord'):
		sudo('unzip latest.zip')
		sudo('rm latest.zip')

	_install_deps()
	_migrate()
	_collectstatic()
	restart()

def cleanup():
	sudo('rm -rf /opt/drbenv/detrundebord/')
	#sudo('rm -rf /opt/fooplaapienv/')
	sudo('rm -rf /etc/supervisor/conf.d/gunicorn.conf')
	sudo('rm -rf /opt/drbenv/gunicorn_config.py')
	_rmTemp()

	return line

def remote_uname():
	sudo('uname -a')

def tpath():
	print ROOT_PATH


