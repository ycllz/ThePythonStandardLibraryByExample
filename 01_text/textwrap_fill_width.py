# -*- coding: utf-8 -*-

import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
for width in [45, 70]:
    print '%d Columns:\n' % width
    print textwrap.fill(dedented_text, width=width)
    print
