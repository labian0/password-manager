import Neutron

win = Neutron.Window("Example", size=(1000, 1000), css="ui/styles.css")
win.display(file="ui/index.html")

first_page = win.getElementById("first-page-body")
main_page = win.getElementById("main-page-body")

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

win.getElementById("open-datebase-button").addEventListener("click", Neutron.event(changepage))

win.show()