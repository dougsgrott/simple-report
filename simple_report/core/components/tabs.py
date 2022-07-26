import uuid
from jinja2 import Environment, FileSystemLoader

from simple_report.core.components.base import BaseElement

env = Environment(loader=FileSystemLoader('simple_report/structure/html/templates'))


class Tabs(BaseElement):
    def __init__(self, content, use_tabs, **kwargs):
        super().__init__(**kwargs)
        self.use_tabs = use_tabs
        self.content = dict()
        for name, value in content.items():
            self.content[name] = value if isinstance(value, list) else [value]

    def to_html(self):
        tabs_id = uuid.uuid4().hex[:10].upper()
        content = {
            'use_tabs': self.use_tabs,
            'anchor_id': tabs_id,
            'content': self.content,
            'tabs_id': tabs_id,
            }
        template = env.get_template('tabs.html')
        rendered_template = template.render(content, enumerate=enumerate)
        return rendered_template