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


class NavigationPage(BasePage):
    """Class that handles navigation to different pages within the application."""
    INPUT_ID = 'Inputs'
    MORE_ID = 'More'
    NATIVE_ID = 'Native'
    NATIVE_CATEGORIES = frozenset(['Image Gallery', 'Scrolling View', 'Table of elements', 'Video Player',
                                     'Camera', 'Out of View Component'])
    INPUT_CATEGORIES = frozenset(['Text View', 'Toggle', 'Date Selector', 'Label View', 'Refresh Control',
                                    'Slider', 'Text Field', 'Submit', 'Selection Wheel', 'Gestures'])
    MORE_CATEGORIES = frozenset(['Nested', 'Crash', 'Alerts', 'Web', 'Login'])

    def go_to_category(self, category_name):
        """Clicks appropriate navigation bar button depending on the category to which the input belongs.

        i.e. Log in page will fall under More tab, image gallery under native, etc.

        Note: Layouts will be different in different sized devices. The MORE_CATEGORIES is constructed to include all
        possible tabs in the More section. On larger devices, the More button may be clicked unnecessarily before
        clicking the respective button in the navigation bar.
        """
        if category_name in self.INPUT_CATEGORIES:
            input_button = self.driver.find_element_by_accessibility_id(self.INPUT_ID)
            input_button.click()

        else:
            if category_name in self.MORE_CATEGORIES:
                more_button = self.driver.find_element_by_accessibility_id(self.MORE_ID)
                more_button.click()
            elif category_name in self.NATIVE_CATEGORIES:
                native_button = self.driver.find_element_by_accessibility_id(self.NATIVE_ID)
                native_button.click()

            category_button = self.driver.find_element_by_accessibility_id(category_name)
            category_button.click()
