from rest_framework.response import Response
from rest_framework.views import APIView

from appium_app.appium.appium import AppiumServer
from appium_app.serializers import AppiumAppSerializer


class AppiumAppView(APIView):
    serializer_class = AppiumAppSerializer

    def get(self, request, *args, **kwargs):
        serializer = self._get_serializer()
        serializer.kill_adb()
        appium_server = AppiumServer()
        appium_server.start_server()
        serializer.runnerPool()
        appium_server.stop_server()
        return Response()

    def _get_serializer(self):
        return self.serializer_class()
