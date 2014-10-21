import unittest

from gtlaunch.launcher import Launcher


class MockOptions(object):
    def __init__(self):
        self.verbose = False
        self.config = ''
        self.project = ''


class LauncherTestCase(unittest.TestCase):
    def setUp(self):
        self.options = MockOptions()
        self.launcher = Launcher(self.options, lazy=True)

    def test_lazy_init(self):
        self.assertIsNone(self.launcher.project)

    def test_no_cwd(self):
        project = {
            'tabs': [],
        }
        args = self.launcher.build_args(project)
        self.assertNotIn('--working-directory', args)

    def test_cwd(self):
        project = {
            'cwd': '/home/test',
            'tabs': [],
        }
        args = self.launcher.build_args(project)
        idx = args.index('--working-directory')
        self.assertEqual(args[idx + 1], project['cwd'])

    def test_args_maximize(self):
        project = {
            'cwd': '~',
            'tabs': [],
        }
        args = self.launcher.build_args(project)
        self.assertIn('--maximize', args)

    def test_tab_no_title(self):
        project = {
            'cwd': '/home/test',
            'tabs': [{
                'command': 'ls -la',
            }],
        }
        args = self.launcher.build_args(project)
        idx = args.index('--title')
        self.assertEqual(args[idx + 1], project['tabs'][0]['command'])

    def test_tab_title(self):
        project = {
            'cwd': '/home/test',
            'tabs': [{
                'command': 'ls -la',
                'title': 'list stuff',
            }],
        }
        args = self.launcher.build_args(project)
        idx = args.index('--title')
        self.assertEqual(args[idx + 1], 'list stuff')


if __name__ == '__main__':
    unittest.main()
