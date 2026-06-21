from jinja2 import Template

def build_latex(results):

    template = open("paper_engine/template.tex").read()
    tex = Template(template).render(results=results)

    with open("output/csdfs.tex", "w") as f:
        f.write(tex)

    print("LaTeX generated.")
