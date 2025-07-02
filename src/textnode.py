from enum import Enum

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

def text_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(
                tag="a",
                value=text_node.text,
                props={ "href": text_node.url }
            )
        case TextType.IMAGE:
            return LeafNode(
                tag="img", 
                value="", 
                props={
                    "src": text_node.url,
                    "alt": text_node.text
                }
            )
        case _:
            raise ValueError("Error: TextNode must have a TextType")

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, node):
        return (
            node.text == self.text
            and node.text_type == self.text_type
            and node.url == self.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
