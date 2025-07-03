import unittest

from textnode import TextType, TextNode
from nodedelimiter import split_nodes_delimiter

class TestNodeDelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is **bold** in the middle.", TextType.TEXT)
        expectation = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" in the middle.", TextType.TEXT),
        ]
        split_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(split_nodes, expectation)
    
    def test_code(self):
        node = TextNode("Example: `return x + y` like that.", TextType.TEXT)
        expectation = [
            TextNode("Example: ", TextType.TEXT),
            TextNode("return x + y", TextType.CODE),
            TextNode(" like that.", TextType.TEXT),
        ]
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(split_nodes, expectation)
    
    def test_italic(self):
        node = TextNode("Some _emphasis_ on words.", TextType.TEXT)
        expectation = [
            TextNode("Some ", TextType.TEXT),
            TextNode("emphasis", TextType.ITALIC),
            TextNode(" on words.", TextType.TEXT),
        ]
        split_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(split_nodes, expectation)
    
    def test_instant_delimiter(self):
        node = TextNode("*Starting* with bold text is mean.", TextType.TEXT)
        expectation = [
            TextNode("Starting", TextType.BOLD),
            TextNode(" with bold text is mean.", TextType.TEXT)
        ]
        split_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(split_nodes, expectation)
    
    def test_multiple_nodes(self):
        node_a = TextNode("Some *bold* text.", TextType.TEXT)
        node_b = TextNode("More *bold* text.", TextType.TEXT)
        expectation = [
            TextNode("Some ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
            TextNode("More ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        split_nodes = split_nodes_delimiter([node_a, node_b], "*", TextType.BOLD)
        self.assertEqual(split_nodes, expectation)
    
    def test_imbalanced_delimiter(self):
        node = TextNode("This has no** bold delimiter.", TextType.TEXT)
        expectation = [TextNode("This has no** bold delimiter.", TextType.TEXT)]
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, expectation)
    
    def test_too_many_delimiters(self):
        node = TextNode("This _has__too_ many _delimiters_", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This ", TextType.TEXT),
                TextNode("has", TextType.ITALIC),
                TextNode("too", TextType.ITALIC),
                TextNode(" many ", TextType.TEXT),
                TextNode("delimiters", TextType.ITALIC),
            ],
            result,
        )
