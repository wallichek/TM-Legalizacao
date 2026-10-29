#!/usr/bin/env python3
"""Renderiza telas HTML (1080x1350) em JPG e confere estouro da zona segura.

Uso:  python3 render.py <pasta_html> <pasta_saida> [prefixo]
  - <pasta_html>: arquivos 01.html, 02.html... (ordem alfabética = ordem do carrossel)
  - <pasta_saida>: recebe prefixo-01.jpg, prefixo-02.jpg... e contato.png
Saída: lista de problemas. Código de saída 1 se houver ESTOURO.

Requer: playwright (Python) com Chromium e Pillow.
"""
import sys, pathlib

def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2])
    prefix = sys.argv[3] if len(sys.argv) > 3 else "tela"
    out.mkdir(parents=True, exist_ok=True)
    files = sorted(src.glob("*.html"))
    if not files:
        print("Nenhum .html em", src); sys.exit(2)

    from playwright.sync_api import sync_playwright
    from PIL import Image

    problems, shots = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i, f in enumerate(files, 1):
            pg.goto(f.resolve().as_uri(), wait_until="networkidle")
            pg.evaluate("document.fonts.ready")
            info = pg.evaluate("""() => {
              const b = document.querySelector('.body');
              if (!b) return {semBody: true};
              const r = {sh: b.scrollHeight, ch: b.clientHeight, sw: b.scrollWidth, cw: b.clientWidth};
              const fonte = document.fonts.check('700 40px Montserrat');
              return {...r, fonte};
            }""")
            name = f"{prefix}-{i:02d}"
            png = out / f"{name}.png"
            pg.screenshot(path=str(png))
            jpg = out / f"{name}.jpg"
            Image.open(png).convert("RGB").save(jpg, quality=92)
            png.unlink()
            shots.append(jpg)
            if info.get("semBody"):
                problems.append(f"{f.name}: sem <main class=\"body\"> — fora do modelo")
            else:
                if info["sh"] > info["ch"] + 1:
                    problems.append(f"{f.name}: ESTOURO vertical ({info['sh']}px de conteúdo em {info['ch']}px) — reduza texto/fonte")
                if info["sw"] > info["cw"] + 1:
                    problems.append(f"{f.name}: ESTOURO horizontal ({info['sw']}px em {info['cw']}px)")
                if not info.get("fonte"):
                    problems.append(f"{f.name}: Montserrat não carregou (sem internet?) — conferir visual")
        b.close()

    # Folha de contato
    th = [Image.open(s).resize((432, 540)) for s in shots]
    cols = min(4, len(th)); rows = (len(th) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 442 - 10, rows * 550 - 10), "#333333")
    for k, im in enumerate(th):
        sheet.paste(im, ((k % cols) * 442, (k // cols) * 550))
    sheet.save(out / "contato.png")

    print(f"{len(shots)} telas renderizadas em {out}")
    if problems:
        print("PROBLEMAS:"); [print(" -", x) for x in problems]
        sys.exit(1 if any("ESTOURO" in x for x in problems) else 0)
    print("OK — nenhuma tela estourou a zona segura.")

if __name__ == "__main__":
    main()
