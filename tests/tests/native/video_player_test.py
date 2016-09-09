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

from tests.tests.base_tests import BaseTest
from tests.pages import VideoPlayerPage


class VideoPlayerTest(BaseTest):
    """Container for all video player page tests."""
    def setUp(self):
        """Sets up Appium connection and navigates to video player page."""
        BaseTest.setUp(self)
        BaseTest.navigate_to_page(self)
        self.video_player_page = VideoPlayerPage(self.driver)

    def get_name(self):
        return 'Video Player'

    def test_video_player(self):
        """Verifies video player is displayed."""
        self.assertTrue(self.video_player_page.video_is_displayed())
