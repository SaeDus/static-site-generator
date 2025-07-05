import unittest

from markdowntohtmlnode import markdown_to_html_node, block_to_html_nodes, extract_title
from parentnode import ParentNode
from leafnode import LeafNode

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_markdown_to_html_node(self):
        self.maxDiff = None
        md = """
# This is a header

### With a subtitle

>Insert inspirational quote

As you can see in this **intense** markdown block
I have inserted _many_ elements that make no sense
Including the need to throw in `some code` too

```coding intensifies```

- oh yeah
- almost forgot
- this **is** a list
- that is _unordered_

1. this list
2. is ordered
3. and _if_ I wanted to
4. I **could**...
5. or...
6. I could do the **other** thing...

k thx bye
"""
        node = markdown_to_html_node(md).to_html()
        self.assertEqual(
            node,
            '<div><h1>This is a header</h1><h3>With a subtitle</h3><blockquote>Insert inspirational quote</blockquote><p>As you can see in this <b>intense</b> markdown block I have inserted <i>many</i> elements that make no sense Including the need to throw in <code>some code</code> too</p><pre><code>coding intensifies</code></pre><ul><li>oh yeah</li><li>almost forgot</li><li>this <b>is</b> a list</li><li>that is <i>unordered</i></li></ul><ol><li>this list</li><li>is ordered</li><li>and <i>if</i> I wanted to</li><li>I <b>could</b>...</li><li>or...</li><li>I could do the <b>other</b> thing...</li></ol><p>k thx bye</p></div>',
        )
    
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_title_extraction(self):
        md = """
# Title Goes Here

### Maybe Other Stuff

Here is some basic text
"""
        self.assertEqual("Title Goes Here", extract_title(md))