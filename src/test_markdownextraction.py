import unittest

from markdownextraction import extract_markdown_images, extract_markdown_links

class TextMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        line = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        result = extract_markdown_images(line)
        self.assertEqual(result, expected)

    def test_false_markdown_image_text(self):
        line = "This is text with a false ![rick roll]in(https://www.boot.dev) or [bootdev](https://www.boot.dev)"
        result = extract_markdown_images(line)
        self.assertEqual(result, [])
    
    def test_extract_markdown_links(self):
        line = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        result = extract_markdown_links(line)
        self.assertEqual(result, expected)
    
    def test_false_markdown_link_text(self):
        line = "This text includes ![bootdev](https://www.boot.dev) or even [not]actually(an image)"
        result = extract_markdown_links(line)
        self.assertEqual(result, [])