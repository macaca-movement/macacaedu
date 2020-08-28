from shutil import copyfile

from django.conf import settings
from django.core.management import BaseCommand
from study.models import StudyMedia, ActivityItem, Activity

instructions_A = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam varius
nisi vitae enim efficitur viverra. Nunc maximus vulputate
Praesent porttitor nulla in condimentum varius. Etiam aliquet ligula libero.
Pellentesque vel nisl luctus, molestie ligula sit amet, accumsan nunc.
Pellentesque vulputate diam mi, sed **tempor** diam condimentum nec. Nam elementum
fermentum felis, sed mattis ante facilisis at. Maecenas sit amet enim quis
ante vulputate egestas id nec risus. Nam ac eros vel massa semper vulputate
nec in ante. In consectetur dapibus porta. Aenean ultricies dictum ante id
aliquam. Curabitur vel laoreet quam, et rhoncus dui.
'''

instructions_B = '''
Do this for 30 seconds, then that 90 seconds. Then rest 2 days.

* A - the first thing do
* B - then there is problably a second one
* C - and finally, finally!
'''

instructions_C = '''
Do 1 for 3000 reps and then HS holds of 10 minutes.

[macaca](https://macaca.life/)
'''


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = '{0}/study-media/{1}'.format(settings.MEDIA_ROOT, 'video1.mp4')
        media_path = '/study-media/{0}'.format('video1.mp4')
        copyfile('{0}/{1}'.format(settings.TESTDATA_DIR, 'test1.mp4'), path)
        video1, _ = StudyMedia.objects.get_or_create(name="The master movement", description=instructions_B)
        video1.video = media_path
        video1.save()
        video2, _ = StudyMedia.objects.get_or_create(name="The dumb movement", description=instructions_C)
        video2.video = media_path
        video2.save()
        video3, _ = StudyMedia.objects.get_or_create(name="The weirdo movement", description="Just do it!")
        video3.video = media_path
        video3.save()

        item_A1, _ = ActivityItem.objects.get_or_create(name="Coordination")
        item_A1.medias.add(video1)
        item_A1.medias.add(video2)

        item_B1, _ = ActivityItem.objects.get_or_create(name="Crab")
        item_B1.medias.add(video1)
        item_B2, _ = ActivityItem.objects.get_or_create(name="Step Behind")
        item_B2.medias.add(video2)
        item_B3, _ = ActivityItem.objects.get_or_create(name="Cossack Insertion")
        item_B3.medias.add(video1)
        item_B4, _ = ActivityItem.objects.get_or_create(name="Lizard")
        item_B4.medias.add(video2)
        item_B5, _ = ActivityItem.objects.get_or_create(name="L-sit Rotacional")
        item_B5.medias.add(video3)
        item_B6, _ = ActivityItem.objects.get_or_create(name="QDR")
        item_B6.medias.add(video1)
        item_B6.medias.add(video2)
        item_B6.medias.add(video3)
        item_C1, _ = ActivityItem.objects.get_or_create(name="Flexão de Punho")
        item_B2.medias.add(video1)
        item_C2, _ = ActivityItem.objects.get_or_create(name="Extensão de Punho")
        item_B2.medias.add(video2)

        activity_1, _ = Activity.objects.get_or_create(name="Would you dare?", instructions=instructions_A)
        activity_1.items.add(item_A1)
        activity_2, _ = Activity.objects.get_or_create(name="Locomotion", instructions=instructions_B)
        activity_2.items.add(item_B1)
        activity_2.items.add(item_B2)
        activity_2.items.add(item_B3)
        activity_2.items.add(item_B4)
        activity_2.items.add(item_B5)
        activity_2.items.add(item_B6)
        activity_3, _ = Activity.objects.get_or_create(name="Handstand", instructions=instructions_C)
        activity_3.items.add(item_C1)
        activity_3.items.add(item_C2)
