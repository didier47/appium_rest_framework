import os

from appium import webdriver
from rest_framework.serializers import Serializer

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AppiumAppSerializer(Serializer):

    def test_appium(self):
        desired_caps = dict(
            platformName='Android',
            platformVersion='10',
            automationName='uiautomator2',
            deviceName='Android Emulator',
            app=PATH('../../../apps/selendroid-test-app.apk')
        )
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        el = self.driver.find_element_by_accessibility_id('item')
        el.click()
