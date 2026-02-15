import os
import shutil
from datetime import datetime
import marko
import frontmatter
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader(searchpath='./templates'),
)


def parse_section(section_path: str) -> str:
    """Renders section.
    """
    section = frontmatter.load(section_path)
    return {
        'title': section.get('title'),
        'start_date': section.get('start_date'),
        'end_date': section.get('end_date'),
        'content': marko.convert(section.content),
    }

def render_site(sections_dir: str = './sections'):
    """Renders site.
    """
    # Build sections
    section_fnames = os.listdir(sections_dir)
    section_fnames.sort()
    section_fnames = section_fnames[::-1]
    sections = []
    for fname in section_fnames:
        sections.append(parse_section(os.path.join(sections_dir, fname)))

    # Render index
    template = env.get_template('index.html')
    return template.render(sections=sections)


def build(build_dir: str = './build'):
    """Builds site.
    """

    # Create build directory
    if not os.path.exists(build_dir):
        os.mkdir(build_dir)

    # Render site
    with open(os.path.join(build_dir, 'index.html'), 'w') as f:
        f.write(render_site())

    # Copy static directory
    build_static_dir = os.path.join(build_dir, './static')
    if os.path.exists(build_static_dir):
        shutil.rmtree(build_static_dir)
    shutil.copytree('./static', build_static_dir)


if __name__ == '__main__':
    print("Starting build...")
    build()
    print("Done!")
