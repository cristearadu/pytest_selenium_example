from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import Timeouts


class CustomMethods:

    """
    CustomMethods class created to improve the driver object, to add more functions to it the driver, such as:
        - wait_for_element_to_be_invisible
        - wait_for_element_to_be_visible
        - wait_for_element_to_be_clickable
        - check_exists
        - get_locator_by_index
    """

    def wait_for_element_to_be_invisible(self, locator, timeout: int = Timeouts.WAIT_TO_DISAPPEAR):
        WebDriverWait(self, timeout).until(EC.invisibility_of_element_located(locator))

    def wait_for_element_to_be_visible(self, locator, timeout: int = Timeouts.TIMEOUT_DEFAULT):
        WebDriverWait(self, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout: int = Timeouts.TIMEOUT_DEFAULT):
        WebDriverWait(self, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_have_specific_text(self, locator, timeout: int = Timeouts.TIMEOUT_DEFAULT,
                                               text: str = ''):
        WebDriverWait(self, timeout).until(CheckTextChanged(text, locator))

    def check_exists(self, locator, timeout: int = Timeouts.TIMEOUT_DEFAULT):
        """
        Return True if element has been located, else returns False
        """
        try:
            WebDriverWait(self, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def get_locator_by_index(self, locator, index=1):
        """
        Function that converts a locator by index and returns an xpath like:
        (By.XPATH, (.//original_xpath)[index])
        """
        locator_list = list(locator)
        locator_list[1] = f"({locator_list[1]})[{str(index)}]"
        locator_tuple = tuple(locator_list)
        return locator_tuple

    """
    Unused functions for webdriver
    """

    def open_new_tab(self, url: str):
        self.execute_script(f'window.open("{url}", "_blank");')

    def switch_tab(self, tab_number: int):
        self.switch_to.window(self.window_handles[tab_number - 1])


class CheckTextChanged(object):
    """
    Class used for WebDriverWait to check the text of an element has changed upon calling the function
    """

    def __init__(self, text, locator):
        self.text = text
        self.locator = locator

    def __call__(self, driver):
        new_element = driver.find_element(*self.locator)
        return new_element.text != self.text


class CustomWebDriverChrome(webdriver.Chrome, CustomMethods):

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        super().__init__(executable_path='chromedriver',
                         service=Service(ChromeDriverManager().install()),
                         options=chrome_options)

        self.implicitly_wait(Timeouts.IMPLICITLY_WAIT)


class CustomWebDriverFirefox(webdriver.Chrome, CustomMethods):

    def __init__(self):
        firefox_options = webdriver.ChromeOptions()
        firefox_options.add_argument("start-maximized")
        firefox_options.add_argument("--disable-blink-features=AutomationControlled")

        super().__init__(executable_path='chromedriver',
                         service=Service(ChromeDriverManager().install()),
                         options=firefox_options)

        self.implicitly_wait(Timeouts.IMPLICITLY_WAIT)
