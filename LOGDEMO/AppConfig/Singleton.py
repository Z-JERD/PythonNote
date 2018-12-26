#普通程序调用日志
import logging
import os
import time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#得到当前文件所在文件夹的上一级路径
LOG_DIR = os.path.join(BASE_DIR, 'logger')
if not os.path.exists(LOG_DIR ):
    os.mkdir(LOG_DIR)

app_name = "appName"
log_file = os.path.join(LOG_DIR,'default.log')
# 一天的日志放到一个文件中
#log_file = os.path.join(LOG_DIR, 'default-{date}.log'.format(date = time.strftime("%Y%m%d",time.localtime())))


class Singleton(object):
   _instance = None

   def __new__(cls, *args, **kwargs):
      if not cls._instance:
         cls._instance = super(Singleton, cls).__new__(cls,
                                    *args, **kwargs)
      return cls._instance


class SingletonLogger(Singleton):

   def __init__(self):
      super(SingletonLogger, self).__init__()
      self.logger = logging.getLogger(app_name)
      format_str = "---[%(levelname)s][%(asctime)s] [%(module)s:%(funcName)s][%(lineno)d]:%(message)s'"
      formatter = logging.Formatter(format_str)
      #文件对象
      file_handler = logging.FileHandler(log_file)
      file_handler.setFormatter(formatter)
      # 屏幕输出
      console_handler = logging.StreamHandler()
      console_handler.setFormatter(formatter)
      self.logger.addHandler(file_handler)
      self.logger.addHandler(console_handler)
      self.logger.setLevel(logging.DEBUG)

   def debug(self, data):
      self.logger.debug(data)

   def info(self, data):
      self.logger.info(data)

   def warning(self, data):
      self.logger.warning(data)

   def error(self, data):
      self.logger.error(data)

logger = SingletonLogger()




