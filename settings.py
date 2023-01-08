import os


ROOT_WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
WEBSITE = 'https://magento.softwaretestingboard.com/'
LOGS_FOLDER = 'logs_folder'


class Timeouts(object):
    ELEMENT = 5
    SMALL = 10
    MEDIUM = 180
    HIGH = 240
    TIMEOUT_DEFAULT: int = 15
    WAIT_TO_DISAPPEAR: int = 60
    CHECK: int = 3
    FAST_CHECK: int = 1
    IMPLICITLY_WAIT: int = 0.1
