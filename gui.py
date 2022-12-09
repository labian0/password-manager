import Neutron
from manager import *

win = Neutron.Window("Example", size=(1000, 1000), css="ui/styles.css")

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

def detail_entry(id=0):
    entry_details.innerHTML = man.db.get_entry(bytes(str(id), "utf-8"))

def display_entries():
    for x in man.db.entries:
        name = str(x["name"], "utf-8")
        email = str(x["email"], "utf-8")
        pw = str(x["pw"], "utf-8")
        id = str(x["id"], "utf-8")
        entry = f"{id}, {name}, {email}, {pw}"
        entry_list.appendChild(f"<a id=\"entry{id}\" onclick=\"detail_entry(\' + {id} + \')\"><li>{entry}</li></a>")

def opendatabase():
    man.opendb(file_path_input.getAttributes()["value"], password_input.getAttributes()["value"])
    changepage()
    display_entries()

def createandopendatabase():
    man.createdb(file_path_input.getAttributes()["value"], password_input.getAttributes()["value"])
    opendatabase()

win.display(file="ui/index.html", pyfunctions=[detail_entry])

first_page = win.getElementById("first-page-body")
main_page = win.getElementById("main-page-body")
file_path_input = win.getElementById("file-path-input")
password_input = win.getElementById("password-input")
man = PwManager() #create instance of password manager
entry_list = win.getElementById("main-page-entries")
entry_details = win.getElementById("main-page-details")

win.getElementById("open-database-button").addEventListener("click", Neutron.event(opendatabase))
win.getElementById("new-database-button").addEventListener("click", Neutron.event(createandopendatabase))

win.show()