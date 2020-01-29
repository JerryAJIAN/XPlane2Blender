import inspect

from typing import Tuple
import os
import sys

import bpy
from io_xplane2blender import xplane_config, xplane_helpers
from io_xplane2blender.tests import *

__dirname__ = os.path.dirname(__file__)

def filterLines(line:Tuple[str])->bool:
    return (isinstance(line[0],str)
             and ("ANIM_" in line[0]
                  or "TRIS" in line[0]))


class ParentOutOfCollectionNotAnim(XPlaneTestCase):
    def test_ExpCollection_not_really_animated(self)->None:
        filename = inspect.stack()[0].function

        self.assertExportableRootExportEqualsFixture(
            bpy.data.collections[filename[5:]],
            os.path.join(__dirname__, "fixtures", filename + ".obj"),
            filename,
            filterLines
        )

runTestCases([ParentOutOfCollectionNotAnim])
