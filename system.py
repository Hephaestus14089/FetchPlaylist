#!/usr/bin/env python3

import os

def create_destination(name):
    print("Creating directory '{}' ...".format(name))
    os.mkdir(name)
    os.chdir(name)
