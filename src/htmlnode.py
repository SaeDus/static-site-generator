class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Error: Node not implemented")
    
    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return
        
        attributes = list(self.props.keys())
        text = list(self.props.values())

        html_string = ""

        for key, value in self.props.items():
            html_string += f' {key}="{value}"'
        
        return html_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
