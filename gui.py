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
    classes = " ".join(classes)
    element.setAttribute("class", classes)

def changepage():
    edit_classlist(first_page, "hidden", remove=False)
    edit_classlist(main_page, "hidden")

def click_entry(id=0):
    global selected_entry
    entry_details.innerHTML = man.db.get_entry(id)
    if selected_entry:
        edit_classlist(win.getElementById(selected_entry), "selected-entry", remove=True) #remove "selected-entry" class from previously selected entry
    edit_classlist(win.getElementById(f"entry{id}"), "selected-entry", remove=False)
    selected_entry = f"entry{id}"

def display_entries():
    entry_list.innerHTML_set("") #clear entry list
    for x in man.db.entries:
        name = x["name"]
        id = x["id"]
        entry_list.appendChild(f"<li id=\"entry{id}\" onclick=\"click_entry(\' + {id} + \')\">{name.upper()}</li>")

def delete_selected_entry():
    global selected_entry
    if selected_entry:
        id = int(selected_entry[5:])
        man.db.del_entry(id)
        display_entries()
        print(id, man.db.entries, entry_list.innerHTML)
        selected_entry = ""

def add_new_entry():
    man.db.add_entry(new_entry_name.getAttributes()["value"], new_entry_email.getAttributes()["value"], new_entry_password.getAttributes()["value"])
    edit_classlist(new_entry_popup, "hidden", remove=False)
    edit_classlist(main_page, "hidden", remove=True)
    display_entries()

def opendatabase():
    man.opendb(file_path_input.getAttributes()["value"], password_input.getAttributes()["value"])
    changepage()
    display_entries()

def createandopendatabase():
    man.createdb(file_path_input.getAttributes()["value"], password_input.getAttributes()["value"])
    opendatabase()

def show_new_entry_popup():
    edit_classlist(main_page, "hidden", remove=False)
    edit_classlist(new_entry_popup, "hidden", remove=True)

win.display(file="ui/index.html", pyfunctions=[click_entry])

first_page = win.getElementById("first-page-body")
main_page = win.getElementById("main-page-body")
file_path_input = win.getElementById("file-path-input")
password_input = win.getElementById("password-input")
man = PwManager() #create instance of password manager
selected_entry = str()
entry_list = win.getElementById("main-page-entries")
entry_details = win.getElementById("main-page-details")
new_entry_popup = win.getElementById("new-entry-popup")
new_entry_name = win.getElementById("new-entry-name")
new_entry_email = win.getElementById("new-entry-email")
new_entry_password = win.getElementById("new-entry-password")

win.getElementById("open-database-button").addEventListener("click", Neutron.event(opendatabase))
win.getElementById("new-database-button").addEventListener("click", Neutron.event(createandopendatabase))
win.getElementById("delete-selected-entry-button").addEventListener("click", Neutron.event(delete_selected_entry))
win.getElementById("create-new-entry-button").addEventListener("click", Neutron.event(show_new_entry_popup))
win.getElementById("add-entry-button").addEventListener("click", Neutron.event(add_new_entry))

win.show()