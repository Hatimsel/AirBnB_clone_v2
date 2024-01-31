#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents
of the web_static folder
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Genreates a .tgz archive
    """
    try:
        local('mkdir -p versions')
        d = datetime.now()
        file_name = f'{d.year}{d.month}{d.day}{d.hour}{d.minute}{d.second}'
        local(
            "tar -czf versions/web_static_{}.tgz web_static".
            format(file_name)
        )
        return f"versions/{file_name}"
    except Exception:
        return None
