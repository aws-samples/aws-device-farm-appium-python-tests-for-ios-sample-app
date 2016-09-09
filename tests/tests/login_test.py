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

from base_tests.base_test import BaseTest
from tests.pages import LoginPage


class LoginTest(BaseTest):
    """Container for all login page tests."""
    LOGIN_SUCCESS_MESSAGE = 'You are logged on as admin'
    LOGIN_FAILURE_MESSAGE = 'You gave me the wrong username and password'
    USERNAME = 'admin'
    VALID_PASSWORD = 'password'
    INVALID_PASSWORD = 'passwrod'

    def setUp(self):
        """Sets up Appium connection and navigates to login page."""
        BaseTest.setUp(self)
        BaseTest.navigate_to_page(self)
        self.login_page = LoginPage(self.driver)

    def get_name(self):
        return 'Login'

    def test_valid_login(self):
        """Login with valid credentials, verify valid login message, log out, verify back at log in."""
        self.login_page.log_in(self.USERNAME, self.VALID_PASSWORD)
        self.assertTrue(self.login_page.is_valid_login_message_displayed())
        self.login_page.click_log_out_button()
        self.assertTrue(self.login_page.is_at_login())

    def test_invalid_login(self):
        """Login with invalid credentials, verify invalid login message, try again, verify back at log in."""
        self.login_page.log_in(self.USERNAME, self.INVALID_PASSWORD)
        self.assertTrue(self.login_page.is_invalid_login_message_displayed())
        self.login_page.click_try_again_button()
        self.assertTrue(self.login_page.is_at_login())
