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

from tests.tests.base_tests import BaseTabTest
from tests.pages import DateSelectorPage


class DateSelectorTest(BaseTabTest):
    """Container for all date selector page tests."""
    MONTH = 'July'
    DAY = '5'
    YEAR = '1994'
    EXPECTED_DATE = 'Jul 5, 1994'

    def setUp(self):
        """Set up Appium connection and navigate to date selector page."""
        BaseTabTest.setUp(self)
        BaseTabTest.navigate_to_page(self)
        self.date_selector_page = DateSelectorPage(self.driver)

    def get_name(self):
        return 'Date Selector'

    def get_page_index(self):
        return 2

    def test_date_selector(self):
        """Sets date, verifies selected date text."""
        self.date_selector_page.set_date(self.MONTH, self.DAY, self.YEAR)
        self.assertEquals(self.date_selector_page.get_selected_date(), self.EXPECTED_DATE)
