import os
import platform
import unittest

from rest_framework.serializers import Serializer

from appium_app.appium.runner import ParametrizedTestCase
from appium_app.tests import EribankTest

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AppiumAppSerializer(Serializer):
    device_config = {}

    def kill_adb(self):
        if platform.system() == "Windows":

            os.system(PATH("../media/documents/kill5037.bat"))
        else:
            os.popen("killall adb")
        os.system("adb start-server")

    def runnerPool(self):
        self.device_config['deviceName'] = 'hamrgywwo7zhzlmr'
        self.device_config['platformVersion'] = '10'
        self.device_config["platformName"] = "android"
        self.device_config["automationName"] = "uiautomator2"
        self.device_config["appPackage"] = 'com.experitest.ExperiBank'
        self.device_config["appActivity"] = 'com.experitest.ExperiBank.LoginActivity'
        self.device_config['unicodeKeyboard'] = True
        self.device_config['resetKeyboard'] = True
        self.device_config['androidScreenshotPath'] = '/storage/emulated/0/Pictures/Screenshots/'

        self.runnerCaseApp()

    def runnerCaseApp(self):
        suite = unittest.TestSuite()
        suite.addTest(ParametrizedTestCase.parametrize(EribankTest, param=self.device_config))
        unittest.TextTestRunner(verbosity=2).run(suite)
