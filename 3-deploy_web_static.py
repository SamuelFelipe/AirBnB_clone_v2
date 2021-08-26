#!/usr/bin/python3

'''
Configure the server
'''

from datetime import datetime
from fabric.api import put, run, env, local
from os.path import exists, isdir


env.hosts = ['34.138.89.43', '54.90.156.100']


def do_pack():
    '''generate a tgz archive'''
    try:
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        if isdir('versions') is False:
            local('mkdir versions')
        file_name = 'versions/web_static_{}.tgz'.format(date)
        local('tar -cvzf {} web_static'.format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    '''distributes an archive to the web servers'''
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split('/')[-1]
        no_ext = file_n.split('.')[0]
        path = '/data/web_static/releases/'
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {1}{0}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    '''send an archive to the servers'''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
