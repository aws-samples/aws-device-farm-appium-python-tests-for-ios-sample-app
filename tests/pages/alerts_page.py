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


class AlertsPage(BasePage):
    """Alerts page representation."""
    OK_BUTTON_ID = 'OK'
    MODAL_BUTTON_ID = 'Modal'

    def click_modal_button(self):
        """Taps the modal button."""
        modal_button = self.driver.find_element_by_accessibility_id(self.MODAL_BUTTON_ID)
        modal_button.click()

    def modal_text_is_displayed(self):
        """Returns visibility of modal's message as a boolean."""
        modal_text = self.driver.find_element_by_class_name(self.STATIC_TEXT_CLASS)
        return modal_text.is_displayed()

    def accept_message(self):
        """Taps the OK button to accept the modal."""
        ok_button = self.driver.find_element_by_accessibility_id(self.OK_BUTTON_ID)
        ok_button.click()
