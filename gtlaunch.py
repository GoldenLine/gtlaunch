#/usr/bin/env python

import argparse
import json
import os
import subprocess


def run(args):
    with open(os.path.expanduser(args.config), 'r') as fp:
        config = json.load(fp)
    project = config['test']
    args = ['gnome-terminal', '--maximize']
    args.extend(['--working-directory', os.path.expanduser(project['cwd'])])
    for idx, tab in enumerate(project['tabs']):
        tab_option = '--tab' if idx == 0 else '--tab-with-profile=Default'
        prefix = project.get('prefix', 'true')
        command = "zsh -is eval '{} && {}'".format(prefix, tab['command'])
        args.append(tab_option)
        args.extend(['--title', tab['title']])
        args.extend(['--command', command])
    return subprocess.Popen(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--config', metavar='FILE', help="path to configuration file",
        default="~/gtlaunch.json",
    )
    args = parser.parse_args()
    run(args)
