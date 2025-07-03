import unittest

from textnode import TextType, TextNode
from texttotextnode import text_to_textnodes

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_textnode(self):
        self.maxDiff = None
        test_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(test_text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            result,
        )
    
    def test_reordered_text(self):
        self.maxDiff = None
        test_text = "This is _really emphasized_ but not **completely** off the rails with `foo = bar` besides [link](https://boot.dev) and ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = text_to_textnodes(test_text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("really emphasized", TextType.ITALIC),
                TextNode(" but not ", TextType.TEXT),
                TextNode("completely", TextType.BOLD),
                TextNode(" off the rails with ", TextType.TEXT),
                TextNode("foo = bar", TextType.CODE),
                TextNode(" besides ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            result,
        )