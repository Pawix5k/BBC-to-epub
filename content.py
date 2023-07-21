from bs4 import BeautifulSoup, NavigableString
import requests

from config import TEMP_DIR


STANDARD_TAGS = ["h1", "h2", "h3", "h4", "h5", "p"]
FIGURE_TAG = "figure"
ALLOWED_ATTRS = ["src"]

class Content:
    def __init__(self, title, links):
        self.title = title
        self.links = links
        self.content = self._get_articles_contents()
    

    def _get_articles_contents(self):
        site_contents = []
        for link in self.links:
            site_contents.append(SiteContent(link))


class SiteContent:
    def __init__(self, link):
        self.link = link
        site_content = self._get_site_content()
        self.lang = self._extract_lang(site_content)
        self.is_rtl = self._check_if_rtl(site_content)
        self.content = self._extract_content(site_content)
        img_links = self._extract_img_links()
        self._download_imgs(img_links)
        self.temp_save_to_file()
    
    def _get_html(self):
        # temporary to avoid making requests
        with open(r"playground\sample_art.html", "r", encoding="utf8") as f:
            html = f.read()
        return html
    
    def _get_site_content(self):
        html = self._get_html()
        return BeautifulSoup(html, "html.parser")
    
    def _extract_lang(self, soup):
        return soup.html["lang"]

    def _check_if_rtl(self, soup):
        if "dir" in soup.html and soup.html["dir"] == "rtl":
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
                        figure.append(figcaption)
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
    
    def _extract_img_links(self):
        links = []
        for descendant in self.content.descendants:
            if isinstance(descendant, NavigableString):
                continue
            if descendant.name == "img":
                links.append(descendant["src"])
        return links

    def _download_imgs(self, img_links):
        for link in img_links:
            file_name = link.split("/")[-1]
            with open(TEMP_DIR / file_name, 'wb') as f:
                f.write(requests.get(link).content)
    
    def temp_save_to_file(self):
        with open(r"playground/temp.html", "w", encoding="utf8") as f:
            f.write(str(self.content))


