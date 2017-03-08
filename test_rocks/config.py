import logging
import logging.config

d = {
    'version': 1,
    'formatters': {
        'detailed': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
        },
        'alternative': {
            'class': 'logging.Formatter',
            'format': '%(levelname)-8s %(module)-30s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'alternative',
        },
        # 'file': {
        #     'class': 'logging.FileHandler',
        #     'filename': 'mplog.log',
        #     'mode': 'w',
        #     'formatter': 'detailed',
        # },
        # 'foofile': {
        #     'class': 'logging.FileHandler',
        #     'filename': 'mplog-foo.log',
        #     'mode': 'w',
        #     'formatter': 'detailed',
        # },
        # 'errors': {
        #     'class': 'logging.FileHandler',
        #     'filename': 'mplog-errors.log',
        #     'mode': 'w',
        #     'level': 'ERROR',
        #     'formatter': 'detailed',
        # },
    },
    'loggers': {
        'foo': {
            'level': 'ERROR',
            # 'handlers': ['foofile']
            'handlers': ['console']
        }
    },
    'root': {
        'level': 'ERROR',
        # 'handlers': ['console', 'file', 'errors']
        'handlers': ['console']
    },
}

logging.config.dictConfig(d)
