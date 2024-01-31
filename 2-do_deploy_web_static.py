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


def do_deploy(archive_path):
    """
    Deploys the archive generated beforehand
    """
    try:
        if not os.path.exists(archive_path):
            return False

        put('archive_path', '/tmp/')

        file_name = archive_path.split('/')[1].split('.')[0]
        run('tar -xzf /tmp/{} /data/web_static/releases/{}'.
            format(archive_path, file_name))

        run('rm /tmp/{} {}'.format(archive_path, '/data/web_static/current/'))
        run(
            f'ln -s /data/web_static/releases/{file_name}\
            /data/web_static/current'
        )
        return True
    except Exception:
        return False
