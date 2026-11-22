"""Glyph extraction helpers: embedded CFF fonts -> SVG path data."""
import pymupdf, io
from fontTools.cffLib import CFFFontSet
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

class FontBank:
    def __init__(self, pdf):
        self.doc = pymupdf.open(pdf)
        self.fonts = {}
        for pno in range(len(self.doc)):
            for f in self.doc[pno].get_fonts(full=True):
                base = f[3].split('+')[-1]
                if base.startswith('TT') and base not in self.fonts:
                    buf = self.doc.extract_font(f[0])[3]
                    cff = CFFFontSet(); cff.decompile(io.BytesIO(buf), None)
                    td = cff[cff.fontNames[0]]
                    self.fonts[base] = td
    def glyph(self, font, gid):
        td = self.fonts[font]
        name = td.charset[gid]
        cs = td.CharStrings[name]
        bp = BoundsPen(None); cs.draw(bp)
        sp = SVGPathPen(None)
        cs.draw(TransformPen(sp, (1, 0, 0, -1, 0, 0)))   # flip y: SVG down
        b = bp.bounds  # font units, y up
        return dict(name=name, d=sp.getCommands(), bounds=b, fontmatrix=list(td.FontMatrix))
