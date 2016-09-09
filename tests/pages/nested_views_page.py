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


class NestedViewsPage(BasePage):
    """Nested views page representation."""
    NEXT_BUTTON_ID = 'Next'
    BACK_BUTTON_ID = 'Back'

    def click_next_button(self):
        """Taps on the next button."""
        next_button = self.driver.find_element_by_accessibility_id(self.NEXT_BUTTON_ID)
        next_button.click()

    def click_back_button(self):
        """Taps on the back button."""
        back_button = self.driver.find_element_by_accessibility_id(self.BACK_BUTTON_ID)
        back_button.click()

    def get_static_text(self):
        """Returns text on a nested view page."""
        static_texts = self.driver.find_elements_by_class_name(self.STATIC_TEXT_CLASS)
        nested_text = static_texts[-1] # Retrieves the topmost static text object
        return nested_text.text
