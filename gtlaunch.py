#/usr/bin/env python

import os
import subprocess

config = {
    'test': {
        'prefix': 'workon test',
        'cwd': '~/Development',
        'tabs': [
            {
                'title': 'editor',
                'command': 'vim',
            },
            {
                'title': 'python',
                'command': 'python',
            },
            {
                'title': 'git',
                'command': 'git status',
            },
        ],
    },
}


def run():
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
    run()
