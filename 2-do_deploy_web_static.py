#!/usr/bin/python3
"""
A Fabric script that distrubutes an archive
to the web servers
"""
import os
from datetime import datetime
from fabric.api import *


env.user = 'ubuntu'
env.hosts = ['54.164.144.136', '18.210.33.80']
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """
    Deploys the archive generated beforehand
    """
    try:
        if not os.path.exists(archive_path):
            return False

        file_name = os.path.basename(archive_path).split('.')[0]
        put(archive_path, '/tmp/{}'.format(file_name))

        run('mkdir -p /data/web_static/releases/{}'.format(file_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(file_name ,file_name))
        # run('mv /data/web_static/releases/{}.tgz /data/web_static/releases/{}'.format(file_name, file_name))

        run('rm -rf /tmp/{}'.format(file_name))
        run('rm -rf /data/web_static/current')

        run(
            f'ln -s /data/web_static/releases/{file_name}/web_static\
            /data/web_static/current'
        )
        return True
    except Exception as e:
        print(f'Error occured: {e}')
        return False
