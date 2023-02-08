import tkinter as tk
from tkinter import *


class GUI:
    def __init__(self, parent=None):
        return

    def setup(self):
        """Call to setup the user interface"""
        self.create_widget()
        self.setup_layout()

    def create_widget(self):
        """Create a widgets in tkinter to first window"""
        # set a default lang
        self.set_language("English")
        # set lang list
        self.langList = ["English", "Português Brasil"]

        # Frames
        self.inforFrame = Frame(self.container, borderwidth=1,
                                highlightbackground="black")
        self.dataFrame = Frame(self.container, borderwidth=1,
                               highlightbackground="black")
        self.btnFrame = Frame(self.container)
        # Labels
        self.titleLb = Label(self.inforFrame, textvariable=self.titleTxt)
        self.nameLb = Label(self.dataFrame, textvariable=self.nameTxt)
        self.lastNameLb = Label(self.dataFrame, textvariable=self.lastNameTxt)
        self.birthdayLb = Label(self.dataFrame, textvariable=self.birthdayTxt)
        self.phoneNumberLb = Label(
            self.dataFrame, textvariable=self.phoneNumberTxt)
        self.addressLb = Label(self.dataFrame, textvariable=self.addressTxt)
        self.emailLb = Label(self.dataFrame, textvariable=self.emailTxt)

        # buttons
        self.searchBtn = Button(
            self.btnFrame, textvariable=self.searchTxt, command=self.searchPerson)
        self.deleteBtn = Button(
            self.btnFrame, textvariable=self.deleteTxt, command=self.deletePerson)
        self.alterBtn = Button(
            self.btnFrame, textvariable=self.alterTxt, command=self.alterPerson)
        self.saveBtn = Button(
            self.btnFrame, textvariable=self.saveTxt, command=self.savePerson)

        # Entrys
        self.nameEntry = Entry(self.dataFrame)
        self.lastNameEntry = Entry(self.dataFrame)
        self.birthdayEntry = Entry(self.dataFrame)
        self.phoneNumberEntry = Entry(self.dataFrame)
        self.addressEntry = Entry(self.dataFrame)
        self.emailEntry = Entry(self.dataFrame)

        # OptionMenu
        # setLanguage command to do
        self.langSelectOpt = OptionMenu(
            self.inforFrame, self.langSelected, *self.langList, command=self.setLanguage)

        """Create widgets in tkinter to second window"""
        # Variables
        self.setFilter = StringVar()
        # frame
        self.topFrame = Frame(self.container2)
        self.centerFrame = Frame(self.container2)
        self.bottomFrame = Frame(self.container2)

        # Labels
        self.searchLbl = Label(self.topFrame, textvariable=self.searchTxt)
        self.resultsLbl = Label(self.centerFrame, textvariable=self.resultsTxt)
        # todo
        self.filterLbl = Label(self.topFrame, textvariable=self.filterTxt)

        # Filter Radio
        self.nameRdo = Radiobutton(self.topFrame, textvariable=self.nameTxt)
        self.lastNameRdo = Radiobutton(
            self.topFrame, textvariable=self.lastNameTxt)
        self.birthdayRdo = Radiobutton(
            self.topFrame, textvariable=self.birthdayTxt)

        # Entry
        self.searchEntry = Entry(self.centerFrame)

        # TreeView
        self.resultsTree = TreeView(self.bottomFrame)

    def savePerson(self):
        print("Save")

    def deletePerson(self):
        print("Delete")

    def alterPerson(self):
        print("Alter")

    def searchPerson(self):
        print("Search")

    def setLanguage(self, language):
        if(language == "English"):
            self.titleTxt = StringVar(None, "Contact Book")
            self.nameTxt = StringVar(None, "Name")
            self.lastNameTxt = StringVar(None, "Last Name")
            self.birthdayTxt = StringVar(None, "Birthday")
            self.phoneNumberTxt = StringVar(None, "Phone Number")
            self.addressTxt = StringVar(None, "Address")
            self.emailTxt = StringVar(None, "Email")
            self.searchTxt = StringVar(None, "Search")
            self.deleteTxt = StringVar(None, "Delete")
            self.alterTxt = StringVar(None, "Alter")
            self.saveTxt = StringVar(None, "Save")
            self.resultsTxt = StringVar(None, "Results")
        elif(language == "Português Brasil"):
            self.titleTxt = StringVar(None, "Livro de Contatos")
            self.nameTxt = StringVar(None, "Nome")
            self.lastNameTxt = StringVar(None, "Sobrenome")
            self.birthdayTxt = StringVar(None, "Data de Aniversário")
            self.phoneNumberTxt = StringVar(None, "Telefone")
            self.addressTxt = StringVar(None, "Endereço")
            self.emailTxt = StringVar(None, "Email")
            self.searchTxt = StringVar(None, "Buscar")
            self.deleteTxt = StringVar(None, "Excluir")
            self.alterTxt = StringVar(None, "Alterar")
            self.saveTxt = StringVar(None, "Salvar")
            self.resultsTxt = StringVar(None, "Resultados")
        else:
            pass
        return self


# test run
if __name__ == '__main__':
    print('runing view')
