import shutil
import os

from jinja2 import Environment, PackageLoader, select_autoescape

from bbcepub.config import TEMP_DIR, TEMP_IMG_DIR, OUTPUT_DIR
from bbcepub.content import Content
from bbcepub.utils import clear_temp_dirs


class Creator:
    def __init__(self, title: str, urls: list[str]):
        clear_temp_dirs()
        self.title = title
        self.content = Content(title, urls)
        self.output_path = TEMP_DIR / title
    
    def _remove_old_imgs(self):
        for file in os.listdir(TEMP_IMG_DIR):
            os.remove(TEMP_IMG_DIR / file)

    def _copy_static(self):
        shutil.copytree(r"static", self.output_path)
    
    def _copy_img(self):
        shutil.copytree(TEMP_IMG_DIR, self.output_path / "img")
    
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
        self._copy_static()
        self._copy_img()
        self._create_articles_htmls(env)
        self._create_content_opf(env)
        self._create_toc_ncx(env)
        shutil.make_archive(TEMP_DIR / self.content.title, 'zip',  root_dir=self.output_path)
        shutil.copy(TEMP_DIR / (self.content.title + ".zip"), OUTPUT_DIR / (self.content.title + ".epub"))
        print(f"Created '{self.title}.epub' in '{OUTPUT_DIR}'")
        clear_temp_dirs()
