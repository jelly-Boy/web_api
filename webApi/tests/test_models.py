from django.test import TestCase
from ..models import MusicService

class MusicServiceTest(TestCase):

    def setUp(self):
        MusicService.objects.create(
            music_service_name='Test name', url='http://127.0.0.1:8000/'
        )

    def testData(self):
        test_music_service = MusicService.objects.get(music_service_name='Test name')
        self.assertEqual(
            test_music_service.get_test(), 'Test name - name of music service, http://127.0.0.1:8000/ - url of music service'
        )
