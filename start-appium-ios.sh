#!/bin/bash

# Assumes the .ipa file is in the same directory as this script.

directory_path="$(pwd *.ipa)"
file_name="$(basename *.ipa)"
app_absolute_path="${directory_path}/${file_name}"

appium --platform-name ios --app $app_absolute_path --udid <DEVICE UDID>