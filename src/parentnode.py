from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if self.children is None:
            raise ValueError("Error: Parent node must have children")
        
        html_string = ""

        for i in range(len(self.children)):
            node = self.children[i]
            html_string += node.to_html()
            if i < len(self.children) - 1:
                if node.tag is None and self.children[i + 1].tag is None:
                    html_string += " "
        
        if self.tag is None:
            return html_string
        
        return f'<{self.tag}>{html_string}</{self.tag}>'