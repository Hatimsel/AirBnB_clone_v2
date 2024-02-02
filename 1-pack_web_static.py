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
        year, month, day = d.year, d.month, d.day
        hr, min, sec = d.hour, d.minute, d.second
        file_name = 'web_static_{}{}{}{}{}{}.tgz'\
                    .format(year, month, day, hr, min, sec)
        local(
            "tar -cvzf versions/{} web_static".
            format(file_name)
        )
        return f"versions/{file_name}"
    except Exception:
        return None
