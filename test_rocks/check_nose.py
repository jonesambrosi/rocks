import config
from nose2.main import discover

nose = discover(plugins=['coverage', 'check_code', 'timer_test_function'])

print(nose.defaultPlugins)
