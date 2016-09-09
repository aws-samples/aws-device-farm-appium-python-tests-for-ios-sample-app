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


class DateSelectorPage(BasePage):
    MONTH_INDEX = 0
    DAY_INDEX = 1
    YEAR_INDEX = 2

    """Date selector page representation."""
    def set_date(self, month, day, year):
        """Sets month, day, year, picker wheels.

        month -- the month as a string
        day -- the day as a string
        year -- the year as a string
        """
        wheels = self.driver.find_elements_by_class_name(self.PICKER_WHEEL_CLASS)

        month_wheel = wheels[MONTH_INDEX]
        day_wheel = wheels[DAY_INDEX]
        year_wheel = wheels[YEAR_INDEX]

        month_wheel.send_keys(month)
        day_wheel.send_keys(day)
        year_wheel.send_keys(year)

    def get_selected_date(self):
        """Retrieves selected date as a string (Month is truncated to three letters)."""
        date = self.driver.find_element_by_class_name(self.STATIC_TEXT_CLASS)
        return date.text
