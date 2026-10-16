#!/usr/bin/env python3
"""Compile tikz figures from tex-src/main.tex to PNGs in computo/figures/.

Each `\\begin{figure}...\\begin{tikzpicture}...\\end{tikzpicture}...\\label{fig:NAME}...\\end{figure}`
block is extracted, wrapped in a standalone LaTeX document, compiled with pdflatex,
and converted to a PNG via pdftocairo. Output: computo/figures/fig-NAME.png.

Re-run after any change to the tikz source in tex-src/main.tex.
"""
import re
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).parent
TEX_SRC = HERE.parent / 'tex-src' / 'main.tex'
OUT_DIR = HERE / 'figures'
OUT_DIR.mkdir(exist_ok=True)

TIKZ_LIBS = 'arrows.meta,positioning,fit,backgrounds,shapes.geometric'
DPI = 200

STANDALONE_TEMPLATE = r"""\documentclass[tikz, border=4pt]{standalone}
\usepackage{amsmath,amssymb}
\usetikzlibrary{""" + TIKZ_LIBS + r"""}
\begin{document}
%s
\end{document}
"""

fig_pat = re.compile(
    r'\\begin\{figure\}.*?'
    r'(\\begin\{tikzpicture\}.*?\\end\{tikzpicture\})'
    r'.*?\\label\{fig:([a-zA-Z0-9_-]+)\}',
    re.DOTALL,
)

tex = TEX_SRC.read_text()
figures = list(fig_pat.finditer(tex))
if not figures:
    raise SystemExit(f"No tikz figures found in {TEX_SRC}")

for m in figures:
    tikz_body, label = m.group(1), m.group(2)
    tex_content = STANDALONE_TEMPLATE % tikz_body
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        tex_file = tmp_path / 'fig.tex'
        tex_file.write_text(tex_content)
        res = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-output-directory', tmp, str(tex_file)],
            capture_output=True, text=True,
        )
        pdf_file = tmp_path / 'fig.pdf'
        if not pdf_file.exists():
            print(f"pdflatex failed for fig-{label}:\n{res.stdout[-1500:]}")
            raise SystemExit(1)
        out_png = OUT_DIR / f'fig-{label}'
        subprocess.run(
            ['pdftocairo', '-png', '-r', str(DPI), '-singlefile', str(pdf_file), str(out_png)],
            check=True,
        )
    print(f"compiled: {out_png}.png")
