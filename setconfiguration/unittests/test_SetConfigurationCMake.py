#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; py-continuation-offset: 4 -*-
"""
"""
from __future__ import print_function
import sys
sys.dont_write_bytecode = True

import os
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pprint import pprint

import unittest
from unittest import TestCase

# Coverage will always miss one of these depending on the system
# and what is available.
try:                                                                                                # pragma: no cover
    import unittest.mock as mock                                                                    # pragma: no cover
except:                                                                                             # pragma: no cover
    import mock                                                                                     # pragma: no cover

from mock import Mock
from mock import MagicMock
from mock import patch

import filecmp
from textwrap import dedent

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

from setenvironment import *

from .common import *


#===============================================================================
#
# General Utility Functions
#
#===============================================================================
global_gen_new_ground_truth_files = False
#global_gen_new_ground_truth_files = True     # comment this out for production.


#===============================================================================
#
# General Utility Functions
#
#===============================================================================



#===============================================================================
#
# Mock Helpers
#
#===============================================================================



#===============================================================================
#
# Tests
#
#===============================================================================



class SetConfigurationCMakeTest(TestCase):
    """
    Main test driver for the SetConfigurationCMake class
    """
    def setUp(self):
        print("")
        self.maxDiff = None
        self._filename = find_config_ini(filename="config_test_setconfigurationcmake.ini")

        # Get the location of the unit testing scripts (for file writing tests)
        unit_test_path = os.path.realpath(__file__)
        self.unit_test_file = os.path.basename(unit_test_path)
        self.unit_test_path = os.path.dirname(unit_test_path)


    def test_SetConfigurationCMake_Template(self):
        """
        Basic template test for SetConfigurationCMake.

        This test doesn't really validate any output -- it just runs a basic check.
        """
        print("\n")
        print("Load file: {}".format(self._filename))
        parser = SetConfigurationCMake(self._filename)
        parser.debug_level = 5
        parser.exception_control_level = 4
        parser.exception_control_compact_warnings = False

        print("-----[ TEST BEGIN ]----------------------------------------")
        section = "TEST_CONFIGURATION_A"
        print("Section  : {}".format(section))

        # parse a section
        data = parser.parse_section(section)

        # Pretty print the actions (unchecked)
        print("")
        parser.pretty_print_actions(section)
        print("-----[ TEST END ]------------------------------------------")

        print("OK")
        return

