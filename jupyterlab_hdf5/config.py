""" JupyterLab HDF : HDF5 file viewer for Jupyterlab """

# from traitlets import Unicode, CaselessStrEnum
from traitlets.config import Configurable
#
class HdfConfig(Configurable):
    pass
#     """
#     A Configurable that declares the configuration options
#     for the LatexHandler.
#     """
#     latex_command = Unicode('xelatex', config=True,
#         help='The LaTeX command to use when compiling ".tex" files.')
#     bib_command = Unicode('bibtex', config=True,
#         help='The BibTeX command to use when compiling ".tex" files.')
#     synctex_command = Unicode('synctex', config=True,
#         help='The synctex command to use when syncronizing between .tex and .pdf files.')
#     shell_escape = CaselessStrEnum(['restricted', 'allow', 'disallow'],
#         default_value='restricted', config=True,
#         help='Whether to allow shell escapes '+\
#         '(and by extension, arbitrary code execution). '+\
#         'Can be "restricted", for restricted shell escapes, '+\
#         '"allow", to allow all shell escapes, or "disallow", '+\
#         'to disallow all shell escapes')
