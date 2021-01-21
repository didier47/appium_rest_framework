from rest_framework.response import Response
from rest_framework.views import APIView

from appium_app.serializers import AppiumAppSerializer


class AppiumAppView(APIView):
    serializer_class = AppiumAppSerializer

    def get(self, request, *args, **kwargs):
        serializer = self._get_serializer()
        serializer.test_appium()
        return Response()

    def _get_serializer(self):
        return self.serializer_class()
