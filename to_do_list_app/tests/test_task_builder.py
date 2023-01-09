from task_builder import TaskBuilder
import unittest

class TestTaskBuilder(unittest.TestCase):
    def test_normal(self):
        task = TaskBuilder().setTitle("Feed Dog").setDescription("He's Hungy").setPriority("Important").setDate("04/20/2069").build()

        self.assertEqual(task.getTitle(), "Feed Dog")
        self.assertEqual(task.getDescription(), "He's Hungy")
        self.assertEqual(task.getPriority(), "Important")
        self.assertEqual(task.getDate(), "04/20/2069")

if __name__ == '__main__':
    unittest.main()
