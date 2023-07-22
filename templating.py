from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("main"),
    autoescape=select_autoescape()
)

template = env.get_template("toc.ncx")

print(template.render(title="SAMPLE_TITLE", articles=["a1", "ART2"]))
