from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Error: Parent node must have a tag")
        
        if self.children is None:
            raise ValueError("Error: Parent node must have children")
        
        html_string = ""
        
        for node in self.children:
            html_string += node.to_html()
        
        return f'<{self.tag}>{html_string}</{self.tag}>'