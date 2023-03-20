from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

drawing = svg2rlg("B08-01.svg")
renderPDF.drawToFile(drawing, "B08-01.pdf")