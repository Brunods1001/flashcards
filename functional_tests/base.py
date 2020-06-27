from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import os
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10


def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    return modified_fn


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')

        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    @wait
    def wait_for(self, fn):
        return fn()
