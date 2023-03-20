text = """
%% !TeX root = ../book.tex
%% !TeX spellcheck = fr_FR
%% !TeX encoding = ISO-8859-1

\section{}


\\begin{figure}[htb]
	\centering
	\includegraphics[width=0.85\linewidth]{B/imagesB/B%02d-01.pdf}
	\caption{}
	\label{fig:B%02d-1}
\end{figure}

\clearpage
"""


for i in range(1,25):
    with open("B%02d.tex" % i, "w") as f:
        f.write(text % (i,i))



    