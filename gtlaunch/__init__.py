#!/usr/bin/env python

import argparse
import json
import os
import sys
import subprocess


class LauncherError(Exception):
    pass


class Launcher(object):
    def __init__(self,  options, lazy=False):
        self.options = options
        self.config = {}
        self.project = None
        if not lazy:
            self.process_options(options)

    def process_options(self, options):
        if options.verbose:
            print("Reading config file '{}'...".format(options.config))
        try:
            with open(os.path.expanduser(options.config), 'r') as fp:
                self.config = json.load(fp)
        except IOError:
            raise LauncherError("Config file '{}' not found.".format(options.config))
        except ValueError:
            raise LauncherError("Config file '{}' is invalid JSON.".format(options.config))
        if options.project:
            try:
                self.project = self.config[options.project]
            except KeyError:
                raise LauncherError("Project '{}' not found.".format(options.project))

    def build_args(self, project):
        args = ['gnome-terminal', '--maximize']
        if 'cwd' in project:
            args.extend([
                '--working-directory', os.path.expanduser(project['cwd']),
            ])
        for idx, tab in enumerate(project['tabs']):
            tab_option = '--tab' if idx == 0 else '--tab-with-profile=Default'
            prefix = project.get('prefix', 'true')
            command = "zsh -is eval '{} && {}'".format(prefix, tab['command'])
            args.append(tab_option)
            tab_title = tab.get('title', tab['command'])
            args.extend(['--title', tab_title])
            args.extend(['--command', command])
        return args

    def run(self):
        if self.options.list:
            print("\n".join(sorted(self.config.keys())))
            return
        args = self.build_args(self.project)
        if self.options.verbose:
            print("Running \"{}\"".format(' \\\n\t'.join(args)))
        return subprocess.Popen(args)


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--config', metavar='FILE', help="path to configuration file",
        default="~/gtlaunch.json",
    )
    parser.add_argument(
        '-v', '--verbose', help="verbose output",
        action='store_true',
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-l', '--list', help="list all projects", action='store_true',
    )
    group.add_argument(
        dest='project', metavar='PROJECT', help="project label", nargs='?',
    )
    args = parser.parse_args()
    try:
        launcher = Launcher(args)
        launcher.run()
    except LauncherError as e:
        print("Launcher error: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    run()
