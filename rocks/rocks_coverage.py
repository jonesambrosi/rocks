import logging
import sys
import coverage
from nose2 import discover


logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)-8s %(name)s[%(lineno)d]: %(message)s",
)

logger = logging.getLogger(__name__)

def check_code(code):

    logger.debug("************* TESTE ****************")

    ret = run_coverage()

    # cov.html_report()
    print("Feito", ret)
    logger.debug("************* TESTE ****************")

    return [ret]


def run_coverage(): 
    
    cov = coverage.Coverage(data_file='/mnt/e/test_rocks/.coverage')
    cov.start()

    # this is where your python file exists
    sys.path.append("/mnt/e/test_rocks/")

    args = ["/mnt/e/test_rocks/test_me.py",
            "-s", "/mnt/e/test_rocks/",
            # "--top-level-dir",
            # "/mnt/e/test_rocks/",
            "--verbose"]

    # discover(argv=args)
    a = 1
    if a == 1:
        print(1)


    cov.stop()
    cov.save()
    # ret = cov.analysis2("test_me.TestA.test_init")
    ret = []

    return ret 

if __name__ == '__main__':
    check_code("")
