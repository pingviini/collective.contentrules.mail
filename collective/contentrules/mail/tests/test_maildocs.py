# -*- coding: utf-8 -*-
# Copyright (c) 2008 Ingeniweb

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING. If not, write to the
# Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
Generic Test case for collective.contentrules.mail doctest
"""
__docformat__ = 'restructuredtext'

import unittest
import doctest
import sys
import os

from Testing.ZopeTestCase import FunctionalDocFileSuite
from Products.Five.testbrowser import Browser

from base import TestCase

current_dir = os.path.dirname(__file__)


def doc_suite(test_dir, setUp=None, tearDown=None, globs=None):
    """Returns a test suite, based on doctests found in /doctest."""
    suite = []
    if globs is None:
        globs = globals()

    # preparing a few elements
    globs['test_dir'] = current_dir
    browser = Browser()
    browser.handleErrors = False
    globs['browser'] = browser

    flags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE |
             doctest.REPORT_ONLY_FIRST_FAILURE |
             doctest.REPORT_UDIFF)

    package_dir = os.path.split(test_dir)[0]
    if package_dir not in sys.path:
        sys.path.append(package_dir)

    docs = []
    for dir_ in ('doctests', 'docs'):
        doctest_dir = os.path.join(package_dir, dir_)

        # filtering files on extension
        docs.extend([os.path.join(doctest_dir, doc) for doc in
                     os.listdir(doctest_dir) if doc.endswith('.txt')])

    for test in docs:
        suite.append(FunctionalDocFileSuite(test, optionflags=flags,
                                            globs=globs, setUp=setUp,
                                            tearDown=tearDown,
                                            test_class=TestCase,
                                            module_relative=False))

    return unittest.TestSuite(suite)


def test_suite():
    """returns the test suite"""
    return doc_suite(current_dir)

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
