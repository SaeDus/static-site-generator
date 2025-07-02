import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prop_to_html(self):
        test_prop = {
            "href": "https://www.boot.dev",
            "target": "_blank",
        }
        node = HTMLNode(props=test_prop)
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')
    
    def test_empty_value(self):
        node = HTMLNode()
        self.assertEqual(node.value, None)
    
    def test_tag(self):
        node = HTMLNode(tag="Just a line of text")
        self.assertEqual(node.tag, "Just a line of text")

if __name__ == "__main__":
    unittest.main()
