import sys
import os
import shutil
from textnode import TextNode, TextType
from markdowntohtmlnode import markdown_to_html_node, extract_title

def generate_page(src_dir, dst_dir):
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)

        print(f'Copying "{src_path}" -> "{dst_dir}"')

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_dir)
            continue

        target_dir = os.path.join(dst_dir, item)
        os.makedirs(target_dir)

        generate_page(src_path, target_dir)

def remove_directory_contents(target_dir):
    shutil.rmtree(target_dir)
    os.makedirs(target_dir)

def create_html_from_template(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    print(f"Reading file at {from_path}")
    with open(from_path, 'r', encoding='utf-8') as from_path_file:
        markdown = from_path_file.read()
    
    print(f"Reading template at {template_path}")
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template = template_file.read()
    
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    print(f"Writing to HTML at {dest_path}")
    with open(dest_path, 'w', encoding='utf-8') as dest_file:
        dest_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)

        if os.path.isdir(src_path):
            target_dir = os.path.join(dest_dir_path, item)
            os.makedirs(target_dir, exist_ok=True)
            generate_pages_recursive(src_path, template_path, target_dir, basepath)
            continue

        if not item.endswith(".md"):
            continue
        
        item_html = item.replace(".md", ".html")
        target_dest_dir = os.path.join(dest_dir_path, item_html)
        
        create_html_from_template(src_path, template_path, target_dest_dir, basepath)

def initialize_static_site():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    src_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(src_dir)

    public_path = os.path.join(project_root, "docs")
    static_path = os.path.join(project_root, "static")

    os.makedirs(public_path, exist_ok=True)

    remove_directory_contents(public_path)
    generate_page(static_path, public_path)

    content_path = os.path.join(project_root, "content")
    template_path = os.path.join(project_root, "template.html")
    dest_dir_path = os.path.join(project_root, "docs")

    generate_pages_recursive(content_path, template_path, dest_dir_path, basepath)

def main():
    initialize_static_site()

if __name__ == "__main__":
    main()
