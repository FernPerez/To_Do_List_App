from event_builder import EventBuilder
import unittest

class TestEventBuilder(unittest.TestCase):
    def test_normal(self):
        event = EventBuilder().setTitle("Feed Dog").setDescription("He's Hungy").setPriority("Important").setDate("04/20/2069").build()

        self.assertEqual(event.getTitle(), "Feed Dog")
        self.assertEqual(event.getDescription(), "He's Hungy")
        self.assertEqual(event.getPriority(), "Important")
        self.assertEqual(event.getDate(), "04/20/2069")

if __name__ == '__main__':
    unittest.main()
