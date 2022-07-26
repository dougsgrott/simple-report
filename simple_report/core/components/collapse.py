import uuid
from jinja2 import Environment, FileSystemLoader

from simple_report.core.components.base import BaseElement

env = Environment(loader=FileSystemLoader('simple_report/structure/html/templates'))


class Collapse(BaseElement):
    def __init__(self, use_panel, toggle_text, content, **kwargs):
        self.use_panel = use_panel
        self.toggle_text = toggle_text
        self.content = content

    def to_html(self):
        toggle_btn_id = uuid.uuid4().hex[:10].upper()
        content = {
            'use_panel': self.use_panel,
            'anchor_id': toggle_btn_id,
            'toggle_text': self.toggle_text,
            'content': self.content
            }
        template = env.get_template('collapse.html')
        rendered_template = template.render(content)
        return rendered_template