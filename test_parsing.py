# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

from lxml import etree, html


class TestLXMLParsing(unittest.TestCase):
    def test_lxml_html_parsing(self):
        p = html.fromstring('<p>Invalid < " > &</p>')
        p_string = etree.tostring(p, method='html', encoding='unicode')
        print(p_string)
        self.assertEqual(p_string, '<p>Invalid &lt; " &gt; &amp;</p>')
