'''
Created on Aug 30, 2014

@author: Max Ruiz
'''
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from ContactBook import *
import xml.etree.ElementTree as ET


class MainWindow(QMainWindow):
    rootFile = 'RootFile.xml'


    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.openBook = None
        self.root = None

        self.initFile()
        self.setupWindow()



    def initFile(self):
        try:
            tree = ET.parse(self.rootFile)
            self.root = tree.getroot()
        except FileNotFoundError:
            self.writeContactInfo()


        self.openBook = self.root.find("[@startUp='True']")



    def writeContactInfo(self, root=None, bookName={}, fName={}, lName={}, phNum={}, email={}, address={}):
        if root is None:
            self.root = ET.Element('Contact_Books')

        book = ET.SubElement(self.root, 'Book')
        try:
            bName = bookName['Name']
            isStartUp = bookName['startUp']
            book.set('Name', bName)
            book.set('startUp', isStartUp)
            infoGood = 1
        except KeyError:
            book.set('Name', 'Generic Book')
            book.set('startUp', 'True')
            infoGood = 0

        if infoGood == 1:
            person = ET.SubElement(book, 'Person')
            self.applyAttrText(person, fName)
            self.applyAttrText(person, lName)

            pn = ET.SubElement(person, 'PhoneNumber')
            self.applyAttrText(pn, phNum)

            em = ET.SubElement(person, 'Email')
            self.applyAttrText(em, email)

            ad = ET.SubElement(person, 'Address')
            self.applyAttrText(ad, address)
        else:
            person = ET.SubElement(book, 'Person')
            person.set('fName', '')
            person.set('lName', '')

            pn = ET.SubElement(person, 'PhoneNumber')
            pn.text = ''

            em = ET.SubElement(person, 'Email')
            em.text = ''

            ad = ET.SubElement(person, 'Address')
            ad.text = ''

        tree = ET.ElementTree(self.root)
        tree.write(self.rootFile)

    def applyAttrText(self, elem, detailDict):
        if len(detailDict) !=0:
            for key in detailDict:
                if key != 'text':
                    elem.set(key, detailDict[key])
                else:
                    elem.text = detailDict['text']
        else:
            pass

    def setupWindow(self):
        for child in self.root:
            self.ui.contactBookComboBox.addItem(child.get('Name'))

        '''
        self.ui.contactBookComboBox.addItem('Hello ComboBox')
        self.ui.contactBookComboBox.addItem('Placeholder 2')
        self.ui.DeleteBookTextBrowser.insertPlainText("Plain Text\n")
        self.ui.DeleteBookTextBrowser.insertPlainText("Plain Text2")
        self.ui.contactBookComboBox.currentIndexChanged.connect(lambda: print(self.ui.contactBookComboBox.currentText()))
        '''



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    wind = MainWindow()
    wind.show()
    app.exec()
