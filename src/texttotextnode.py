from textnode import TextType, TextNode
from nodedelimiter import split_nodes_delimiter
from nodesplitter import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    input_nodes = [text_node]

    delimiters = (("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE))

    for d, t in delimiters:
        output_nodes = split_nodes_delimiter(input_nodes, d, t)
        input_nodes = output_nodes
    
    output_nodes = split_nodes_image(input_nodes)
    input_nodes = output_nodes

    return split_nodes_link(input_nodes)