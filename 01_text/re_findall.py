# -*- coding: utf-8 -*-

import re

text = 'abbaaabbbaaaaa'

pattern = 'ab'

for match in re.findall(pattern, text):
    print 'Found "%s"' % match
