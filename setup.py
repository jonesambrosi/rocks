try:
    import sublime
except:
    from distutils.core import setup  # , find_packages

    setup(
        name='rocks',
        version='1.0',
        description='Rocks auto test plugin for SublimeText.',
        author='Jones Ambrosi',
        author_email='jones@centrimobi.com.br',
        url='http://rocks.io/',
        namespace_packages=['tests'],
    )
