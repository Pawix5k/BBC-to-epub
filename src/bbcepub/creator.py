import os
import shutil
import tempfile
from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape

from bbcepub.content import Content


class Creator:
    def __init__(self, title: str, urls: list[str], tmp_dir):
        self.title = title
        self.tmp_dir = tmp_dir
        self.content = Content(title, urls, tmp_dir)
        self.tmp_dir = tmp_dir
        self.staging_dir = tmp_dir / title
        self.img_dir = self.content.img_dir
        self.static_dir = Path(os.path.dirname(__file__)) / "static"

    def _copy_static(self):
        shutil.copytree(self.static_dir, self.staging_dir)
    
    def _copy_img(self):
        shutil.copytree(self.img_dir, self.staging_dir / "img")
    
    def _create_articles_htmls(self, env):
        template = env.get_template("content.html")
        for article in self.content.articles:
            with open(self.staging_dir / rf"{article.file_name}.html", "w", encoding="utf8") as f:
                f.write(template.render(article_content=article))
    
    def _create_content_opf(self, env):
        template = env.get_template("content.opf")
        with open(self.staging_dir / "content.opf", "w", encoding="utf8") as f:
                f.write(template.render(content=self.content))
    
    def _create_toc_ncx(self, env):
        template = env.get_template("toc.ncx")
        with open(self.staging_dir / "toc.ncx", "w", encoding="utf8") as f:
                f.write(template.render(content=self.content))

    def create_epub(self):
        env = Environment(
            loader=PackageLoader("bbcepub"),
            autoescape=select_autoescape()
        )
        self._copy_static()
        self._copy_img()
        self._create_articles_htmls(env)
        self._create_content_opf(env)
        self._create_toc_ncx(env)
        shutil.make_archive(self.tmp_dir / self.content.title, 'zip',  root_dir=self.staging_dir)
        shutil.copy(self.tmp_dir / (self.content.title + ".zip"), Path(self.content.title + ".epub"))
        print(f"Created '{self.title}.epub'")
        # clear_temp_dirs()


def create_epub(filename, links):
    with tempfile.TemporaryDirectory() as tmp_dir:
        creator = Creator(filename, links, Path(tmp_dir))
        creator.create_epub()
