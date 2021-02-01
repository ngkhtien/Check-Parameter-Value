"""Setting true value for parameter if the input contains nominated room name and false value if not."""
__author__='NguyenKhanhTien - khtien0107@gmail.com'
from Autodesk.Revit.DB import FilteredElementCollector, FilteredElementIdIterator, Transaction
from Autodesk.Revit.UI import TaskDialog
from rpw.ui.forms import TextInput, FlexForm, Label, ComboBox, TextBox,\
                         TaskDialog, Separator, Button, CheckBox
from Autodesk.Revit.DB.Architecture import Room, RoomFilter

doc = __revit__.ActiveUIDocument.Document
component = [Label('Enter Parameter Name:'),
                TextBox('textbox1', Text="CheckBalcony"),
                Label('Enter Room Name:'),
                TextBox('textbox2', Text="Balcony"),
                Separator(),
                Label('Nguyen Khanh Tien - khtien0107@gmail.com'),
                Button('Select')]
form = FlexForm('Check Parameter Value',component)
form.show()
paraname = form.values['textbox1']
name = form.values['textbox2']
RmFilter = RoomFilter()
collector = FilteredElementCollector(doc)
collector.WherePasses(RmFilter)
roomIdItr = collector.GetElementIdIterator()
roomIdItr.Reset()

t=Transaction(doc,"Check Parameter Value")
t.Start()
print ("Checking...")
while (roomIdItr.MoveNext()):
    roomId=roomIdItr.Current
    room = doc.GetElement(roomId)
    rmname = room.LookupParameter("Name").AsString()
    checkbal=room.LookupParameter(paraname)
    if ( name in rmname):
        checkbal.Set(True)
    else:
        checkbal.Set(False)
print ("COMPLETED!!!")
t.Commit()
