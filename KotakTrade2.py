from PyQt5.QtWidgets import QWidget, QVBoxLayout,QGridLayout, QPushButton, QLineEdit, QLabel, QCheckBox, QComboBox
# from PyQt6.QtWidgets import QWidget, QVBoxLayout,QGridLayout, QPushButton, QLineEdit, QLabel, QCheckBox
# from PyQt6 import QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QKeySequence 
from PyQt5.QtWidgets import QShortcut
import threading
from threading import Thread
import json
import http.client
#import requests
import time
import datetime
##from datetime import datetime, timedelta
import math
import kotaklogin

import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        # app = QApplication(sys.argv)
        # main_window = QMainWindow()
        # self.setWindowTitle('Trade Fields')
        self.setWindowTitle('Trade Execution')

        # Text fields in the first row
        text_fields_layout = QGridLayout()
        layout.addLayout(text_fields_layout)

        # Button fields in the second row
        button_fields_layout = QGridLayout()
        layout.addLayout(button_fields_layout)

        # Create a keyboard shortcut 
        shortcut1 = QKeySequence(Qt.Key_Up)
        self.shortcut1 = QShortcut(shortcut1, self)
        shortcut2 = QKeySequence(Qt.Key_Down)
        self.shortcut2 = QShortcut(shortcut2, self)
        shortcut3 = QKeySequence(Qt.Key_Left)
        self.shortcut3 = QShortcut(shortcut3, self)
        shortcut4 = QKeySequence(Qt.Key_Right)
        self.shortcut4 = QShortcut(shortcut4, self)
        shortcut5 = QKeySequence(Qt.Key_G)
        self.shortcut5 = QShortcut(shortcut5, self)
        shortcut6 = QKeySequence(Qt.Key_I)
        self.shortcut6 = QShortcut(shortcut6, self)
        # shortcut7 = QKeySequence(Qt.Key_C)
        shortcut7 = QKeySequence(Qt.Key_Space)
        self.shortcut7 = QShortcut(shortcut7, self)
        shortcut8 = QKeySequence(Qt.Key_P)
        self.shortcut8 = QShortcut(shortcut8, self)

         # Create four buttons
        button1 = QPushButton("BCALL")
        button1.setAccessibleName("BCALL") # _ is used for temp storage 
        button1.setStyleSheet("background-color: green")
        button1.setGeometry(20, 20, 100, 30)
        button2 = QPushButton("SCALL")
        button2.setAccessibleName("SCALL") 
        button2.setStyleSheet("background-color: red")
        button2.setGeometry(20, 20, 100, 30)
        button3 = QPushButton("BPUT")
        button3.setAccessibleName("BPUT") 
        button3.setStyleSheet("background-color: green")
        button3.setGeometry(20, 20, 100, 30)
        button4 = QPushButton("SPUT")
        button4.setAccessibleName("SPUT") 
        button4.setStyleSheet("background-color: red")
        button4.setGeometry(20, 20, 100, 30)
        button5 = QPushButton("Index")
        button5.setAccessibleName("BN") 
        button5.setStyleSheet("background-color: orange")
        button5.setGeometry(20, 20, 100, 30)
        button6 = QPushButton("CE")
        button6.setAccessibleName("CE") 
        button6.setStyleSheet("background-color: green")
        button6.setGeometry(20, 20, 100, 30)
        button7 = QPushButton("PE")
        button7.setAccessibleName("PE") 
        button7.setStyleSheet("background-color: red")
        button7.setGeometry(20, 20, 100, 30)

        # Add the buttons and dropdowns to the layout
        button_fields_layout.addWidget(button1, 0, 0)
        button_fields_layout.addWidget(button2, 1, 0)
        button_fields_layout.addWidget(button3, 2, 0)
        button_fields_layout.addWidget(button4, 3, 0)
        button_fields_layout.addWidget(button5, 4, 0)
        button_fields_layout.addWidget(button6, 5, 0)
        button_fields_layout.addWidget(button7, 6, 0)

        self.text_box1 = QLineEdit("900")
        self.text_box1.setPlaceholderText("900")
        self.text_box1.setGeometry(140, 20, 150, 30)
        increment_button1 = QPushButton("+")
        increment_button1.setStyleSheet("background-color: green")
        decrement_button1 = QPushButton("-")
        decrement_button1.setStyleSheet("background-color: red")



        # layout_row = QHBoxLayout()
        layout_row = QGridLayout()
        layout_row.addWidget(self.text_box1,0, 1)
        layout_row.addWidget(increment_button1,0, 2)
        layout_row.addWidget(decrement_button1,0, 3)

        # this label moved up here t oavoid the exception Exception while connection to get index->socket: 'MyWidget' object has no attribute 'response_label_order5' coming from self.text_box11 = QLineEdit(str(self.execute_curl_getIndex("NIFTY BANK")))
        self.response_label_order5 = QLabel("Index")
        layout_row.addWidget(button5,4,5)
        layout_row.addWidget(self.response_label_order5,5,5)

        self.text_box11 = QLineEdit(str(self.execute_curl_getIndex("NIFTY BANK")))
        self.text_box11.setPlaceholderText("48000")
        increment_button11 = QPushButton("+")
        increment_button11.setStyleSheet("background-color: green")
        decrement_button11 = QPushButton("-")
        decrement_button11.setStyleSheet("background-color: red")


        # layout_row = QHBoxLayout()
        layout_row.addWidget(self.text_box11,0, 4)
        layout_row.addWidget(increment_button11,0, 5)
        layout_row.addWidget(decrement_button11,0, 6)       

        # layout_row.addWidget(self.doubleSpinBox,0, 7)
        self.checkbox = QCheckBox("NIFTY")
        self.checkbox.stateChanged.connect(lambda: self.checkbox_function())

        #self.text_boxIDX = QLineEdit("BANKNIFTY")
        #self.text_boxIDX.setPlaceholderText("BANKNIFTY")
        #self.text_boxIDX.setGeometry(140, 20, 150, 30)

        self.text_boxIDX = QComboBox()
        #self.text_boxIDX.addItem("NIFTY BANK")
        self.text_boxIDX.addItem("BANKNIFTY")
        self.text_boxIDX.addItem("NIFTY")
        self.text_boxIDX.addItem("FINNIFTY")
        self.text_boxIDX.addItem("MIDCPNIFTY")

        layout_row.addWidget(self.text_boxIDX,0, 7)   

        #layout_row.addWidget(self.checkbox,0, 7)  
        # layout_row.addWidget(self.doubleSpinBox,0, 7)

        # self.text_boxslimit = QLineEdit("5")
        # self.text_boxslimit.setPlaceholderText("5")
        # self.checkbox1.stateChanged.connect(lambda: self.checkbox_function())
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self)
        # self.doubleSpinBox.setGeometry(QtCore.QRect(500, 210, 75, 30))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setValue(10)
        self.doubleSpinBox.setRange(0.00, 800.00)
        self.doubleSpinBox.setSingleStep(1)
        # layout_row.addWidget(self.doubleSpinBox,0, 11)  
        layout_row.addWidget(self.doubleSpinBox,0, 8)  

        self.checkbox1 = QCheckBox("SLTPLimit")
        self.checkbox1.stateChanged.connect(lambda: self.checkbox_function())
        layout_row.addWidget(self.checkbox1,0, 9)  
        # self.checkbox.show()

        self.checkbox2 = QCheckBox("GetExpDate")
        self.checkbox2.setChecked(True)
        if self.checkbox2.isChecked():
            self.getexpdate()
            print("Checkbox2 getexp date is checked!")
        self.checkbox2.stateChanged.connect(lambda: self.getexpdate())
        layout_row.addWidget(self.checkbox2,0, 10) 

        layout.addLayout(layout_row)
        #layout.addLayout(button_fields_layout)
        self.setLayout(layout)

        self.text_box2 = QLineEdit("5")
        self.text_box2.setPlaceholderText("5")
        self.text_box2.setGeometry(140, 20, 150, 30)
        self.increment_button2 = QPushButton("+")
        self.increment_button2.setStyleSheet("background-color: green")
        self.decrement_button2 = QPushButton("-")
        self.decrement_button2.setStyleSheet("background-color: red")
        button9 = QPushButton("SL")
        button9.setAccessibleName("SL") 
        button9.setStyleSheet("background-color: red")
        button9.setGeometry(20, 20, 100, 30)

        # layout_row = QHBoxLayout()
        layout_row2 = QGridLayout()
        layout_row2.addWidget(self.text_box2,7, 1)
        layout_row2.addWidget(self.increment_button2,7, 2)
        layout_row2.addWidget(self.decrement_button2,7, 3)
        layout_row2.addWidget(button9,7, 4)
        layout.addLayout(layout_row2)

        self.text_box22 = QLineEdit("5")
        self.text_box22.setPlaceholderText("5")
        self.text_box22.setGeometry(140, 20, 150, 30)
        self.increment_button22 = QPushButton("+")
        self.increment_button22.setStyleSheet("background-color: green")
        self.decrement_button22 = QPushButton("-")
        self.decrement_button22.setStyleSheet("background-color: red")
        button8 = QPushButton("TP")
        button8.setAccessibleName("TP") 
        button8.setStyleSheet("background-color: green")
        button8.setGeometry(20, 20, 100, 30)

        # layout_row = QHBoxLayout()
        layout_row2 = QGridLayout()
        layout_row2.addWidget(self.text_box22,8, 4)
        layout_row2.addWidget(self.increment_button22,8, 5)
        layout_row2.addWidget(self.decrement_button22,8, 6)
        layout_row2.addWidget(button8,8, 7)
        layout.addLayout(layout_row2)


        self.text_box3 = QLineEdit("240113000001542")
        self.text_box3.setPlaceholderText("240113000001542")
        self.text_box3.setGeometry(140, 20, 150, 30)
        button10 = QPushButton("CancOrdNo")
        button10.setAccessibleName("CancOrdNo") 
        button10.setStyleSheet("background-color: grey")
        button10.setGeometry(20, 20, 100, 30)

        layout_row3 = QGridLayout()
        layout_row3.addWidget(self.text_box3,9, 1)
        # layout_row2.addWidget(self.increment_button22,8, 5)
        # layout_row2.addWidget(self.decrement_button22,8, 6)
        layout_row3.addWidget(button10,9, 2)
        layout.addLayout(layout_row3)

        self.text_box31 = QLineEdit("240113000001542") # order no
        self.text_box31.setPlaceholderText("240113000001542")
        self.text_box31.setGeometry(140, 20, 150, 30)
        self.text_box32 = QLineEdit("15") # qty 
        self.text_box32.setPlaceholderText("150")
        self.text_box32.setGeometry(140, 20, 150, 30)

        self.text_box34 = QLineEdit("BANKNIFTY") # trdsym 
        self.text_box34.setPlaceholderText("150")
        self.text_box34.setGeometry(140, 20, 150, 30)
        self.text_box35 = QLineEdit("11536") # tok 
        self.text_box35.setPlaceholderText("11536")
        self.text_box35.setGeometry(140, 20, 150, 30)

        self.text_box33 = QLineEdit("150") # price 
        self.text_box33.setPlaceholderText("150")
        self.text_box33.setGeometry(140, 20, 150, 30)
        self.increment_button32 = QPushButton("+")
        self.increment_button32.setStyleSheet("background-color: green")
        self.decrement_button32 = QPushButton("-")
        self.decrement_button32.setStyleSheet("background-color: red")
        button11 = QPushButton("Modify")
        button11.setAccessibleName("Modify") 
        button11.setStyleSheet("background-color: grey")
        button11.setGeometry(20, 20, 100, 30)

        layout_row3 = QGridLayout()
        layout_row3.addWidget(self.text_box31,9, 3)
        layout_row3.addWidget(self.text_box32,9, 4)
        
        layout_row3.addWidget(self.text_box34,9, 5)
        layout_row3.addWidget(self.text_box35,9, 6)
        layout_row3.addWidget(self.text_box33,9, 7)
        layout_row3.addWidget(self.increment_button32,9, 8)
        layout_row3.addWidget(self.decrement_button32,9, 9)
        layout_row3.addWidget(button11,9, 10)
        layout.addLayout(layout_row3)


        buttongetpos = QPushButton("GetPositions")
        buttongetpos.setAccessibleName("GetPositions")
        layout.addWidget(buttongetpos)
        buttongetpos.clicked.connect(lambda: self.execute_curl_commandgetpos1())
        self.response_label = QLabel("get pos API Response")
        layout.addWidget(self.response_label)

        buttonclosepos = QPushButton("ClosePositions")
        buttonclosepos.setAccessibleName("ClosePositions")
        layout.addWidget(buttonclosepos)
        buttonclosepos.clicked.connect(lambda: self.execute_curl_commandclosepos())
        self.response_label_close = QLabel("close API Response")
        layout.addWidget(self.response_label_close)

        self.response_label_order1 = QLabel("OrderAPI Response")
        layout_row.addWidget(button1,4,1)
        layout_row.addWidget(self.response_label_order1,5,1)
        #button1.clicked.connect(self.response_label_order1)

        self.response_label_order2 = QLabel("OrderAPI Response")
        layout_row.addWidget(button2,4,2)
        layout_row.addWidget(self.response_label_order2,5,2)

        self.response_label_order3 = QLabel("OrderAPI Response")
        layout_row.addWidget(button3,4,3)
        layout_row.addWidget(self.response_label_order3,5,3)

        self.response_label_order4 = QLabel("OrderAPI Response")
        layout_row.addWidget(button4,4,4)
        layout_row.addWidget(self.response_label_order4,5,4)

        

        self.response_label_order6 = QLabel("CE")
        layout_row.addWidget(button6,4,6)
        layout_row.addWidget(self.response_label_order6,5,6)

        self.response_label_order7 = QLabel("PE")
        layout_row.addWidget(button7,4,7)
        layout_row.addWidget(self.response_label_order7,5,7)

        
        self.response_label_lesson = QLabel("ITS Ok Go Big dont hesitate you can handle just bloody do it and be Patient")
        fontt = self.response_label_lesson.font()
        fontt.setBold(True)
        self.response_label_lesson.setFont(fontt)
        layout.addWidget(self.response_label_lesson)
        self.response_label_lesson = QLabel("Dont freeze when its happening Dont be afraid to enter and be patient after you enter and when you are in loss you dont mind going big with aggression ")
        layout.addWidget(self.response_label_lesson)
        self.response_label_lesson1 = QLabel("so Use the same aggression at the first place but with sniper trades and just when you lose dont lose more than what you  make on an aaverage just get ou its ok accept the loss for the day")
        layout.addWidget(self.response_label_lesson1)
        # self.response_label_lesson2 = QLabel("so Use the same aggression at the first place but with sniper trades and just when you lose dont lose more than what you  make on an aaverage just get ou its ok accept the loss for the day")
        # layout.addWidget(self.response_label_lesson2)

        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.process_values)
        # self.timer.start(100)  # Update every 100 milliseconds

        # Connect the activated signal to the function
        #self.text_boxIDX.activated[str].connect(self.on_combobox_changed)
        

        #if button1:
        button1.clicked.connect(lambda _,tb=self.text_box1, tb1=self.text_box11,tb2=self.text_boxIDX: self.button_clicked(tb,tb1,tb2))        
        increment_button1.clicked.connect(lambda _, tb=self.text_box1: self.increment_value(tb))
        decrement_button1.clicked.connect(lambda _, tb=self.text_box1: self.decrement_value(tb))
        increment_button11.clicked.connect(lambda _, tb=self.text_box11: self.increment_value1(tb))
        decrement_button11.clicked.connect(lambda _, tb=self.text_box11: self.decrement_value1(tb))
        self.increment_button2.clicked.connect(lambda _, tb=self.text_box2: self.increment_value2(tb))
        self.decrement_button2.clicked.connect(lambda _, tb=self.text_box2: self.decrement_value2(tb))
        self.increment_button22.clicked.connect(lambda _, tb=self.text_box22: self.increment_value2(tb))
        self.decrement_button22.clicked.connect(lambda _, tb=self.text_box22: self.decrement_value2(tb))

        self.increment_button32.clicked.connect(lambda _, tb=self.text_box33: self.increment_value2(tb))
        self.decrement_button32.clicked.connect(lambda _, tb=self.text_box33: self.decrement_value2(tb))
 
        button2.clicked.connect(lambda _,tb=self.text_box1, tb1=self.text_box11,tb2=self.text_boxIDX: self.button_clicked(tb,tb1,tb2))        

        button3.clicked.connect(lambda _,tb=self.text_box1, tb1=self.text_box11,tb2=self.text_boxIDX: self.button_clicked(tb,tb1,tb2))        

        button4.clicked.connect(lambda _,tb=self.text_box1, tb1=self.text_box11,tb2=self.text_boxIDX: self.button_clicked(tb,tb1,tb2))      
        button5.clicked.connect(lambda: self.execute_curl_getIndex("NIFTY BANK"))
        button6.clicked.connect(lambda: self.execute_curl_getLTP(str(self.text_box11.text())))
        button7.clicked.connect(lambda: self.execute_curl_getLTP(str(self.text_box11.text())))          
        button10.clicked.connect(lambda: self.execute_cancelorder(str(self.text_box3.text()))) 
        button11.clicked.connect(lambda: self.execute_modifyorder())

        #if self.shortcut1 :
        self.shortcut1.activated.connect(lambda: self.key_clicked(self.text_box1, self.text_box11,self.shortcut1))
        #if self.shortcut2 :
        self.shortcut2.activated.connect(lambda: self.key_clicked(self.text_box1, self.text_box11,self.shortcut2))
        #if self.shortcut3 :
        self.shortcut3.activated.connect(lambda: self.key_clicked(self.text_box1, self.text_box11,self.shortcut3))
        #if self.shortcut4 :
        self.shortcut4.activated.connect(lambda: self.key_clicked(self.text_box1, self.text_box11,self.shortcut4))
        #if self.shortcut4 :
        self.shortcut5.activated.connect(lambda: self.execute_curl_commandgetpos1())    
        # self.shortcut6.activated.connect(lambda: self.execute_curl_getIndex("NIFTY BANK"))  
        # self.shortcut7.activated.connect(lambda: self.keyCP_clicked(self.text_box11,self.shortcut7))  
        self.shortcut7.activated.connect(lambda: self.execute_curl_commandclosepos())  
        self.shortcut8.activated.connect(lambda: self.keyCP_clicked(self.text_box11,self.shortcut8))  

    def on_combobox_changed(self, selected_value):
        """
        This function is called when an item in the combobox is selected.

        Args:
            selected_value (str): The text of the selected item.
        """
        print(f"Selected value: {selected_value}")
        # Call your desired function here, passing selected_value as an argument
        #str(self.execute_curl_getIndex("NIFTY BANK"))
        self.text_box11 = str(self.execute_curl_getIndex(selected_value))
        #self.my_function(selected_value)

    def getexpdate(self):
        global stripped_date,formatted_date,formatted_datethu,formatted_datetue
        today = datetime.date.today()


        # Get the current day of the week
        today1 = datetime.date.today().weekday()

        # Calculate the number of days until the next Wednesday
        if today1 == 0:  # Monday
            days_until_wednesday = 2
            days_until_Tuesday  = 1
            days_until_Thursday = 3
            days_until_Friday = 4
        elif today1 == 1:  # Tuesday
            days_until_wednesday = 1
            days_until_Tuesday  = 0
            days_until_Thursday = 2
            days_until_Friday = 3
        elif today1 == 2:  # Wednesday
            days_until_wednesday = 0
            days_until_Tuesday  = 6
            days_until_Thursday = 1
            days_until_Friday = 2
        elif today1 == 3:  # Thursday
            days_until_wednesday = 6
            days_until_Tuesday  = 5
            days_until_Thursday = 0
            days_until_Friday = 1
        elif today1 == 4:  # Friday
            days_until_wednesday = 5
            days_until_Tuesday  = 4
            days_until_Thursday = 6
            days_until_Friday = 0
        elif today1 == 5:  # Saturday
            days_until_wednesday = 4
            days_until_Tuesday  = 3
            days_until_Thursday = 5
            days_until_Friday = 6
        else:  # Sunday
            days_until_wednesday = 3
            days_until_Tuesday  = 2
            days_until_Thursday = 4
            days_until_Friday = 5
        #samco
        # Calculate the number of days until next Wednesday
        # days_until_wednesday = (6 - today.weekday()) % 7
        next_wednesday = today + datetime.timedelta(days=((2 - today.weekday()) % 7))
        # next_wednesday = today + datetime.timedelta(days=days_until_wednesday)

        # Format the date as requested
        formatted_date = next_wednesday.strftime("%d%b%y")

        uppercase_month = formatted_date[3:6].upper()  # Extract month and capitalize it
        formatted_date = formatted_date[:3] + uppercase_month + formatted_date[6:]  # Reconstruct the date with capitalized month
        # print(formatted_date)  # Output: 17JAN24

        print("Next Wednesday:", formatted_date)

        #kotak
        # Calculate the number of days until next Wednesday
        days_until_wednesday1 = (2 - today.weekday()) % 7
        next_wednesday1 = today + datetime.timedelta(days=days_until_wednesday1)

        # Extract year, month, and day separately
        next_wednesday_year = next_wednesday1.year % 100  # Extract last two digits of the year
        next_wednesday_month = next_wednesday1.month  # Month as a number (1-12)
        next_wednesday_day = next_wednesday1.day

        # Format the date as requested
        formatted_date1 = f"{next_wednesday_year:02d}{next_wednesday_month:02d}{next_wednesday_day:02d}"
        stripped_date = formatted_date1[0:2] + formatted_date1[3:]  # Concatenate first 2 characters with characters from index 3 to the end
        # print(stripped_date)  # Output: 24117

        print("Next Wednesday kotak:", stripped_date)

        # Get the next Wednesday
        nextlast_wednesday = today + datetime.timedelta(days=7-today.weekday())

        # Check if the next Wednesday falls in the last week of the month
        if nextlast_wednesday.day > 21:
            # If it does, set the value to "24JAN"
            value = "24" + nextlast_wednesday.strftime("%b").upper()
        else:
            # If it doesn't, set the value to the current month in all caps
            value = today.strftime("%b").upper()

        print("this month expiry",value)

        # Find the upcoming Thursday
        upcoming_thursday = today + datetime.timedelta((3 - today.weekday()) % 7)

        # Format the date as year, month, day
        formatted_datethu = upcoming_thursday.strftime('%y%m%d')
        # Remove the century from the year
        formatted_datethu = formatted_datethu[0:2] + formatted_datethu[3:]  #formatted_datethu[2:]    
        print("for nifty",formatted_datethu)

        # Find the upcoming Thursday
        upcoming_tuesday = today + datetime.timedelta((1 - today.weekday()) % 7)

        # Format the date as year, month, day
        formatted_datetue = upcoming_tuesday.strftime('%y%m%d')
        # Remove the century from the year
        formatted_datetue = formatted_datetue[0:2] + formatted_datetue[3:]  #formatted_datethu[2:]    
        print("for finnifty",formatted_datetue)

    def checkbox_function(self):
        global upd
        if self.checkbox.isChecked():
            upd= True
            print("Checkbox Nifty is checked!")
        else:
            upd= False
            print("Checkbox Nifty is not checked!")
        if self.checkbox1.isChecked():
            upd= True
            print("Checkbox1 SLTPLimit is checked!")
        else:
            upd= False
            print("Checkbox1 SLTPLimit is not checked!")    
    def key_clicked(self,text_box1,text_box11, shortcut):
        #text_boxla= self.text_boxes[-1].text()
        qty = text_box1.text()
        Strike = text_box11.text()
        sequence = shortcut.key()
        key_name = QKeySequence(sequence).toString()

        if key_name == 'Up':
            # qty = text_box1.text()
            # Strike = text_box11.text()
            self.execute_curl_commandbuycall(str(Strike),str(qty))
        elif key_name == 'Left':   
            # qty = text_box1.text()
            # Strike = text_box11.text()
            self.execute_curl_commandsellcall(str(Strike),str(qty))
        elif key_name == 'Down':   
            # qty = text_box1.text()
            # Strike = text_box11.text()
            self.execute_curl_commandbuyputnew(str(Strike),str(qty))
        elif key_name == 'Right':   
            # qty = text_box1.text()
            # Strike = text_box11.text()
            self.execute_curl_commandsellputnew(str(Strike),str(qty)) 

        print("Shortcut pressed:", key_name,qty,Strike)
        print(f"Input qty: {qty}")
        print(f"Input Strike: {Strike}")

    def button_clicked(self, text_box,text_box1,text_box2):
        qty = text_box.text()
        Strike = text_box1.text()
        #selected_value = text_box2.currentText()  
        Indexnm = text_box2.currentText()  #text_box2.text()      
        butnName = self.sender()

        #button = self.sender()
        #print("button action is ",butnName.accessibleName())
        if butnName.accessibleName() == 'BCALL':
            #print("BC")
            self.execute_curl_commandbuycall(str(Strike),str(qty),str(Indexnm))
        if butnName.accessibleName() == 'SCALL':
            #print("BC")
            self.execute_curl_commandsellcall(str(Strike),str(qty),str(Indexnm))
        if butnName.accessibleName() == 'BPUT':
            #print("BC")
            self.execute_curl_commandbuyputnew(str(Strike),str(qty),str(Indexnm))
        if butnName.accessibleName() == 'SPUT':
            #print("BC")
            self.execute_curl_commandsellputnew(str(Strike),str(qty),str(Indexnm))              
        #print("button name is ",butnName)
        print(f"Input qty: {qty}")
        print(f"Input Strike: {Strike}")
        print(f"Input Index: {Indexnm}")
        # print(accesstoken)

    def execute_curl_commandbuycall(self,intext,inqty,ind):
            #opttype ="CE"
            #Tradetype = "B"
        self.execute_splitorder(intext,"CE","B",inqty,ind)

    def execute_curl_commandsellcall(self,intext,inqty,ind):
        self.execute_splitorder(intext,"CE","S",inqty,ind)

    def execute_curl_commandbuyputnew(self,intext,inqty,ind):
        self.execute_splitorder(intext,"PE","B",inqty,ind)

    def execute_curl_commandsellputnew(self,intext,inqty,ind):
        self.execute_splitorder(intext,"PE","S",inqty,ind)    
   
    
    def execute_curl_getIndex(self,IndexName):
