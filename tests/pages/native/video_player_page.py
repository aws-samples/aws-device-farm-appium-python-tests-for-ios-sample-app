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
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class VideoPlayerPage(BasePage):
    """Video player page representation."""
    SIMULATOR_VIDEO_LOAD_TIME = 30
    MEDIA_PLAYER_VIEW_ID = 'MediaPlayerView'

    def video_is_displayed(self):
        """Returns visibility of video as a boolean.

        Implicit wait for iOS simulator because it may take some time to load the video.
        """
        wait = WebDriverWait(self.driver, self.SIMULATOR_VIDEO_LOAD_TIME)
        video_player = wait.until(ec.presence_of_element_located((By.ID, self.MEDIA_PLAYER_VIEW_ID)))
        return video_player.is_displayed()
