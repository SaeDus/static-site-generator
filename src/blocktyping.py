from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(text):
    if text.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if text.startswith("```") and text.endswith("```"):
        return BlockType.CODE
    
    split_text = text.split("\n")

    is_quote = True
    for q in split_text:
        if not q.startswith(">"):
            is_quote = False
            break
    
    if is_quote:
        return BlockType.QUOTE

    is_unordered_list = True
    for line in split_text:
        if not line.startswith("- "):
            is_unordered_list = False
            break
    
    if is_unordered_list:
        return BlockType.UNORDERED_LIST
    
    is_ordered_list = True
    for i in range(len(split_text)):
        if not split_text[i].startswith(f"{i + 1}. "):
            is_ordered_list = False
    
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH