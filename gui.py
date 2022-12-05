import Neutron
from manager import *

win = Neutron.Window("Example", size=(1000, 1000), css="ui/styles.css")
win.display(file="ui/index.html")

first_page = win.getElementById("first-page-body")
main_page = win.getElementById("main-page-body")
file_path_input = win.getElementById("file-path-input")
password_input = win.getElementById("password-input")
man = PwManager() #create instance of password manager

def edit_classlist(element, classname, remove=True):
    classes = element.getAttributes()["className"].split(" ")
    if classname in classes and remove:
        classes.remove(classname)
    elif classname not in classes and remove:
        print("class not found")
        return
    else:
        classes.append(classname)
    classes = str().join(classes)
    element.setAttribute("class", classes)

def changepage():
    edit_classlist(first_page, "hidden", remove=False)
    edit_classlist(main_page, "hidden")

def opendatabase():
    man.opendb("path", "password")
    changepage()
    print(man.db.entries)

def createandopendatabase():
    man.createdb("path", "password")
    opendatabase()

win.getElementById("open-database-button").addEventListener("click", Neutron.event(opendatabase))
win.getElementById("new-database-button").addEventListener("click", Neutron.event(createandopendatabase))

win.show()