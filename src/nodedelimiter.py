from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final_nodes = []
    for i in old_nodes:
        if i.text_type != TextType.TEXT:
            final_nodes.append(i)
            continue
        
        if not i.text:
            continue
        
        new_nodes = []
        split_text = i.text.split(delimiter)

        if len(split_text) == 1:
            final_nodes.append(i)
            continue

        if len(split_text) % 2 == 0:
            final_nodes.append(i)
            continue
        
        is_text_type = True
        for s in split_text:
            if len(s) == 0:
                is_text_type = not is_text_type
                continue
            
            next_type = TextType.TEXT if is_text_type else text_type
            new_nodes.append(TextNode(text=s, text_type=next_type))
            is_text_type = not is_text_type
        
        final_nodes.extend(new_nodes)

    return final_nodes