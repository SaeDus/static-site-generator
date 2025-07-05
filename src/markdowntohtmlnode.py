from blocksplitter import markdown_to_blocks
from blocktyping import BlockType, block_to_block_type

from parentnode import ParentNode
from leafnode import LeafNode

from textnode import TextNode, text_to_html_node
from texttotextnode import text_to_textnodes

def extract_title(markdown):
    for block in markdown_to_blocks(markdown):
        if block.startswith("# "):
            return block[2:]
    raise Exception("Error: No title found in markdown")

def markdown_to_html_node(markdown):
    html_nodes = []
    for block in markdown_to_blocks(markdown):
        html_nodes.append(block_to_html_nodes(block))
    return ParentNode("div", html_nodes)

def block_to_html_nodes(block):
    sub_nodes = []
    match block_to_block_type(block):
        case BlockType.PARAGRAPH:
            for line in block.split("\n"):
                sub_nodes.append(ParentNode(None, text_to_leaf_nodes(line)))
            return ParentNode("p", sub_nodes)

        case BlockType.HEADING:
            split_lines = block.split("\n")
            i = split_lines[0].find(" ")
            split_lines[0] = split_lines[0][i + 1:]

            for line in split_lines:
                sub_nodes.append(ParentNode(None, text_to_leaf_nodes(line)))
            return ParentNode(f"h{i}", sub_nodes)

        case BlockType.CODE:
            split_lines = block.split("\n")
            split_lines[0] = split_lines[0][3:]
            split_lines[-1] = split_lines[-1][:-3]

            full_text = ""
            for i in range(len(split_lines)):
                if not split_lines[i]:
                    continue

                full_text += split_lines[i]

                if i < len(split_lines) - 1:
                    full_text += "\n"

            return ParentNode("pre", [LeafNode("code", full_text)])

        case BlockType.QUOTE:
            split_lines = block.split("\n")
            split_lines[0] = split_lines[0][1:].strip()
            for line in split_lines:
                sub_nodes.append(ParentNode(None, text_to_leaf_nodes(line)))
            return ParentNode("blockquote", sub_nodes)

        case BlockType.UNORDERED_LIST:
            for line in block.split("\n"):
                line = line[2:]
                sub_nodes.append(ParentNode("li", text_to_leaf_nodes(line)))
            return ParentNode("ul", sub_nodes)

        case BlockType.ORDERED_LIST:
            for line in block.split("\n"):
                line = line[3:]
                sub_nodes.append(ParentNode("li", text_to_leaf_nodes(line)))
            return ParentNode("ol", sub_nodes)
        
        case _:
            raise ValueError("Error: BlockType not found")

def text_to_leaf_nodes(text):
    leaf_nodes = []
    for node in text_to_textnodes(text):
        leaf_nodes.append(text_to_html_node(node))
    return leaf_nodes

def text_to_code_nodes(text):
    return LeafNode(None, text)
