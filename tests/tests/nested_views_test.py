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
from tests.pages import NestedViewsPage


class NestedViewsTest(BaseTest):
    """Container for all nested views page tests."""
    FIRST_VIEW_TEXT = 'This is the first view'
    SECOND_VIEW_TEXT = 'This is the second view'
    THIRD_VIEW_TEXT = 'This is the third view'
    FOURTH_VIEW_TEXT = 'This is the fourth view'

    def setUp(self):
        """Sets up Appium connection and navigates to nested views page."""
        BaseTest.setUp(self)
        BaseTest.navigate_to_page(self)
        self.nested_views_page = NestedViewsPage(self.driver)

    def get_name(self):
        return 'Nested'

    def test_nested(self):
        """Cycles through nested views, verifies text on each page."""
        self.assertEquals(self.nested_views_page.get_static_text(), self.FIRST_VIEW_TEXT)

        self.nested_views_page.click_next_button()
        self.assertEquals(self.nested_views_page.get_static_text(), self.SECOND_VIEW_TEXT)

        self.nested_views_page.click_next_button()
        self.assertEquals(self.nested_views_page.get_static_text(), self.THIRD_VIEW_TEXT)

        self.nested_views_page.click_next_button()
        self.assertEquals(self.nested_views_page.get_static_text(), self.FOURTH_VIEW_TEXT)

        self.nested_views_page.click_back_button()
        self.assertEquals(self.nested_views_page.get_static_text(), self.THIRD_VIEW_TEXT)

        self.nested_views_page.click_back_button()
        self.assertEquals(self.nested_views_page.get_static_text(), self.SECOND_VIEW_TEXT)

        self.nested_views_page.click_back_button()
        self.assertEquals(self.nested_views_page.get_static_text(), self.FIRST_VIEW_TEXT)
