import unittest
from unittest.mock import patch
from main import get_doc_shelf, delete_doc, add_new_doc, append_doc_to_shelf

class TestFunctions(unittest.TestCase):

    @patch('builtins.input', side_effect=['T000001', 'Test doc', 'Alexey', 2])
    def test_add_new_doc(self, mock_inputs):
        new_doc_shelf_number = add_new_doc()
        self.assertEqual(new_doc_shelf_number, 2)

    @patch('builtins.input', side_effect=['10006'])
    def test_get_doc_shelf(self, mock_inputs):
        directory_number = get_doc_shelf()
        self.assertEqual(directory_number, '2')

    @patch('builtins.input', side_effect=['11-2'])
    def test_delete_doc(self, mock_inputs):
        doc_number, deleted = delete_doc()
        self.assertEqual(deleted, True)