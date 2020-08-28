from django.test import TestCase
from study.models import StudyMedia, ActivityItem, Activity

instructions_A = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam varius
nisi vitae enim efficitur viverra. Nunc maximus vulputate nibh quis efficitur.
Praesent porttitor nulla in condimentum varius. Etiam aliquet ligula libero.
Pellentesque vel nisl luctus, molestie ligula sit amet, accumsan nunc.
Pellentesque vulputate diam mi, sed tempor diam condimentum nec. Nam elementum
fermentum felis, sed mattis ante facilisis at. Maecenas sit amet enim quis
ante vulputate egestas id nec risus. Nam ac eros vel massa semper vulputate
nec in ante. In consectetur dapibus porta. Aenean ultricies dictum ante id
aliquam. Curabitur vel laoreet quam, et rhoncus dui.
'''


class StudyModelsTest(TestCase):

    def test_activity_creation(self):
        media_1 = StudyMedia.objects.create(name="The master movement", description="Just do it!")
        self.assertTrue(isinstance(media_1, StudyMedia))
        self.assertEqual(media_1.name, "The master movement")
        self.assertEqual(media_1.description, "Just do it!")

        item_A = ActivityItem.objects.create(name="Coordination")
        item_A.medias.add(media_1)
        self.assertTrue(isinstance(item_A, ActivityItem))
        self.assertEqual(item_A.name, "Coordination")

        activity = Activity.objects.create(name="Would you dare?", instructions=instructions_A)
        activity.items.add(item_A)
        self.assertTrue(isinstance(activity, Activity))
        self.assertEqual(activity.name, "Would you dare?")
        self.assertEqual(activity.instructions, instructions_A)
