#!/usr/bin/python3
"""
A Fabric script that creates and distrubutes an archive
to the web servers
"""
import os
from datetime import datetime
from fabric.api import *
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """
    Creates and distrubutes an archive to the web servers
    """
    path_to_tgz = do_pack()
    if path_to_tgz is None:
        return False
    return do_deploy(path_to_tgz)
