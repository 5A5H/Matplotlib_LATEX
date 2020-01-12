## Import
import pathlib
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Setup Matplotlib for Latex
matplotlib.use("pgf")
matplotlib.rcParams.update({
    'text.latex.preamble': r"\usepackage{lmodern}",
    "pgf.texsystem": "pdflatex",
    'font.family': 'lmodern',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'font.size': 12.0
})

## Set Values
X_I = np.array([[0,0],[1,0],[0,1],[1.5,1.5]])
m_I = np.array([0,1,2,3])
    
X = np.array([[0,0.5,1.0],[0,0.5,1.0],[0,0.5,1.0]])
Y = np.array([[0,0,0],[0.5,0.5,0.5],[1.0,1.0,1.0]])
Z = np.array([[0,0,0],[1,2,1],[1,3,2]])

## Plot
fig = plt.figure()
ax = plt.gca()
ax.contourf(X, Y, Z, levels=np.linspace(0,Z.max(),50))
# Plot Nodes
ax.plot(X.flatten(),Y.flatten(),color='black',marker='o',linewidth=0)
# Plot The Grid Lines Manually
ax.plot([0,1],[0,0],color='black',linewidth=1.5)
ax.plot([0,1],[0.5,0.5],c='black',lw=1.5)
ax.plot([0,1],[1,1],c=(0.0,0.0,0.0),lw=1.5)

plt.plot([0,0],[0,1],color='black',linewidth=1.5)
plt.plot([0.5,0.5],[0,1],color='black',linewidth=1.5)
plt.plot([1,1],[0,1],color='black',linewidth=1.5)

# Some Notes:
# c  = color
# fc = facecolor (r, g, b)
# ec = edgecolor (r, g, b)
# ls = linestyle {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
# lw = linewidth float
P1 = Polygon(np.array([[0,0],[0.5,0],[0.5,0.5],[0,0.5]]), True, fc=(1.0,0.0,0.0),  ec=(0.0,1.0,0.0) )
ax.add_patch(P1)

ax.set_xticks(np.linspace(0,1,6,endpoint=True))
ax.ticklabel_format(axis='x', style='sci', scilimits=(0,0), useOffset=0.0)


# Aspect ratio is set manually by specifying both width and height
fig.set_size_inches(w=6.3,h=6.3)
#plt.show()

plt.savefig(str(pathlib.Path(__file__).parent.absolute())+'/mpm1.pgf', dpi=400, bbox_inches='tight')

# Adding to latex
# !!! \usepackage{pgf}
# \begin{Figure}[htb]
# \begin{center}
# \input{mpm1.pgf}
# \end{center}
# 	\caption{A plot made from python with matplotlib.}
# 	\label{fig:first}
# \end{Figure}