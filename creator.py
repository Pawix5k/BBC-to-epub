import shutil
from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape

from config import TEMP_DIR
from content import Content


class Creator:
    def __init__(self, content: Content):
        self.content = content
        self.output_path = TEMP_DIR / content.title

    def _copy_static(self):
        shutil.copytree(r"static", self.output_path)
    
    def _create_articles_htmls(self, env):
        template = env.get_template("content.html")
        for article in self.content.articles:
            with open(self.output_path / rf"{article.file_name}.html", "w", encoding="utf8") as f:
                f.write(template.render(article_content=article))
    
    def _create_content_opf(self, env):
        template = env.get_template("content.opf")
        with open(self.output_path / "content.opf", "w", encoding="utf8") as f:
                f.write(template.render(content=self.content))
    
    def _create_toc_ncx(self, env):
        template = env.get_template("toc.ncx")
        with open(self.output_path / "toc.ncx", "w", encoding="utf8") as f:
                f.write(template.render(content=self.content))

    def create_epub(self):
        env = Environment(
            loader=PackageLoader("main"),
            autoescape=select_autoescape()
        )
        shutil.rmtree(TEMP_DIR)
        self._copy_static()
        self._create_articles_htmls(env)
        self._create_content_opf(env)
        self._create_toc_ncx(env)
