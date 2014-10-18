#/usr/bin/env python

import argparse
import json
import os
import subprocess


def run(options):
    if options.verbose:
        print("Reading config file '{}'...".format(options.config))
    try:
        with open(os.path.expanduser(options.config), 'r') as fp:
            config = json.load(fp)
    except IOError:
        print("Config file '{}' not found.".format(options.config))
        return
    except ValueError:
        print("Config file '{}' is invalid JSON.".format(options.config))
        return
    try:
        project = config[options.project]
    except KeyError:
        print("Project '{}' not found.".format(options.project))
        return
    args = ['gnome-terminal', '--maximize']
    args.extend(['--working-directory', os.path.expanduser(project['cwd'])])
    for idx, tab in enumerate(project['tabs']):
        tab_option = '--tab' if idx == 0 else '--tab-with-profile=Default'
        prefix = project.get('prefix', 'true')
        command = "zsh -is eval '{} && {}'".format(prefix, tab['command'])
        args.append(tab_option)
        args.extend(['--title', tab['title']])
        args.extend(['--command', command])
    if options.verbose:
        print("Running '{}'...".format(' '.join(args)))
    return subprocess.Popen(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--config', metavar='FILE', help="path to configuration file",
        default="~/gtlaunch.json",
    )
    parser.add_argument(
        '-v', '--verbose', help="verbose output",
        action='store_true',
    )
    parser.add_argument(
        dest='project', metavar='PROJECT', help="project label",
    )
    args = parser.parse_args()
    run(args)
