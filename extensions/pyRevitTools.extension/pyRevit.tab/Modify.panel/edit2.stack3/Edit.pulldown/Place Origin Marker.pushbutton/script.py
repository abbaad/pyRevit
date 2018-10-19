"""Tag all chosen element types in all views."""
#pylint: disable=C0103,E0401,C0111,W0703
from pyrevit import revit, DB
from pyrevit import forms
from pyrevit import script

__author__ = "{{author}}"


logger = script.get_logger()
output = script.get_output()


# makr a cross shape
line1 = DB.Line.CreateBound(DB.XYZ(-1, -1, 0), DB.XYZ(1, 1, 0))
line2 = DB.Line.CreateBound(DB.XYZ(1, -1, 0), DB.XYZ(-1, 1, 0))
# place lines on active view
try:
    with revit.Transaction('Place Origin Marker', log_errors=False):
        revit.doc.Create.NewDetailCurve(revit.activeview, line1)
        revit.doc.Create.NewDetailCurve(revit.activeview, line2)
except Exception as ex:
    forms.alert("You are not on a plan view.", sub_msg=str(ex))