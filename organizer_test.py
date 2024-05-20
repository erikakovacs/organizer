import unittest
import organizer

class BasicTestCase(unittest.TestCase):
    def test_add_task(self):
        tasks = []                                                                   
        organizer.add_task_to_list(tasks,"20/12/2038","Dzsoki")
        self.assertTrue({"task" : "Dzsoki", "date" : "20/12/2038"} in tasks)

    def test_format_validation(self):
        tasks = []                                                                   
        with self.assertRaises(ValueError): 
            organizer.add_task_to_list(tasks,"20-12-2038","Dzsoki")

    def test_not_before_validation(self):
        tasks = []                                                                   
        with self.assertRaises(ValueError): 
            organizer.add_task_to_list(tasks,"20/12/2012","Dzsoki")
            
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