#     spotPrice=random.randint(40000, 50000)
     spotPrice=47000
     spotPrice1=47000
    #  self.response_label_order5.setText(f"LTP is {spotPrice}")
     try:
          #st.write("API Response:")
          conn = http.client.HTTPSConnection("api.stocknote.com")
          #urlpos1="/quote/indexQuote?indexName="+str(IndexName)
          urlpos1="/quote/indexQuote?indexName=NIFTY%20BANK"
          #urlpos1="/quote/indexQuote?indexName="+str(IndexName)

          headerssamco = {
                "Content-Type": "application/json",
                "x-session-token": tokensam
                }
          payload = '' 
          conn.request("GET", urlpos1, payload, headerssamco)
          res = conn.getresponse()
          optiondata = res.read().decode()
                # Parse the JSON data
          response1_json = json.loads(optiondata)
          if response1_json['status'] == 'Success':
          #if quote_response.status_code == 200:
                # Parse the quote response JSON and extract price
                #quote_data = quote_response.json()
                spotPrice = response1_json["spotPrice"]
                spotPrice1 = self.round_up_to_nearest_hundredth(int(float(spotPrice)))
                #sSL = setSL
                print("Spot price of "+IndexName, spotPrice)
                self.response_label_order5.setText(f"LTP is {spotPrice}")
     except Exception as e:
        print("Exception while connection to get index->socket: %s\n" % e)           
     return spotPrice1
    def round_up_to_nearest_hundredth(self,number):
        return math.floor(number / 100) * 100
    
    def keyCP_clicked(self,text_box11, shortcut):
        #text_boxla= self.text_boxes[-1].text()
        # qty = text_box1.text()
        conn = http.client.HTTPSConnection("api.stocknote.com")
        tSymexpSSamco="BANKNIFTY"+ formatted_date #"17JAN24"
        TrdSymbolSamco = tSymexpSSamco+str(text_box11.text())#+self.response_label_order6.text()
        Strike = text_box11.text()
        sequence = shortcut.key()
        key_name = QKeySequence(sequence).toString()

        if key_name == 'C' or key_name == 'c':
            TrdSymbolSamco=TrdSymbolSamco+"CE"
            urlpos1="/quote/getQuote?exchange=NFO&symbolName="+str(TrdSymbolSamco)
        elif key_name == 'P' or key_name == 'p':   
            TrdSymbolSamco=TrdSymbolSamco+"PE"
            urlpos1="/quote/getQuote?exchange=NFO&symbolName="+str(TrdSymbolSamco)
        headerssamco = {
                "Content-Type": "application/json",
                "x-session-token": tokensam
                }
        payload = '' 
        conn.request("GET", urlpos1, payload, headerssamco)
        res = conn.getresponse()
        optiondata = res.read().decode()
            # Parse the JSON data
        response1_json = json.loads(optiondata)

        # Check if the status is Success
        if response1_json['status'] == 'Success':
                #print("success")
        #if response1_json.status == 'Success':
                # Parse the quote response JSON and extract price
                #quote_data = response1_json.json()
                current_price = response1_json["lastTradedPrice"]
                print("LTP of "+TrdSymbolSamco, current_price)
                if key_name == 'C' or key_name == 'c':
                #print("BC")
                #TrdSym+"CE"
                    #self.response_label_order6.setText("LTP of CE"+TrdSym, current_price)
                    self.response_label_order6.setText(f"LTP is {current_price}")
                if key_name == 'P' or key_name == 'p':
                #print("BC")
                #TrdSym+"CE"
                    #self.response_label_order7.setText("LTP of PE"+TrdSym, current_price)
                    self.response_label_order7.setText(f"LTP is {current_price}")    

        print("Shortcut pressed:", key_name,Strike)
        print(f"Input Strike: {Strike}")

    def execute_curl_getLTP(self,text_box11):
        #global current_price
        try:
            #st.write("API Response:")
            conn = http.client.HTTPSConnection("api.stocknote.com")
            # if self.checkbox.isChecked():
            #     tSymexpSSamco="NIFTY"+ formatted_date #"17JAN24"  "24JAN"
            # else:
            #     tSymexpSSamco="BANKNIFTY"+ formatted_date #"17JAN24"  "24JAN"
            tSymexpSSamco="BANKNIFTY"+ formatted_date #"24FEB" # "17JAN24"  "24JAN"
            # print("tSymexpSSamco",tSymexpSSamco)
            TrdSymbolSamco = tSymexpSSamco+text_box11#+self.response_label_order6.text()
            # print("trading symbol samco is",TrdSymbolSamco)
            urlpos1="/quote/getQuote?exchange=NFO&symbolName="+str(TrdSymbolSamco)
            # print("TrdSymbolSamco",TrdSymbolSamco)
            #SStrike = text_box11.text() 
            now = datetime.datetime.now()
            time_string = now.strftime("%H:%M:%S")
            current_price="0"
            butnName = self.sender()
            if butnName.accessibleName() == 'CE':
                    #print("BC")
                TrdSymbolSamco=TrdSymbolSamco+"CE"
                urlpos1="/quote/getQuote?exchange=NFO&symbolName="+str(TrdSymbolSamco)
            else:
                urlpos1="/quote/getQuote?exchange=NFO&symbolName="+str(TrdSymbolSamco)    
            if butnName.accessibleName() == 'PE':
                    #print("BC")
                TrdSymbolSamco=TrdSymbolSamco+"PE"
                urlpos1="/quote/getQuote?exchange=NFO&symbolName="+str(TrdSymbolSamco)
            else:
                urlpos1="/quote/getQuote?exchange=NFO&symbolName="+str(TrdSymbolSamco)
            # print("TrdSym for samco ",TrdSymbolSamco)    
            # print("turl is",urlpos1)                
            headerssamco = {
                "Content-Type": "application/json",
                "x-session-token": tokensam
                }
            payload = '' 
            conn.request("GET", urlpos1, payload, headerssamco)
            res = conn.getresponse()
            optiondata = res.read().decode()
                # Parse the JSON data
            response1_json = json.loads(optiondata)

            # Check if the status is Success
            if response1_json['status'] == 'Success':
                    current_price = response1_json["lastTradedPrice"]
                    print("LTP of "+TrdSymbolSamco + " at "+ time_string , current_price)
                    # print("LTP of "+TrdSymbolSamco, current_price)
                    if butnName.accessibleName() == 'CE':
                    #print("BC")
                    #TrdSym+"CE"
                        #self.response_label_order6.setText("LTP of CE"+TrdSym, current_price)
                        self.response_label_order6.setText(f"LTP is {current_price}")
                    if butnName.accessibleName() == 'PE':
                    #print("BC")
                    #TrdSym+"CE"
                        #self.response_label_order7.setText("LTP of PE"+TrdSym, current_price)
                        self.response_label_order7.setText(f"LTP is {current_price}")
            conn.close()            
        except Exception as e:
            print("Exception while connection to GetLTP->socket: %s\n" % e)           
        return str(current_price)
    

    def execute_cancelorder(self,nOrdNo):
        try:
            httpurl = "/Orders/2.0/quick/order/cancel?sId="+ str(newhsServerId)
            print("url",nOrdNo)
            # httpurl1 = "/Orders/2.0/quick/order/rule/ms/place?sId=server1"    
            conn = http.client.HTTPSConnection("gw-napi.kotaksecurities.com")   
            AccessToken = "Bearer "+ accesstoken
            # Set up request headers
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Sid":newsid,
                "Auth":newtoken,
                "neo-fin-key":"neotradeapi",
                "accept":"application/json",
                "Authorization": AccessToken
            }
            # Ordno=nOrdNo

            canpayld = 'jData=%7B%22on%22%3A%22' + nOrdNo + '%22%7D'
            # print("payload is ",canpayld)
            #buypayld = 'jData=%7B%22am%22%3A%22NO%22%2C%20%22dq%22%3A%220%22%2C%22es%22%3A%22' + nse_fo + '%22%2C%20%22mp%22%3A%220%22%2C%20%22pc%22%3A%22' + NRML + '%22%2C%20%22pf%22%3A%22N%22%2C%20%22pr%22%3A%22' + 0 + '%22%2C%20%22pt%22%3A%22' + MKT + '%22%2C%20%22qt%22%3A%22' + inqty + '%22%2C%20%22rt%22%3A%22' + DAY + '%22%2C%20%22tp%22%3A%22' + 0 + '%22%2C%20%22ts%22%3A%22' + tSymexpSS+intext+opttype + '%22%2C%20%22tt%22%3A%22' + Tradetype + '%22%7D'
            # Record the start time
            start_time = time.time()

            conn.request("POST", httpurl , canpayld, headers)
            res = conn.getresponse()

            # Record the end time
            end_time = time.time()
            # Calculate the elapsed time
            elapsed_time = end_time - start_time

            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            # print("price would be at",price)
            orderplaceddata = res.read().decode()
            # Parse the JSON data
            response_json = json.loads(orderplaceddata)

            # Print the JSON response
            print(response_json)

        except Exception as e:
            print("Exception while connection to cancel order->socket: %s\n" % e)
    

    def execute_orderbook(self,Ordno):
        try:
            conn = http.client.HTTPSConnection("gw-napi.kotaksecurities.com")
            httpurl = "/Orders/2.0/quick/user/orders?sId="+ str(newhsServerId)
            AccessToken = "Bearer "+ accesstoken
            headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Sid":newsid,
                    "Auth":newtoken,
                    "neo-fin-key":"neotradeapi",
                    "accept":"application/json",
                    "Authorization": AccessToken
                }
            payload = ''
            conn.request("GET", httpurl, payload, headers)
            
            res = conn.getresponse()
            print("sell ord no was",Ordno)

            # reports = data.decode("utf-8")
            posplaceddata = res.read().decode("utf-8")
            # Parse the JSON data
            response1_json = json.loads(posplaceddata)
            response_data = response1_json
            if 'data' in response_data:
                for item in response_data["data"]:
                    if item["nOrdNo"] == Ordno:
                        self.token = item['tok']
                        self.trdsym = item['trdSym']
            else:
                print("no data")    
                print("response_data",response_data)

            # data = ast.literal_eval(reports)
            # return data
        except Exception as e:
            print("Exception while connection to  order book->socket: %s\n" % e) 
        return str(self.token),  str(self.trdsym)

    def execute_modifyorder(self):
        try:
            httpurl = "/Orders/2.0/quick/order/vr/modify?sId="+ str(newhsServerId)            
            # print("url",nOrdNo)
            # httpurl1 = "/Orders/2.0/quick/order/rule/ms/place?sId=server1"    
            conn = http.client.HTTPSConnection("gw-napi.kotaksecurities.com")   
            AccessToken = "Bearer "+ accesstoken
            # Set up request headers
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Sid":newsid,
                "Auth":newtoken,
                "neo-fin-key":"neotradeapi",
                "accept":"application/json",
                "Authorization": AccessToken
            }
            # Ordno=nOrdNo

            tp= "0"
            pr = str(self.text_box33.text())
            mp="0"
            pc="NRML"
            dd="NA"
            dq="0"
            vd="DAY"
            tt="S"
            es="nse_fo"
            pt="L"
            tk= str(self.text_box35.text())
            ts= str(self.text_box34.text())
            qt= str(self.text_box32.text())
            no= str(self.text_box31.text())
            modpayload = 'jData=%7B%22tk%22%3A%22' + tk + '%22%2C%20%22am%22%3A%22NO%22%2C%20%22mp%22%3A%22' + mp + '%22%2C%20%22pc%22%3A%22' + pc + '%22%2C%20%22dd%22%3A%22' + dd + '%22%2C%20%22dq%22%3A%22' + dq + '%22%2C%20%22vd%22%3A%22' + vd + '%22%2C%20%22ts%22%3A%22' + ts + '%22%2C%20%22tt%22%3A%22' + tt + '%22%2C%20%22pr%22%3A%22' + pr + '%22%2C%20%22tp%22%3A%22' + tp + '%22%2C%20%22qt%22%3A%22' + qt + '%22%2C%20%22no%22%3A%22' + no + '%22%2C%20%22es%22%3A%22' + es + '%22%2C%20%22pt%22%3A%22' + pt + '%22%7D'
            # print("modify payload",modpayload)
            # print("payload is ",canpayld)
            #buypayld = 'jData=%7B%22am%22%3A%22NO%22%2C%20%22dq%22%3A%220%22%2C%22es%22%3A%22' + nse_fo + '%22%2C%20%22mp%22%3A%220%22%2C%20%22pc%22%3A%22' + NRML + '%22%2C%20%22pf%22%3A%22N%22%2C%20%22pr%22%3A%22' + 0 + '%22%2C%20%22pt%22%3A%22' + MKT + '%22%2C%20%22qt%22%3A%22' + inqty + '%22%2C%20%22rt%22%3A%22' + DAY + '%22%2C%20%22tp%22%3A%22' + 0 + '%22%2C%20%22ts%22%3A%22' + tSymexpSS+intext+opttype + '%22%2C%20%22tt%22%3A%22' + Tradetype + '%22%7D'
            # Record the start time
            start_time = time.time()

            conn.request("POST", httpurl , modpayload, headers)
            res = conn.getresponse()

            # Record the end time
            end_time = time.time()
            # Calculate the elapsed time
            elapsed_time = end_time - start_time
            # conn.close()
            # intext =intext+opttype
            # price= self.execute_curl_getLTP(intext+opttype)
            # Print the elapsed time
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            # print("price would be at",price)
            orderplaceddata = res.read().decode()
            # Parse the JSON data
            response_json = json.loads(orderplaceddata)

            # Print the JSON response
            print(response_json)

        except Exception as e:
            print("Exception while connection to modify order->socket: %s\n" % e)        

    
    def execute_curl_getLTPL(self,text_box11):
        # Acquire a lock to synchronize access to the current_price variable
        # with threading.Lock():
        #global current_price
        try:
            #st.write("API Response:")
            conn = http.client.HTTPSConnection("api.stocknote.com")
            # tSymexpSSamco="BANKNIFTY"+ "17JAN24"
            TrdSymbolSamco = text_box11#+self.response_label_order6.text()
            # print("trading symbol samco is",TrdSymbolSamco)
            urlpos1="/quote/getQuote?exchange=NFO&symbolName="+str(TrdSymbolSamco)
            #SStrike = text_box11.text() 
            current_price="0"
                        
            headerssamco = {
                "Content-Type": "application/json",
                "x-session-token": tokensam
                }
            payload = '' 
            conn.request("GET", urlpos1, payload, headerssamco)
            res = conn.getresponse()
            optiondata = res.read().decode()
                # Parse the JSON data
            response1_json = json.loads(optiondata)

            if response1_json['status'] == 'Success':
                    #print("success")
            #if response1_json.status == 'Success':
                    # Parse the quote response JSON and extract price
                    #quote_data = response1_json.json()
                    current_price = response1_json["lastTradedPrice"]
                    print("LTP of "+TrdSymbolSamco, current_price)                    
        except Exception as e:
            print("Exception while connection to GetLTP->socket: %s\n" % e)    
            # finally:
            # Release the lock
                # threading.Lock().release()           
        return str(current_price)
    
    

    
    # used by Get positions button
    def execute_curl_commandgetpos1(self):
        try:
              urlpos="https://gw-napi.kotaksecurities.com/Orders/2.0/quick/user/positions?sId="+newhsServerId
              urlpos1="/Orders/2.0/quick/user/positions?sId=server1"+str(newhsServerId)
              #s = requests.Session()
              AccessToken = "Bearer "+ accesstoken
                # Set up request headers
              headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Sid":newsid,
                "Auth":newtoken,
                "neo-fin-key":"neotradeapi",
                "accept":"application/json",
                "Authorization": AccessToken
               }
              conn = http.client.HTTPSConnection("gw-napi.kotaksecurities.com")
              payload = ''
              start_time = time.time()
              #conn.request("GET", "/Orders/2.0/quick/user/positions?sId=server1", payload, headers)
              conn.request("GET", urlpos1, payload, headers)
              res = conn.getresponse()
              #data = res.read()
              # Record the end time
              end_time = time.time()
                # Calculate the elapsed time
              elapsed_time = end_time - start_time

                # Print the elapsed time
              print(f"Elapsed time: {elapsed_time:.2f} seconds")
                
              posplaceddata = res.read().decode()
                # Parse the JSON data
              response1_json = json.loads(posplaceddata)
              response_data = response1_json

                # Initialize variables
              final_pnl = 0  # Final result variable
              final_qty_diff = 0
              qty_diff_list = []  # List to store qty_diff values
              trd_sym_list = []   # List to store trd_sym values
              results = []  # List to store individual results

              if 'data' in response_data:
                # The "data" field exists
                # Continue with your desired actions here

                    # Loop through each object in "data"
                for item in response_data["data"]:
                        # Extract the "buyAmt" and "sellAmt" as floats
                        buy_amt = float(item["buyAmt"])
                        sell_amt = float(item["sellAmt"])
                        # Calculate the difference between "buyAmt" and "sellAmt"
                        pnl = sell_amt - buy_amt

                        # Extract the "flBuyQty" and "flSellQty" as floats
                        fl_buy_qty = float(item["flBuyQty"])
                        fl_sell_qty = float(item["flSellQty"])
                        # Calculate the difference between "flBuyQty" and "flSellQty"
                        qty_diff = fl_buy_qty - fl_sell_qty
                        
                        # Get the "trdSym" field
                        trd_sym = item["trdSym"]
                        stkPrc = item["stkPrc"]
                        optTp = item["optTp"]
                        # Append qty_diff and trd_sym to their respective lists
                        qty_diff_list.append(qty_diff)
                        trd_sym_list.append(trd_sym)
                        # Append the result to the list and print it
                        result = {
                            "Symbol": stkPrc,
                            "Type": optTp,
                            "P&L": pnl
                        }
                        results.append(result)
                        print(f"Symbol: {stkPrc}{optTp}, P&L: {pnl},diffQty: {qty_diff}")

                        # Add the pnl to the final_pnl
                        final_pnl += pnl
                        final_qty_diff += qty_diff
                    # Print the final result
                # print(f"Final P&L: {final_pnl}")
                print(f"Final Qty Difference: {final_qty_diff}")
                #print(f"Time taken: {response1.elapsed}")

                print("final_pnl is ",final_pnl)
                #self.response_label.setText('pnl is '+str(final_pnl)+'res time is '+str(response1.elapsed))
                self.response_label.setText('pnl is '+str(final_pnl)+' resp time is '+f"Elapsed time: {elapsed_time:.2f} seconds")

                print("qty still open is ",final_qty_diff)

              else:
                print("No data available")
                self.response_label.setText("No data available")

        except Exception as e:
        #print("Exception while connection to socket->socket: %s\n" % e)
            print(f"Error executing command: {e}") 
        #close_qty_diff(qty_diff_list, trd_sym_list)
        return qty_diff_list, trd_sym_list


    def execute_curl_commandclosepos(self):
        nOrdNo = self.text_box3.text() # text box for cancelling order 
        self.execute_cancelorder(nOrdNo)
        AccessToken = "Bearer "+ accesstoken
                # Set up request headers
        headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Sid":newsid,
        "Auth":newtoken,
        "neo-fin-key":"neotradeapi",
        "accept":"application/json",
        "Authorization": AccessToken
        }
        httpurl = "/Orders/2.0/quick/order/rule/ms/place?sId="+ str(newhsServerId)
        conn = http.client.HTTPSConnection("gw-napi.kotaksecurities.com")
        elapsed_time =0
        try:
            max_qty = 900
            print("This below is not final_pnl  ")
            qty_diff_list, trd_sym_list = self.execute_curl_commandgetpos1()
            for i in range(len(qty_diff_list)):
                if qty_diff_list[i] > 0:
                    #if qty_diff_list[i] >= 0:
                    print(f"Symbol {trd_sym_list[i]} has Qty Difference > 0 and its: {qty_diff_list[i]}")
                    # Set containing decimal values
                    decimal_set = {qty_diff_list[i]}

                    # Convert the set to a set of integers using a loop
                    integer_set = set(int(value) for value in decimal_set)
                    # print(integer_set)
                    # print(decimal_set)
                    # Convert the set to a list
                    my_list = list(integer_set)
                    # Serialize the list to JSON
                    qtyjson_data = json.dumps(my_list)
                    # print(qtyjson_data)
                    # Parse the JSON string to a Python list
                    data_list = json.loads(qtyjson_data)
                    # Access the first element and convert it to an integer
                    plain_integer = int(data_list[0])
                    print(plain_integer)
                    sqqty = plain_integer
                    strikeset = {trd_sym_list[i]}
                    # Convert it to a plain string
                    trd_sym_str = strikeset.pop()

                    while sqqty > 0:
                        if sqqty >= max_qty:
                            es= "nse_fo"
                            mp= "0"
                            pc= "NRML"
                            pf= "N"
                            pr= "0"
                            pt= "MKT"
                            qt= str(max_qty)
                            rt= "DAY"
                            tp= "0"
                            Tradetype ="S"
                            sellpayld = 'jData=%7B%22am%22%3A%22NO%22%2C%20%22dq%22%3A%220%22%2C%22es%22%3A%22' + es + '%22%2C%20%22mp%22%3A%220%22%2C%20%22pc%22%3A%22' + pc + '%22%2C%20%22pf%22%3A%22N%22%2C%20%22pr%22%3A%22' + pr + '%22%2C%20%22pt%22%3A%22' + pt + '%22%2C%20%22qt%22%3A%22' + qt + '%22%2C%20%22rt%22%3A%22' + rt + '%22%2C%20%22tp%22%3A%22' + tp + '%22%2C%20%22ts%22%3A%22' + trd_sym_str + '%22%2C%20%22tt%22%3A%22' + Tradetype + '%22%7D'
                            
                            #print(f"Data: {form_data}")
                            # Send the request
                            # response = requests.post(url, headers=headers, data=form_data)
                            start_time = time.time()

                            conn.request("POST", httpurl , sellpayld, headers)
                            res = conn.getresponse()

                            # Record the end time
                            end_time = time.time()
                            # Calculate the elapsed time
                            elapsed_time = end_time - start_time
                            print(f"Elapsed time: {elapsed_time:.2f} seconds")
                            sellorderplaceddata = res.read().decode()
                            # Parse the JSON data
                            response_json = json.loads(sellorderplaceddata)

                            # Print the JSON response
                            print(response_json)
                            # reduce sqqty to below max qty
                            sqqty -= max_qty

                            print("Trading symbol was",{trd_sym_list[i]})

                        else:
                                es= "nse_fo"
                                mp= "0"
                                pc= "NRML"
                                pf= "N"
                                pr= "0"
                                pt= "MKT"
                                qt= str(sqqty)
                                rt= "DAY"
                                tp= "0"
                                Tradetype ="S"
                                sellpayld = 'jData=%7B%22am%22%3A%22NO%22%2C%20%22dq%22%3A%220%22%2C%22es%22%3A%22' + es + '%22%2C%20%22mp%22%3A%220%22%2C%20%22pc%22%3A%22' + pc + '%22%2C%20%22pf%22%3A%22N%22%2C%20%22pr%22%3A%22' + pr + '%22%2C%20%22pt%22%3A%22' + pt + '%22%2C%20%22qt%22%3A%22' + qt + '%22%2C%20%22rt%22%3A%22' + rt + '%22%2C%20%22tp%22%3A%22' + tp + '%22%2C%20%22ts%22%3A%22' + trd_sym_str + '%22%2C%20%22tt%22%3A%22' + Tradetype + '%22%7D'
                                
                                #print(f"Data: {form_data}")
                                # Send the request
                                # response = requests.post(url, headers=headers, data=form_data)
                                start_time = time.time()

                                conn.request("POST", httpurl , sellpayld, headers)
                                res = conn.getresponse()

                                # Record the end time
                                end_time = time.time()
                                # Calculate the elapsed time
                                elapsed_time = end_time - start_time
                                print(f"Elapsed time: {elapsed_time:.2f} seconds")
                                sellorderplaceddata = res.read().decode()
                                # Parse the JSON data
                                response_json = json.loads(sellorderplaceddata)

                                # Print the JSON response
                                print(response_json)
                                sqqty = 0
                                # print(response.text)
                                # placeholder = st.empty()
                                # Replace the chart with several elements:
                                # with placeholder.container():
                                # Print the API response
                                # st.write("sqqty is < max_qty")
                                # st.write("time taken to respond",response.elapsed)
                                print("Trading symbol was",{trd_sym_list[i]})
                                # st.write(form_data)
                                # st.write("API Response:")
                                # st.code(response.text, language="json")
                                #execute_curl_commandclosepos({trd_sym_list[i]},{qty_diff_list[i]})
                                # print(f"for Symbol  {trd_sym_list[i]} has Qty Difference > 0 and its: {qty_diff_list[i]}")  
                # else:  
                    # print(f"for Symbol {trd_sym_list[i]} has Qty Difference > 0 is: none : {qty_diff_list[i]} so no open positions")
            print("This is below is final_pnl ")
            self.execute_curl_commandgetpos1()
            # self.response_label_close.setText('positions closed')
            self.response_label_close.setText(f"Elapsed time: {elapsed_time:.2f} seconds")
            # self.response_label_close.setText('pnl is '+str(final_pnl)+' resp time is '+f"Elapsed time: {elapsed_time:.2f} seconds")                                                
        except Exception as e:
            print("Exception while connection cloase order to socket->socket: %s\n" % e)

    def execute_splitorder(self,intext,opttype,Tradetype,inqty,ind):     
        max_order_qty = 900
        lot_size = 15
        qty=int(inqty)
        while qty > 0: 
            if qty <= 900:
                self.execute_tradecall(intext,opttype,Tradetype,qty,ind)
                qty = 0 
            
            elif 1000 <= qty <= 20000:
                print("qty ",qty)
                num_calls = qty // 900  # Calculate the number of API calls
                count = int(float(num_calls)) # for e.g 3
                remaining_qty = qty % 900  # Calculate the remaining quantity
                print("count and remaing qty is ",count,remaining_qty)
                with ThreadPoolExecutor(max_workers=15) as executor:
                # Submit API calls to the executor
                # Create a list to store the submitted tasks
                    tasks = []
                
                    # Submit API calls to the executor
                    for _ in range(count):
                        task = executor.submit(self.execute_tradecall, intext, opttype, Tradetype, max_order_qty,ind)
                        # task = executor.submit(execute_tradecall_wrapper, intext, opttype, Tradetype, max_order_qty)
                        tasks.append(task)

                    concurrent.futures.wait(tasks)
                    
                    # concurrent.futures.wait(results)
                qty = remaining_qty    
            else:
                self.execute_tradecall(intext,opttype,Tradetype,max_order_qty,ind)
                qty -= max_order_qty                                 
      
                
    def execute_tradecall(self,intext,opttype,Tradetype,inqty,ind):
        global price
        # if self.checkbox.isChecked():
        #     tSymexpSS="NIFTY"+ stripped_date #"24117"  #24 YR 1 MO 17 DD   "24JAN"
        # else:
        #     tSymexpSS="BANKNIFTY"+ stripped_date #"24117"  #24 YR 1 MO 17 DD   "24JAN"
        if ind == 'NIFTY':
            stripped_date1= formatted_datethu
            tSymexpSS= ind + stripped_date1 #"BANKNIFTY"+ stripped_date # "24FEB" # "24117"  #24 YR 1 MO 17 DD   "24JAN"
        elif ind == 'FINNIFTY':
            stripped_date2= formatted_datetue 
            tSymexpSS= ind + stripped_date2 #"BANKNIFTY"+ stripped_date # "24FEB" # "24117"  #24 YR 1 MO 17 DD   "24JAN"
        elif ind == 'BANKNIFTY':
            stripped_date3= stripped_date   
            tSymexpSS= ind + stripped_date3 #"BANKNIFTY"+ stripped_date # "24FEB" # "24117"  #24 YR 1 MO 17 DD   "24JAN"  

        
        #s = requests.Session()
        url = "https://gw-napi.kotaksecurities.com/Orders/2.0/quick/order/rule/ms/place?sId="+ newhsServerId    
        httpurl = "/Orders/2.0/quick/order/rule/ms/place?sId="+ str(newhsServerId)
        # httpurl1 = "/Orders/2.0/quick/order/rule/ms/place?sId=server1"    
        conn = http.client.HTTPSConnection("gw-napi.kotaksecurities.com")   
        AccessToken = "Bearer "+ accesstoken
        # Set up request headers
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Sid":newsid,
            "Auth":newtoken,
            "neo-fin-key":"neotradeapi",
            "accept":"application/json",
            "Authorization": AccessToken
        }
        try:
            es= "nse_fo"
            mp= "0"
            pc= "NRML"
            pf= "N"
            pr= "0"
            pt= "MKT"
            qt= str(inqty)
            rt= "DAY"
            tp= "0"
        
            buypayld = 'jData=%7B%22am%22%3A%22NO%22%2C%20%22dq%22%3A%220%22%2C%22es%22%3A%22' + es + '%22%2C%20%22mp%22%3A%220%22%2C%20%22pc%22%3A%22' + pc + '%22%2C%20%22pf%22%3A%22N%22%2C%20%22pr%22%3A%22' + pr + '%22%2C%20%22pt%22%3A%22' + pt + '%22%2C%20%22qt%22%3A%22' + qt + '%22%2C%20%22rt%22%3A%22' + rt + '%22%2C%20%22tp%22%3A%22' + tp + '%22%2C%20%22ts%22%3A%22' + tSymexpSS+intext+opttype + '%22%2C%20%22tt%22%3A%22' + Tradetype + '%22%7D'
            #buypayld = 'jData=%7B%22am%22%3A%22NO%22%2C%20%22dq%22%3A%220%22%2C%22es%22%3A%22' + nse_fo + '%22%2C%20%22mp%22%3A%220%22%2C%20%22pc%22%3A%22' + NRML + '%22%2C%20%22pf%22%3A%22N%22%2C%20%22pr%22%3A%22' + 0 + '%22%2C%20%22pt%22%3A%22' + MKT + '%22%2C%20%22qt%22%3A%22' + inqty + '%22%2C%20%22rt%22%3A%22' + DAY + '%22%2C%20%22tp%22%3A%22' + 0 + '%22%2C%20%22ts%22%3A%22' + tSymexpSS+intext+opttype + '%22%2C%20%22tt%22%3A%22' + Tradetype + '%22%7D'
            # Record the start time
            start_time = time.time()

            conn.request("POST", httpurl , buypayld, headers)
            res = conn.getresponse()

            # Record the end time
            end_time = time.time()
            # Calculate the elapsed time
            elapsed_time = end_time - start_time
            intextn =intext+opttype
            # price= self.execute_curl_getLTP(intextn)
            print("intext is",intextn)
            print("trd symbol is",ind+stripped_date+intextn)
            # Print the elapsed time
            nowb = datetime.datetime.now()
            time_stringb = nowb.strftime("%H:%M:%S")
            print(f"Elapsed time: {elapsed_time:.2f} seconds at time {time_stringb}")
            # print("price would be at",price)
            orderplaceddata = res.read().decode()
            # Parse the JSON data
            response_json = json.loads(orderplaceddata)

            # Print the JSON response
            print(response_json)
            
            ordNo = response_json['nOrdNo']
              
            tSymexpSSamco="BANKNIFTY"+ formatted_date # "24FEB" # "17JAN24"  "24JAN"
            # if self.checkbox.isChecked():
            #     tSymexpSSamco="NIFTY"+ formatted_date #"17JAN24"  "24JAN"
            # else:
            #     tSymexpSSamco="BANKNIFTY"+ formatted_date #"17JAN24"  "24JAN"                
            TrdSymbolSamco = tSymexpSSamco+intext+opttype
            curr_price= self.execute_curl_getLTPL(TrdSymbolSamco) #executor.submit(self.execute_tradecall, intext, opttype, Tradetype, max_order_qty)
            # with ThreadPoolExecutor(max_workers=10) as executor1:
            #     curr_price= executor1.submit(self.execute_curl_getLTPL,TrdSymbolSamco)

            # with ThreadPoolExecutor(max_workers=10) as executor1:
            #     curr_price = executor1.submit(self.execute_curl_getLTPL, TrdSymbolSamco).result() 
            if Tradetype=='B':
                print("Buy Order no is :",ordNo)
                print("curr_price for buy is:",curr_price)
            else: 
                print("Sell Order no is :",ordNo) 
                print("curr_price for sell is:",curr_price)
            
            selllimitprice= int(float(curr_price)) + 5
            
            if self.checkbox1.isChecked():
                # self.text_boxslimit.setText(str(token))
                limitprc= str(float(self.doubleSpinBox.value()))
                selllimitprice= int(float(curr_price)) + int(float(limitprc))
                if Tradetype == 'B':
                    time.sleep(0.35)
                    self.execute_tradecallselllimit(intext,opttype,"S",inqty,selllimitprice,ind)
                    print("selllimitprice for sell is:",selllimitprice)
                    print("sell limit placed ")
            else:
                print("sell limit not placed ")        

            #stCode = response_json["stCode"]
            if opttype == 'CE' and Tradetype == 'B':
                self.response_label_order1.setText(f"Elapsed time: {elapsed_time:.2f} seconds")
            elif opttype == 'CE' and Tradetype == 'S':
                self.response_label_order2.setText(f"Elapsed time: {elapsed_time:.2f} seconds")
            elif opttype == 'PE' and Tradetype == 'B':
                self.response_label_order3.setText(f"Elapsed time: {elapsed_time:.2f} seconds")
            elif opttype == 'PE' and Tradetype == 'S':
                self.response_label_order4.setText(f"Elapsed time: {elapsed_time:.2f} seconds") 
            tSymexpSSamco="BANKNIFTY"+ formatted_date#"17JAN24"
            if  Tradetype =='B':  
                if self.checkbox1.isChecked():
                    print("SLTP called")
                    # self.execute_curl_setTPorSLn(tSymexpSSamco,intext,opttype)
                    # t = threading.Thread(target=self.execute_curl_setTPorSL(tSymexpSSamco,intext,opttype))
                    # t.start()
                else:
                    print("SLTP not called!")
            conn.close()        
        except Exception as e:
            print("Exception while connection to buy/sell order api->socket: %s\n" % e)

    def execute_tradecallselllimit(self,intext,opttype,Tradetype,inqty,selllimitprice,ind):
            global price
            # if self.checkbox.isChecked():
            #     tSymexpSS="NIFTY"+ stripped_date #"24117"  #24 YR 1 MO 17 DD   "24JAN"
            # else:
            #     tSymexpSS="BANKNIFTY"+ stripped_date #"24117"  #24 YR 1 MO 17 DD   "24JAN"
            tSymexpSS= ind + stripped_date #"BANKNIFTY"+ stripped_date #"24FEB" # "24117" # 24 year 1 month 10 exp date  "24JAN"
            #s = requests.Session()
            # url = "https://gw-napi.kotaksecurities.com/Orders/2.0/quick/order/rule/ms/place?sId="+ newhsServerId    
            httpurl = "/Orders/2.0/quick/order/rule/ms/place?sId="+ str(newhsServerId)
            # httpurl1 = "/Orders/2.0/quick/order/rule/ms/place?sId=server1"    
            conn = http.client.HTTPSConnection("gw-napi.kotaksecurities.com")   
            AccessToken = "Bearer "+ accesstoken
            # Set up request headers
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Sid":newsid,
                "Auth":newtoken,
                "neo-fin-key":"neotradeapi",
                "accept":"application/json",
                "Authorization": AccessToken
            }
            try:
                es= "nse_fo"
                mp= "0"
                pc= "NRML"
                pf= "N"
                pr= str(selllimitprice)
                pt= "L"
                qt= str(inqty)
                rt= "DAY"
                tp= "0"
                
                sellpayld = 'jData=%7B%22am%22%3A%22NO%22%2C%20%22dq%22%3A%220%22%2C%22es%22%3A%22' + es + '%22%2C%20%22mp%22%3A%220%22%2C%20%22pc%22%3A%22' + pc + '%22%2C%20%22pf%22%3A%22N%22%2C%20%22pr%22%3A%22' + pr + '%22%2C%20%22pt%22%3A%22' + pt + '%22%2C%20%22qt%22%3A%22' + qt + '%22%2C%20%22rt%22%3A%22' + rt + '%22%2C%20%22tp%22%3A%22' + tp + '%22%2C%20%22ts%22%3A%22' + tSymexpSS+intext+opttype + '%22%2C%20%22tt%22%3A%22' + Tradetype + '%22%7D'
                #buypayld = 'jData=%7B%22am%22%3A%22NO%22%2C%20%22dq%22%3A%220%22%2C%22es%22%3A%22' + nse_fo + '%22%2C%20%22mp%22%3A%220%22%2C%20%22pc%22%3A%22' + NRML + '%22%2C%20%22pf%22%3A%22N%22%2C%20%22pr%22%3A%22' + 0 + '%22%2C%20%22pt%22%3A%22' + MKT + '%22%2C%20%22qt%22%3A%22' + inqty + '%22%2C%20%22rt%22%3A%22' + DAY + '%22%2C%20%22tp%22%3A%22' + 0 + '%22%2C%20%22ts%22%3A%22' + tSymexpSS+intext+opttype + '%22%2C%20%22tt%22%3A%22' + Tradetype + '%22%7D'
                # Record the start time
                start_time = time.time()

                conn.request("POST", httpurl , sellpayld, headers)
                res = conn.getresponse()

                # Record the end time
                end_time = time.time()
                # Calculate the elapsed time
                elapsed_time = end_time - start_time

                nows = datetime.datetime.now()
                time_strings = nows.strftime("%H:%M:%S")
                print(f"Elapsed time: {elapsed_time:.2f} seconds at time {time_strings}")
                # print("price would be at",price)
                orderplaceddata = res.read().decode()
                # Parse the JSON data
                response_json = json.loads(orderplaceddata)

                # Print the JSON response
                print(response_json)
                SordNo = response_json['nOrdNo']
                print("Sell limit Order no is :",SordNo)
                self.text_box3.setText(SordNo) # setting this field with oprdno to keep the cancel options ready 
                tSymexpSSamco="BANKNIFTY"+ "24FEB" #formatted_date #"17JAN24"
                TrdSymbolSamco = tSymexpSSamco+intext+opttype
                # curr_price= self.execute_curl_getLTPL(TrdSymbolSamco)
                # print("curr_price for sell is:",curr_price)
                # curr_price=str(int(float(curr_price)))
                self.text_box31.setText(SordNo)
                self.text_box32.setText(qt) # qty which we just set limit ordder 
                self.text_box33.setText(str(selllimitprice))
                token, trdsym= self.execute_orderbook(SordNo)
                # ordersplaced = self.orderbook()
                # print("Orderbook fetched at ",datetime.datetime.now())

                # orderlen = len(ordersplaced['data'])
                # self.token = ordersplaced['data'][orderlen-1]['tok']
                self.text_box35.setText(str(token))
                self.text_box34.setText(str(trdsym))

            except Exception as e:
                print("Exception while connection to sell limit order api->socket: %s\n" % e)         

    def increment_value1(self, text_box1):
        current_value1 = int(text_box1.text())
        new_value1 = current_value1 + 100
        text_box1.setText(str(new_value1))

    def decrement_value1(self, text_box1):
        current_value1 = int(text_box1.text())
        new_value1 = current_value1 - 100
        text_box1.setText(str(new_value1))

    def increment_value(self, text_box):
        current_value = int(text_box.text())
        new_value = current_value + 150
        text_box.setText(str(new_value))

    def decrement_value(self, text_box):
        current_value = int(text_box.text())
        new_value = current_value - 150
        text_box.setText(str(new_value))

    def increment_value2(self, text_box):
        current_value = int(text_box.text())
        new_value = current_value + 1
        text_box.setText(str(new_value))

    def decrement_value2(self, text_box):
        current_value = int(text_box.text())
        new_value = current_value - 1
        text_box.setText(str(new_value)) 
    # def process_values(self):
    #     value1 = int(self.text_box2.text())
    #     value2 = int(self.text_box22.text())
        # print("value1",value1)
        # print("value2",value2)
        # Perform actions based on value1 and other values       

