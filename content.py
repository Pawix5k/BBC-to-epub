from __future__ import annotations

from dataclasses import dataclass

from bs4 import BeautifulSoup, NavigableString
import requests

from config import TEMP_IMG_DIR

STANDARD_TAGS = ["h1", "h2", "h3", "h4", "h5", "p"]
FIGURE_TAG = "figure"
ALLOWED_ATTRS = ["src"]

@dataclass
class ImgLink:
    web_url: str
    local_url: str
    filename: str

class Content:
    def __init__(self, title, links):
        self.title = title
        self.links = links
        self.articles = self._get_articles_contents()
    
    def _get_articles_contents(self) -> list[ArticleContent]:
        articles = []
        for i, link in enumerate(self.links, 1):
            try:
                article = ArticleContent(link, i)
            except AttributeError:
                print(f"Article '{link}' seems to be incorrect, skipped.")
                continue
            articles.append(article)
        return articles

    def get_enumerated_img_links(self):
        return enumerate((link.local_url for article in self.articles for link in article.img_links), 1)


class ArticleContent:
    def __init__(self, link, i):
        self.i = i
        self.file_name = f"article_{str(i).zfill(3)}"
        self.link = link
        site_content = self._get_site_content()
        self.lang = self._extract_lang(site_content)
        self.is_rtl = self._check_if_rtl(site_content)
        self.content = self._extract_content(site_content)
        self.title = self._extract_title()
        self.img_links = self._get_and_update_img_links()
        self._download_imgs()
    
    def _get_html(self):
        return requests.get(self.link).text
    
    def _get_site_content(self):
        html = self._get_html()
        return BeautifulSoup(html, "html.parser")
    
    def _extract_lang(self, soup):
        return soup.html["lang"]

    def _extract_title(self):
        return self.content.find("h1").string

    def _check_if_rtl(self, soup):
        if "dir" in soup.html.attrs and soup.html["dir"] == "rtl":
            return True
        return False
    
    def _extract_content(self, soup: BeautifulSoup):
        elements = []
        container = soup.find("main")
        for child in container.children:
            if child.name != "div":
                continue
            for child_child in child.children:
                if child_child.name in STANDARD_TAGS:
                    elements.append(child_child)
                if child_child.name == FIGURE_TAG:
                    figure = soup.new_tag("figure")
                    img = child_child.find("img")
                    figcaption = child_child.find("figcaption")
                    figure.append(img)
                    if figcaption:
                        if figcaption.find("span", recursive=False):
                            figcaption.span.extract()
                        figure.append(figcaption.p)
                    elements.append(figure)
        body = soup.new_tag("body")
        if self.is_rtl:
            body["dir"] = "rtl"
            body["class"] = "rtl"
        body.extend(elements)

        for descendant in body.descendants:
            if isinstance(descendant, NavigableString):
                continue
            descendant.attrs = {k: v for k, v in descendant.attrs.items() if k in ALLOWED_ATTRS}

        return body

    def _download_imgs(self):
        for link in self.img_links:
            with open(TEMP_IMG_DIR / link.filename, 'wb') as f:
                f.write(requests.get(link.web_url).content)
    
    def _get_and_update_img_links(self):
        links = []
        for descendant in self.content.descendants:
            if isinstance(descendant, NavigableString):
                continue
            if descendant.name == "img":
                img_url = descendant["src"]
                img_filename = img_url.split("/")[-1]
                local_link = rf"img/{img_filename}"
                links.append(ImgLink(img_url, local_link, img_filename))
                descendant["src"] = local_link
        return links
