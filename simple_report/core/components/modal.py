import uuid
from jinja2 import Environment, FileSystemLoader

from simple_report.core.elements.base import BaseElement

env = Environment(loader=FileSystemLoader('simple_report/structure/html/templates'))


class Modal(BaseElement):
    def __init__(self, toggle_text, content, **kwargs):
        super().__init__(**kwargs) # Code only works with this
        self.toggle_text = toggle_text
        self.content = [content] if not isinstance(content, list) else content
        # From Copilot
        # self.id = uuid.uuid4().hex[:10].upper()
        # self.title = kwargs.get('title', '')
        # self.body = kwargs.get('body', '')
        # self.footer = kwargs.get('footer', '')

    def to_html(self):
        anchor_id = uuid.uuid4().hex[:10].upper()
        content = {
            'anchor_id': anchor_id,
            'toggle_text': self.toggle_text,
            'content': self.content
            }
        template = env.get_template('modal.html')
        rendered_template = template.render(content)
        return rendered_template