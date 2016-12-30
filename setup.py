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
        # test_suite='nose2.collector.collector',
        packages=['rocks.rocks'],
        # namespace_packages=['tests'],
        # packages=find_packages()
    )
