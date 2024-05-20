import unittest
import organizer

class BasicTestCase(unittest.TestCase):
    def test_add_task(self):
        tasks = []                                                                   
        organizer.add_task_to_list(tasks,"Dzsoki")
        self.assertTrue("Dzsoki" in tasks)

    def test_delete_task(self):
        tasks = ["madár"]                                                                
        organizer.delete_task(tasks,0)
        self.assertTrue( "madár" not in tasks) 

    def test_modify_task_for_replace(self):
        tasks = ["madár"]                                                                
        organizer.modify_task(tasks,0, "kutya")
        self.assertTrue( "madár" not in tasks)
        self.assertTrue( "kutya" in tasks)

    def test_modify_task_for_wrong_number(self):
        tasks = ["Dzsoki"] 
        with self.assertRaises(ValueError):                                                               
            organizer.modify_task(tasks,"Dzsoki", "Jockey")

    def test_modify_task_for_wrong_task(self):
        tasks = ["madár"]                                                                
        with self.assertRaises(IndexError):                                                               
            organizer.modify_task(tasks,"9", "Jockey")      
