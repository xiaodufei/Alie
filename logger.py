import sys
import logging
from colorama import Fore, Style
from settings import Settings


class Logger(object):

    def __init__(self, logger_name, settings):
        """
        创建日志记录器，设定日志级别
        :param logger:  定义对应的程序模块名name，默认为root
        """
        # 创建一个logger
        self.logger = logging.getLogger(name=logger_name)
        self.logger.setLevel(logging.DEBUG)  # 指定最低的日志级别 critical > error > warning > info > debug

        # 创建一个handler -- 用于输出到控制台
        console_handler = logging.StreamHandler(sys.stdout)  # sys.stdout用来设置 控制台输出字体的颜色
        console_handler.setLevel(settings.debug_level)

        # 设置handler的输出格式
        formatter = logging.Formatter(fmt="%(asctime)s | %(name)s | %(message)s",
                                      datefmt='%Y-%m-%d %H:%M:%S')  # 设置 日期输出格式
        # 用formatter渲染Handler
        console_handler.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(console_handler)

    def debug(self, msg):
        """
        定义输出的颜色debug--white，info--green，warning/error/critical--red
        :param msg: 输出的log文字
        :return:
        """
        self.logger.debug(f"DEBUG   | {msg}" + Style.RESET_ALL)

    def info(self, msg):
        self.logger.info(Fore.GREEN + f"INFO    | {msg}" + Style.RESET_ALL)

    def warning(self, msg):
        self.logger.warning(Fore.RED + f"WARNING | {msg}" + Style.RESET_ALL)


if __name__ == '__main__':

    ai_settings = Settings()

    # 创建logger实例对象
    log = Logger(logger_name="DOC Ticketing", settings=ai_settings)

    # 测试数据
    main_ticket = 'Z_SRM16350556A'
    sub_ticket = 'Z_SRM16350556A001'

    # 输出log
    log.debug("ticket")
    log.info(f'main ticket: {main_ticket:17} | sub ticket: {sub_ticket}')
    log.warning("warning")
