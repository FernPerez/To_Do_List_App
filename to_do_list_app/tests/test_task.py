from event_and_task import Task
import unittest

class Test_Task(unittest.TestCase):
    def test_important(self):
        task = Task()
        task.setTitle("Grocery Shopping")
        task.setDescription("Milk, Eggs, and Bread")
        task.setPriority("Important")
        task.setDate("04/22/2022")

        self.assertEqual(task.getTitle(), "Grocery Shopping")
        self.assertEqual(task.getDescription(), "Milk, Eggs, and Bread")
        self.assertEqual(task.getPriority(), "Important")
        self.assertEqual(task.getDate(), "04/22/2022")

    def test_unimportant(self):
        task = Task()
        task.setTitle("Buy Games")
        task.setDescription("New Lego Star Wars Game")
        task.setPriority("Unimportant")
        task.setDate("04/25/2022")

        self.assertEqual(task.getTitle(), "Buy Games")
        self.assertEqual(task.getDescription(), "New Lego Star Wars Game")
        self.assertEqual(task.getPriority(), "Unimportant")
        self.assertEqual(task.getDate(), "04/25/2022")

    def test_non_match(self):
        task = Task()
        task.setTitle("Buy Games")
        task.setDescription("New Lego Star Wars Game")
        task.setPriority("Unimportant")
        task.setDate("04/25/2022")

        self.assertNotEqual(task.getTitle(), "Grocery Shopping")
        self.assertNotEqual(task.getDescription(), "Milk, Eggs, and Bread")
        self.assertNotEqual(task.getPriority(), "Important")
        self.assertNotEqual(task.getDate(), "04/22/2022")



if __name__ == '__main__':
    unittest.main()
