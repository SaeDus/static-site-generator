import unittest

from blocksplitter import markdown_to_blocks

class TestBlockSplitter(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_too_many_gaps(self):
        md= """
This is **bold** text


Added a _gap_ to the string
Maybe a little `code` too




- a list
- with something
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bold** text",
                "Added a _gap_ to the string\nMaybe a little `code` too",
                "- a list\n- with something",
            ],
        )