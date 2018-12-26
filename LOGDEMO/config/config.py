import os
import json
import time
import logging.config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'logger')
info_file = os.path.join(LOG_DIR, "default.log")
#每天的写到一个文件中
#info_file = os.path.join(LOG_DIR, 'default-{date}.log'.format(date = time.strftime("%Y%m%d",time.localtime())))
error_file = os.path.join(LOG_DIR, "error.log")


if not os.path.exists(LOG_DIR ):
    os.mkdir(LOG_DIR)
    with open(info_file, 'w') as f1, \
            open(error_file, 'w') as f2:
        pass
#去掉console, 控制台不打印
def setup_logging(
        default_path=BASE_DIR+'/config/logging.json',
        default_level=logging.INFO,
        env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    print('value is ',value)
    if value:
        path = value
    print('path is ',path)
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        #1.将日志达到一个文件中
        config['handlers']['info_file_handler'].update({'filename':info_file})
        config['handlers']['error_file_handler'].update({'filename': error_file})
        logging.config.dictConfig(config)
        #2.每一级目录下都存在一个logger,就在logging.json中设置日志文件
    else:
        logging.basicConfig(level=default_level)