class frstwindow(QWidget):
    #global accesstoken
    def __init__(self):
        super().__init__()
        self.resize(300, 150)
        self.setWindowTitle("Kotak NEO Client")
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        buttonlogin = QPushButton("Login to kotak", self)
        buttonlogin.clicked.connect(self.login)
        buttonlogin.move(95, 92)
        buttonzgentok = QPushButton("AccessToken", self)
        buttonzgentok.clicked.connect(self.zgentoken)
        buttonzgentok.move(95, 12)
        # self.zrestok = QtWidgets.QLineEdit(self)
        # self.zrestok.setGeometry(QtCore.QRect(95, 52, 150, 30))

    def zgentokenthread(self):
        # kotaklogin.
        my_object = self.kotaklogin()
        my_object.main() 
        

    def zgentoken(self):
        t = threading.Thread(target=self.zgentokenthread)
        t.start()

    def login(self):
        #global newtoken, newsid, newhsServerId, tokensam

        global newtoken, newsid, newhsServerId, accesstoken , tokensam  
        with open("cred.json", "r") as f:
            data = json.load(f)

        newtoken = data["token"]
        newsid = data["id"]
        newhsServerId = data["hsid"]
        accesstoken= data["accesstoken"]
        tokensam= data["tokensam"]

        self.close()
        self.win = MyWidget()
        self.win.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    # window = MyWidget()
    window = frstwindow()
    window.show()
    app.exec_()     
    # sys.exit(app.exec())   