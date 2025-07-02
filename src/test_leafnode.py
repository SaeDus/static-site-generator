import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_href(self):
        test_prop = {
            "href": "https://www.boot.dev",
        }
        node = LeafNode("a", "Click me!", test_prop)
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">Click me!</a>')
    
    def test_value_only(self):
        node = LeafNode(None, "Displaying text only")
        self.assertEqual(node.to_html(), "Displaying text only")

if __name__ == "__main__":
    unittest.main()
