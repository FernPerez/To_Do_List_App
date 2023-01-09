from activity_builder import ActivityBuilder
import unittest

class TestActivityBuilder(unittest.TestCase):
    def test_normal(self):
        activity = ActivityBuilder().setTitle("Feed Dog").setDescription("He's Hungy").setPriority("Important").setDate("04/20/2069").build()

        self.assertEqual(activity.getTitle(), "Feed Dog")
        self.assertEqual(activity.getDescription(), "He's Hungy")
        self.assertEqual(activity.getPriority(), "Important")
        self.assertEqual(activity.getDate(), "04/20/2069")

if __name__ == '__main__':
    unittest.main()
