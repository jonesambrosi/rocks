# # coding: utf-8
# from __future__ import unicode_literals, division, absolute_import, print_function

# import sys


# # The name of the package
# pkg_name = 'rocks'

# # A list of all python files in subdirectories, listed in their dependency
# # order
# pkg_files = [
#     # 'subdir._types',
#     # 'subdir._osx',
#     # 'subdir._linux',
#     # 'subdir._win',
#     'rocks',
# ]

# if sys.version_info >= (3,):
#     from imp import reload
#     prefix = pkg_name + '.'
# else:
#     prefix = ''

# for pkg_file in pkg_files:
#     pkg_file_path = prefix + pkg_file
#     if pkg_file_path in sys.modules:
#         reload(sys.modules[pkg_file_path])
