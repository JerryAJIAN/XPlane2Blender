import bpy
import os
import inspect
import sys

from io_xplane2blender.tests import *
from io_xplane2blender import xplane_config

__dirname__ = os.path.dirname(__file__)

def filterLines(line):
    return isinstance(line[0],str) and\
            ("ANIM" in line[0] or\
             "ATTR_manip" in line[0])

class TestRotationBoneRules(XPlaneTestCase):
    def test_1_only_rotated_around_one_axis(self):
        out = self.exportLayer(0)
        self.assertLoggerErrors(1)

    def test_2_rot_keyframes_must_be_sorted(self):
        out = self.exportLayer(1)
        self.assertLoggerErrors(1)

    def test_3_must_have_ge_2_rot_keyframes(self):
        out = self.exportLayer(2)
        self.assertLoggerErrors(1)

    def test_4_must_be_driven_by_only_1_dataref(self):
        out = self.exportLayer(3)
        self.assertLoggerErrors(1)

    def test_5_0_degree_rotation_not_allowed(self):
        out = self.exportLayer(4)
        self.assertLoggerErrors(1)

    def test_6_counter_clockwise_also_allowed(self):
        out = self.exportLayer(5)
        self.assertLoggerErrors(1)

    def test_7_known_good_rotation_bone(self):
        filename = inspect.stack()[0][3]
        self.assertLayerExportEqualsFixture(
            7, os.path.join(__dirname__, 'fixtures', filename + '.obj'),
            filename,
            filterLines
        )

runTestCases([TestRotationBoneRules])