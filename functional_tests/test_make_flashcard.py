from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class CreateFlashcard(FunctionalTest):

    def test_user_can_create_card(self):
        # Bruno goes to the website
        self.browser.get(self.live_server_url)
        self.assertIn('home', self.browser.title.lower())

        # He sees a prompt to create a flashcard and creates one
        self.browser.find_element_by_id('id_title').click()
        self.browser.find_element_by_id('id_title').send_keys(
            'My new flashcard'
        )
        self.browser.find_element_by_id('id_front-text').send_keys(
            'What is the mass of the sun?'
        )
        self.browser.find_element_by_id('id_back-text').send_keys(
            '1.989*10^30 kg'
        )
        self.browser.find_element_by_id('id_back-text').send_keys(Keys.ENTER)

        # The page redirects to itself and he is greeted by a success message
        self.wait_for(
            lambda: self.assertIn(
                'success',
                self.browser.find_element_by_class_name(
                    'alert-success').text.lower()
            )
        )




