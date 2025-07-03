import re

from textnode import TextType, TextNode

def split_nodes_image(old_nodes):
    final_nodes = []
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_nodes.extend([node])
            continue
            
        if not node.text:
            final_nodes.extend([node])
            continue
        
        if not re.search(image_pattern, node.text):
            final_nodes.append(node)
            continue

        full_text = node.text
        pos = 0

        for match in re.finditer(image_pattern, full_text):
            start, end = match.span()
            alt = match.group(1)
            url = match.group(2)

            if start > pos:
                before = full_text[pos:start]
                if before:
                    final_nodes.append(TextNode(before, TextType.TEXT))
            
            final_nodes.append(TextNode(alt, TextType.IMAGE, url))

            pos = end

        if pos < len(full_text):
            after = full_text[pos:]
            if after:
                final_nodes.append(TextNode(after, TextType.TEXT))
    
    return final_nodes

def split_nodes_link(old_nodes):
    final_nodes = []
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_nodes.extend([node])
            continue
            
        if not node.text:
            final_nodes.extend([node])
            continue
        
        if not re.search(link_pattern, node.text):
            final_nodes.append(node)
            continue

        full_text = node.text
        pos = 0

        for match in re.finditer(link_pattern, full_text):
            start, end = match.span()
            alt = match.group(1)
            url = match.group(2)

            if start > pos:
                before = full_text[pos:start]
                if before:
                    final_nodes.append(TextNode(before, TextType.TEXT))
            
            final_nodes.append(TextNode(alt, TextType.LINK, url))

            pos = end
        
        if pos < len(full_text):
            after = full_text[pos:]
            if after:
                final_nodes.append(TextNode(after, TextType.TEXT))
    
    return final_nodes
