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
from tests.pages import AlertsPage


class AlertsTest(BaseTest):
    """Container for all alerts page tests."""
    def setUp(self):
        """Sets up Appium connection and navigates to alerts page."""
        BaseTest.setUp(self)
        BaseTest.navigate_to_page(self)
        self.alerts_page = AlertsPage(self.driver)

    def get_name(self):
        return 'Alerts'

    def test_modal(self):
        """Click modal button, verify modal message is displayed, accept the message."""
        self.alerts_page.click_modal_button()
        self.assertTrue(self.alerts_page.modal_text_is_displayed())
        self.alerts_page.accept_message()
