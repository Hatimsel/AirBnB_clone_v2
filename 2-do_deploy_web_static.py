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

        file = os.path.basename(archive_path)
        file_name = file.split('.')[0]
        dir = '/data/web_static/releases/'

        put(archive_path, '/tmp/{}'.format(file))

        run(
            'mkdir -p {}{}'
            .format(dir, file_name)
        )
        run(
            'tar -xzf /tmp/{} -C {}{}'.format(file, dir, file_name))

        run('rm /tmp/{}'.format(file))

        run('mv {}{}/web_static/* {}{}'
            .format(dir, file_name, dir, file_name))

        run('rm -rf {}{}/web_static'.format(dir, file_name))

        run('rm -rf /data/web_static/current')

        run(
            'ln -s {}{} /data/web_static/current'
            .format(dir, file_name)
        )
        return True

    except Exception:
        return False
