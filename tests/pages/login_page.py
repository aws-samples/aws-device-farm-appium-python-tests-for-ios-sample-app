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


class LoginPage(BasePage):
    """Login page representation."""
    LOGIN_BUTTON_ID = 'Login'
    LOGGED_IN_MESSAGE_ID = 'Logged in as admin'
    PERMISSION_DENIED_MESSAGE_ID = 'PERMISSION DENIED'
    LOGOUT_BUTTON_ID = 'log out'
    TRY_AGAIN_BUTTON_ID = 'try again'

    def get_element_center(self, element):
        """Calculates the center of inputted element and returns it as a tuple (x, y)."""
        element_mid_width = element.size['width'] / 2
        element_mid_height = element.size['height'] / 2
        return element.location['x'] + element_mid_width, element.location['y'] + element_mid_height

    def tap_button_center(self, element):
        """Taps the center of an element.

        This was needed because "clickable" was disabled for some elements.
        """
        button_center = self.get_element_center(element)
        self.driver.tap([button_center], 1)

    def log_in(self, username, password):
        """Types in inputted username and password and presses log in button."""
        username_field = self.driver.find_element_by_class_name(self.TEXT_FIELD_CLASS)
        password_field = self.driver.find_element_by_class_name(self.SECURE_TEXT_FIELD_CLASS)
        log_in_button = self.driver.find_element_by_accessibility_id(self.LOGIN_BUTTON_ID)

        username_field.send_keys(username)
        password_field.send_keys(password)
        log_in_button.click()

    def is_valid_login_message_displayed(self):
        """Returns visibility of valid login message as a boolean."""
        logged_in_message = self.driver.find_element_by_accessibility_id(self.LOGGED_IN_MESSAGE_ID)
        return logged_in_message.is_displayed()

    def is_invalid_login_message_displayed(self):
        """Returns visibility of invalid login message as a boolean."""
        permission_denied_message = self.driver.find_element_by_accessibility_id(self.PERMISSION_DENIED_MESSAGE_ID)
        return permission_denied_message.is_displayed()

    def click_log_out_button(self):
        """Taps the log out button."""
        log_out_button = self.driver.find_element_by_accessibility_id(self.LOGOUT_BUTTON_ID)
        self.tap_button_center(log_out_button)

    def click_try_again_button(self):
        """Taps the try again button."""
        try_again_button = self.driver.find_element_by_accessibility_id(self.TRY_AGAIN_BUTTON_ID)
        self.tap_button_center(try_again_button)

    def is_at_login(self):
        """Returns whether or not we are back at the original login view as a boolean.

        Simply checks the visibility of the login button.
        """
        log_in_button = self.driver.find_element_by_accessibility_id(self.LOGIN_BUTTON_ID)
        return log_in_button.is_displayed()
