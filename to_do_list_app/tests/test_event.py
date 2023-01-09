from event_and_task import Event
import unittest

class TestEvent(unittest.TestCase):
    def test_important(self):
        event = Event()
        event.setTitle("Party at Stacy's")
        event.setDescription(
            "Gotta be there!"
        )
        event.setDate("04/20/2022")
        event.setPriority("Important")

        self.assertEqual(event.getTitle(), "Party at Stacy's")
        self.assertEqual(event.getDescription(), "Gotta be there!")
        self.assertEqual(event.getDate(), "04/20/2022")
        self.assertEqual(event.getPriority(), "Important")

    def test_unimportant(self):
        event = Event()
        event.setTitle("Neighborhood Get-Together")
        event.setDescription(
            "Meet up at the park at 6:00 pm"
        )
        event.setDate("04/25/2022")
        event.setPriority("Unimportant")

        self.assertEqual(event.getTitle(), "Neighborhood Get-Together")
        self.assertEqual(event.getDescription(), "Meet up at the park at 6:00 pm")
        self.assertEqual(event.getDate(), "04/25/2022")
        self.assertEqual(event.getPriority(), "Unimportant")

    def test_non_match(self):
        event = Event()
        event.setTitle("Neighborhood Get-Together")
        event.setDescription(
            "Meet up at the park at 6:00 pm"
        )
        event.setDate("04/25/2022")
        event.setPriority("Unimportant")

        self.assertNotEqual(event.getTitle(), "Party at Stacy's")
        self.assertNotEqual(event.getDescription(), "Gotta be there!")
        self.assertNotEqual(event.getDate(), "04/20/2022")
        self.assertNotEqual(event.getPriority(), "Important")

if __name__ == '__main__':
    unittest.main()
