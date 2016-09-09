# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
# http://aws.amazon.com/apache2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from tests.pages.base_pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class WebPage(BasePage):
    """Static web page representation."""
    WEBSITE_LOAD_TIME = 10

    def web_view_is_displayed(self):
        """Returns visibility of the web view.

        Does not actually check for web page content - look up hybrid page for this.
        """
        wait = WebDriverWait(self.driver, self.WEBSITE_LOAD_TIME)
        web_view = wait.until(ec.presence_of_element_located((By.CLASS_NAME, self.WEB_VIEW_CLASS)))
        return web_view.is_displayed()
