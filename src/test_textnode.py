import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertEqual(node.url, "https://boot.dev")
    
    def test_text_type(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        self.assertEqual(node.text_type, TextType.PLAIN)

if __name__ == "__main__":
    unittest.main()
