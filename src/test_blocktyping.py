import unittest

from blocktyping import BlockType, block_to_block_type

class TestBlockTyping(unittest.TestCase):
    def test_heading_block(self):
        text = "# This is a heading"
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.HEADING)
    
    def test_false_heading_block(self):
        text = "#Not a heading"
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.PARAGRAPH)
    
    def test_code_block(self):
        text = "```entering some code```"
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.CODE)
    
    def test_false_code_block(self):
        text = "```not actually code"
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.PARAGRAPH)
    
    def test_quote_block(self):
        text = ">someone once said something"
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.QUOTE)
    
    def test_multiline_quote_block(self):
        text = ">someone said something\n>then said another thing"
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.QUOTE)
    
    def test_false_quote_block(self):
        text = "<not here though"
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.PARAGRAPH)
    
    def test_missed_quote_delimiter_block(self):
        text = ">blah blah blah\nand another thing..."
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.PARAGRAPH)
    
    def test_unordered_list_block(self):
        text = "- something\n- then another\n- don't forget this one"
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.UNORDERED_LIST)
    
    def test_false_unordered_list_block(self):
        text = "- something\n-- falsely typed\noops"
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.PARAGRAPH)
    
    def test_ordered_list_block(self):
        text = "1. one\n2. two\n3. three\n4. four"
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.ORDERED_LIST)
    
    def test_false_ordered_list_block(self):
        text = "1. one\n3. oops\n2. yeah...\n12. not in order"
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.PARAGRAPH)