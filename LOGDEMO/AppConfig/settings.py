#Django中的配置
import os
import logging
import time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#得到当前文件所在文件夹的上一级路径
LOG_DIR = os.path.join(BASE_DIR, 'logger')
if not os.path.exists(LOG_DIR ):
    os.mkdir(LOG_DIR)
LOGGING = {
    'version': 1,
    'disable_existing_loggers':False,
    'formatters': {
        'standard': {
            'format': '------[%(levelname)s][%(asctime)s] [%(module)s:%(funcName)s][%(lineno)d]:%(message)s'},
            'simple': {
                        'format': '[%(levelname)s][%(asctime)s]-:%(message)s'
                    },
    },

    'filters': {

    },

    'handlers': {
        'console': {
                    'level': 'INFO',
                    'class': 'logging.StreamHandler',
                    'formatter': 'simple'
                },
        'file_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'default.log'),#所有的日志都记录到一个文件中
            #一天的日志放到一个文件中
            #'filename': os.path.join(LOG_DIR, 'default-{date}.log'.format(date = time.strftime("%Y%m%d",time.localtime()))),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 7,
            'encoding': 'utf8',
            'formatter': 'standard',
        },
        'error_handler': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 7,
            'encoding': 'utf8',
            'formatter': 'standard',
        },

        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
             'formatter':'standard'
        },
    },

    'loggers': {

        'mydjango': {
            'handlers': ['console','file_handler'],  #不打印到控制台就去掉console
            'level':'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },

        'error': {
            'handlers': ['console', 'error'],
            'level': 'ERROR',
            'propagate': False
        },
    }
}
logger = logging.getLogger("mydjango")
