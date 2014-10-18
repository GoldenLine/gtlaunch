import unittest

from gtlaunch import Launcher


class MockOptions(object):
    def __init__(self):
        self.verbose = False
        self.config = ''
        self.project = ''


class LauncherTestCase(unittest.TestCase):
    def test_lazy_init(self):
        options = MockOptions()
        launcher = Launcher(options, lazy=True)
        self.assertIsNone(launcher.project)

    def test_args_maximize(self):
        options = MockOptions()
        project = {
            'cwd': '~',
            'tabs': [],
        }
        launcher = Launcher(options, lazy=True)
        args = launcher.build_args(project)
        self.assertIn('--maximize', args)


if __name__ == '__main__':
    unittest.main()
