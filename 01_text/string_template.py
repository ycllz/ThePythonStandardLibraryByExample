# -*- coding: utf-8 -*-
import string

values = {'var':'foo'}

t= string.Template("""
Variable            : $var
Escape              : $$
Variable in text    : ${var}ialbe
""")

print 'TEMPLATE:', t.substitute(values)

s = """
Variable            : %(var)s
Escape              : %%
Variable in text    : %(var)siable
"""

print 'INTERPOLATION:', s % values
