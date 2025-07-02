import unittest

from textnode import TextNode, TextType, text_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertEqual(node.url, "https://boot.dev")
    
    def test_text_type(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.text_type, TextType.TEXT)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_code(self):
        node = TextNode("i = 4", TextType.CODE)
        html_node = text_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>i = 4</code>")
    
    def test_link(self):
        node = TextNode("bootdev", TextType.LINK, "https://www.boot.dev")
        html_node = text_to_html_node(node)
        self.assertEqual(
            html_node.to_html(), 
            '<a href="https://www.boot.dev">bootdev</a>'
        )

if __name__ == "__main__":
    unittest.main()
