import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stencilview import StencilView
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics import *
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


#Sam for the SQL lite database I really just need databases for Class, Student, and the classes array contained in mainscreen at 189
#they're all just arrays of values so I hope this is a good way to interface with it.
class Class(object):
    def __init__(self, name):
        self.students = []
        self.name = name

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_name(self):
        return self.name

    def get_self(self):
        return self



class Student(object):
    def __init__(self, name, age, gender, miletimemin, miletimesec, pushups, curlups, stretchl, stretchr):
        self.name = name
        self.age = age
        self.gender = gender
        self.miletime_min = miletimemin
        self.miletime_sec = miletimesec
        self.pushups = pushups
        self.curlups = curlups
        self.stretchl = stretchl
        self.stretchr = stretchr

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_name(self):
        return self.name

    def get_miletime(self):
        return str(self.miletime_min) +':'+ str(self.miletime_sec)

    def get_pushups(self):
        return self.pushups

    def get_curlups(self):
        return self.curlups

    def get_stretchl(self):
        return self.stretchl

    def get_stretchr(self):
        return self.stretchr

    def get_self(self):
        return self



#This loads when the class menu items are chosen
#For some reason the buttons in the first column don't space like everything else. Figure this out.
#We should probably figure out how to judge student scores based on the conneticut criteria and then color the numbers in this screen
#red for fail, green for pass, and then maybe gold for the super great standard that i think there is
class ReportScreen(FloatLayout):
    def __init__(self, classname, parent = None, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)
        self.students = classname.students
        self.parent = parent
        studentlayout = BoxLayout(orientation='vertical', spacing = 10, size_hint_x = 2)
        overalllayout = BoxLayout(orientation='horizontal', pos=(Window.width/10,Window.height/5), size=(Window.width - Window.width/5, Window.height - Window.height/5))
        studentgenderlayout = BoxLayout(orientation='vertical')
        studentagelayout = BoxLayout(orientation='vertical')
        miletimelayout = BoxLayout(orientation = 'vertical')
        pushupslayout = BoxLayout(orientation = 'vertical')
        curlupslayout = BoxLayout(orientation = 'vertical')
        stretchlayout = BoxLayout(orientation = 'vertical')
        genderlabel = Label(text = 'Gender')
        studentnamelabel = Label(text = '')
        agelabel = Label(text = 'Age')
        miletimelabel = Label(text = 'Mile Time')
        pushupslabel = Label(text = 'Push Ups')
        curlupslabel = Label(text = 'Curl Ups')
        stretchlabel = Label(text = 'Stretch L/R')
        studentlayout.add_widget(studentnamelabel)
        studentgenderlayout.add_widget(genderlabel)
        studentagelayout.add_widget(agelabel)
        miletimelayout.add_widget(miletimelabel)
        pushupslayout.add_widget(pushupslabel)
        curlupslayout.add_widget(curlupslabel)
        stretchlayout.add_widget(stretchlabel)

        #This loop adds in the scores for each student
        for x in self.students:
            labelname1 = Button(text = x.get_name(), background_normal='buttons/button_normal.png', background_down='buttons/button_down.png') 
            labelname1.bind(on_release=self.parent.student_callback)
            labelname2 = Label(text = x.get_gender()) 
            labelname3 = Label(text = str(x.get_age()))
            labelname4 = Label(text = x.get_miletime())
            labelname5 = Label(text = str(x.get_pushups()))  
            labelname6 = Label(text = str(x.get_curlups()))
            labelname7 = Label(text = str(x.get_stretchl()) + '/' + str(x.get_stretchr())) 

            #Color Text Based on Scores, this is just sample code. We need to expand this based on the standards and age
            #Pass
            if x.get_pushups() >= 0:
                labelname5.color = (0.031372549, 0.768627451, 0.109803922, 1)
            #Fail
            if x.get_curlups() <= 10:
                labelname6.color = (0.82745098, 0.003921569, 0.02745098, 1)

            #Super Saiyan
            if x.get_miletime() >= 0:
                labelname4.color = (1, 0.847058824, 0.109803922, 1)

            studentlayout.add_widget(labelname1)
            studentgenderlayout.add_widget(labelname2)
            studentagelayout.add_widget(labelname3)
            miletimelayout.add_widget(labelname4)
            pushupslayout.add_widget(labelname5)
            curlupslayout.add_widget(labelname6)
            stretchlayout.add_widget(labelname7)



        overalllayout.add_widget(studentlayout)
        overalllayout.add_widget(studentgenderlayout)
        overalllayout.add_widget(studentagelayout)
        overalllayout.add_widget(miletimelayout)
        overalllayout.add_widget(pushupslayout)
        overalllayout.add_widget(curlupslayout)
        overalllayout.add_widget(stretchlayout)
        self.add_widget(overalllayout)


#This loads when a student is selected from the Report Screen
#Some alignment and centering issues in this class
#Call back functions need to be added to the activity buttons, should be added in MainScreen NOT in this class. See line 111 for an example
#These functions should bring up a popup prompting for the correct unit input. Stretch needs to have Left and Right Separately but
#in the same popup
#I will create art for the buttons missing
class StudentScreen(FloatLayout):
    def __init__(self, student, parent = None, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)
        self.student = student
        parent = parent
        name = self.student.get_name()
        gender = self.student.get_gender()
        age = self.student.get_age()
        mile_time = self.student.get_miletime()
        curlups = self.student.get_curlups()
        stretchl = self.student.get_stretchl()
        stretchr = self.student.get_stretchr()
        pushups = self.student.get_pushups()
        top_boxlayout = BoxLayout(orientation = 'horizontal', spacing = Window.width/15, size = (Window.width - Window.width/5., Window.height/10.), pos = (Window.width/10, Window.height - Window.height/10))
        genderlabel = Label(text = gender)
        studentnamelabel = Label(text = name)
        agelabel = Label(text = 'Age: ' + str(age))
        top_boxlayout.add_widget(studentnamelabel)
        top_boxlayout.add_widget(agelabel)
        top_boxlayout.add_widget(genderlabel)
        main_boxlayout = BoxLayout(orientation = 'horizontal', spacing = (Window.width - Window.width/3.5 - 400.), size =(Window.width - Window.width/3.5, Window.height - Window.height/3.33), pos = (Window.width/7., Window.height/6.66))
        column1 = BoxLayout(orientation = 'vertical')
        column2 = BoxLayout(orientation = 'vertical')
        milelabel = Label(text = 'Mile Time: ' + mile_time)
        pushupslabel = Label(text = 'Push-ups: ' +str(pushups))
        curlupslabel = Label(text = 'Curl-ups: ' +str(curlups))
        stretchlabel = Label(text = 'Stretch L/R: ' +str(stretchl) + '/' + str(stretchr))
        milebutton = Button(text = 'Mile Run', size_hint_y = None, height=157, width = 200 , valign = 'bottom', background_normal='buttons/runninglogo.png', text_size = (None, self.height*1.3))
        pushupsbutton = Button(text ='Push-Ups', size_hint_y = None, height=157, width = 200, valign = 'bottom', background_normal='buttons/pushuplogo.png', text_size = (None, self.height*1.3))
        curlupsbutton = Button(text = 'Curl-Ups', size_hint_y = None, height=157, width = 200 , valign = 'bottom', background_normal='buttons/curlupslogo.png', text_size = (None, self.height*1.3))
        stretchbutton = Button(text = 'Sit-and-Reach', size_hint_y = None, height=157, width = 200, valign = 'bottom', background_normal='buttons/sitandreachlogo.png', text_size = (None, self.height*1.3))
        pushupsbutton.bind(on_release = parent.studentscreen_callback)
        curlupsbutton.bind(on_release = parent.studentscreen_callback)
        milebutton.bind(on_release = parent.studentscreen_callback)
        stretchbutton.bind(on_release = parent.studentscreen_callback)
        column1.add_widget(milebutton)
        column1.add_widget(milelabel)
        column1.add_widget(pushupsbutton)
        column1.add_widget(pushupslabel)
        column2.add_widget(curlupsbutton)
        column2.add_widget(curlupslabel)
        column2.add_widget(stretchbutton)
        column2.add_widget(stretchlabel)
        main_boxlayout.add_widget(column1)
        main_boxlayout.add_widget(column2)
        self.add_widget(top_boxlayout)
        self.add_widget(main_boxlayout)
        
#MainScreen is the first screen that shows up as well as the class that controls which menu options show up and how.
#All button functions should occur in this class

class CsvReader():
    def __init__(self,csvfile):
        self.reader = open(csvfile,'r')
        
    def get_classes(self):
        classes = []
        for line in self.reader:
            print line
            #assume that if : is in a line, it is a class name
            if line.strip() == '':
                pass
            elif ':' in line:
                classes.append(Class(line.rstrip(':\n')))            
            else:
                splitline = [x.strip() for x in line.split(',')]
                classes[-1].add_student(Student(splitline[0],splitline[1],splitline[2], splitline[3], splitline[4], splitline[5], splitline[6], splitline[7], splitline[8]))
        return classes
                

class MainScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)
        self.classes = []

        reader = CsvReader('classes.csv')
        self.classes = reader.get_classes()
        self.menu_width = Window.width *.40
        self.menu_height = Window.height *.66
        self.menu_x = Window.width *.30
        self.menu_y = Window.height *.10
        self.popup_height = Window.height *.50
        self.popup_height2 = Window.height * .33
        self.popup_y = Window.height *.45
        self.currentclass = None
        self.menu = BoxLayout(orientation= 'vertical',spacing = Window.height/50., size = (self.menu_width, self.menu_height), pos = (self.menu_x, self.menu_y))
        for each in self.classes:
            button = Button(text=each.get_name(), size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
            button.bind(on_release=self.callback)
            #This is the corresponding code to load a class see line #224
            self.menu.add_widget(button)
        self.addclassbutton = Button(text='Add Class', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.addclassbutton.bind(on_release=self.callback)
        self.menu.add_widget(self.addclassbutton)
        self.removeclassbutton = Button(text='Remove Class', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.removeclassbutton.bind(on_release=self.callback)
        self.menu.add_widget(self.removeclassbutton)
        self.redraw_canvas()
        self.draw_logo()

    def callback(self, instance):
        print instance.text
        if instance.text == 'Add Class':
            self.add_class()
        if instance.text == 'Create Class':
            print 'Dismissing popup'
            print self.textinput.text
            self.create_class(self.textinput.text)
            self.addclass_popup.dismiss()

        if instance.text == 'Remove Class':
            self.remove_class()

        else:
            classname = 'self.' + instance.text
            for each in self.classes:
                internalclassname = 'self.' + each.get_name()
                if classname == internalclassname:
                    self.draw_report(each.get_self())

    def student_callback(self, instance):
        print instance.text

        studentname = 'self.' + instance.text
        for each in self.currentclass.students:
            internalstudentname = 'self.' + each.get_name()
            if studentname == internalstudentname:
                self.draw_studentscreen(each.get_self())

    def studentscreen_callback(self, instance):
        print instance.text
        if instance.text == 'Edit Information':
            self.edit_information_button()
        if instance.text  == 'Update Student':
            self.update_information(self.studentnameinput.text, self.studentageinput.text, self.studentgenderinput.text)
        if instance.text == 'Back':
            self.remove_widget(self.studentscreen)
            self.draw_report(self.currentclass)
        if instance.text == 'Mile Run':
            self.mile_run_button()
        if instance.text  == 'Input Mile Score':
            self.update_miles(self.minutesinput.text, self.secondsinput.text)
        if instance.text == 'Sit-and-Reach':
            self.stretch_button()
        if instance.text  == 'Input Sit-and-Reach Score':
            self.update_stretch(self.stretchlinput.text, self.stretchrinput.text)
        if instance.text == 'Curl-Ups':
            self.curlups_button()
        if instance.text  == 'Input Curl-Ups Score':
            self.update_curlups(self.curlupsinput.text)
        if instance.text == 'Push-Ups':
            self.pushups_button()
        if instance.text  == 'Input Push-Ups Score':
            self.update_pushups(self.pushupsinput.text)

    def edit_information_button(self):
        popupmenu =  BoxLayout(orientation= 'vertical',spacing = Window.height/50., size = (self.menu_width, self.popup_height), pos = (self.menu_x, self.popup_y))
        
        popuplabel1 = Label(text='Name:')
        popuplabel2 = Label(text='Student age:')
        popuplabel3 = Label(text='Student gender:')
        self.studentnameinput = TextInput(multiline = False, text = self.currentstudent.get_name())
        self.studentageinput = TextInput(multiline = False, text = str(self.currentstudent.get_age()))
        self.studentgenderinput = TextInput(multiline = False, text = self.currentstudent.get_gender())
        popupmenu.add_widget(popuplabel1)
        popupmenu.add_widget(self.studentnameinput)
        popupmenu.add_widget(popuplabel2)
        popupmenu.add_widget(self.studentageinput)
        popupmenu.add_widget(popuplabel3)
        popupmenu.add_widget(self.studentgenderinput)
        dismissbutton = Button(text='Update Student', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        popupmenu.add_widget(dismissbutton)
        dismissbutton.bind(on_release=self.studentscreen_callback)
        self.updatestudent_popup = Popup(title='Update Student Information', size_hint=(None,None), pos_hint = {'x': .30, 'y':.45}, size = (self.menu_width, self.popup_height), content = popupmenu)
        self.updatestudent_popup.open()


    def update_information(self, textinput1, textinput2, textinput3):
        self.currentstudent.name = textinput1
        self.currentstudent.age = int(textinput2)
        self.currentstudent.gender = textinput3
        self.draw_studentscreen(self.currentstudent)
        self.updatestudent_popup.dismiss()

    def mile_run_button(self):
        popupmenu =  BoxLayout(orientation= 'vertical',spacing = Window.height/50., size = (self.menu_width, self.popup_height2), pos = (self.menu_x, self.popup_y))
        popuplabel1 = Label(text='Minutes:')
        popuplabel2 = Label(text='Seconds:')
        self.minutesinput = TextInput(multiline = False)
        self.secondsinput = TextInput(multiline = False)
        popupmenu.add_widget(popuplabel1)
        popupmenu.add_widget(self.minutesinput)
        popupmenu.add_widget(popuplabel2)
        popupmenu.add_widget(self.secondsinput)
        inputscorebutton = Button(text='Input Mile Score', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        popupmenu.add_widget(inputscorebutton)
        inputscorebutton.bind(on_release=self.studentscreen_callback)
        self.updatemiles_popup = Popup(title='Record Mile Score', size_hint=(None,None),pos_hint = {'x': .30, 'y':.45}, size = (self.menu_width, self.popup_height2), content = popupmenu)
        self.updatemiles_popup.open()

    def update_miles(self, textinput1, textinput2):
        self.currentstudent.miletime_min = int(textinput1)
        self.currentstudent.miletime_sec = int(textinput2)
        self.draw_studentscreen(self.currentstudent)
        self.updatemiles_popup.dismiss()

    def stretch_button(self):
        popupmenu =  BoxLayout(orientation= 'vertical',spacing = Window.height/50., size = (self.menu_width, self.popup_height2), pos = (self.menu_x, self.popup_y))
        popuplabel1 = Label(text='Stretch L')
        popuplabel2 = Label(text='Stretch R')
        self.stretchlinput = TextInput(multiline = False)
        self.stretchrinput = TextInput(multiline = False)
        popupmenu.add_widget(popuplabel1)
        popupmenu.add_widget(self.stretchlinput)
        popupmenu.add_widget(popuplabel2)
        popupmenu.add_widget(self.stretchrinput)
        inputscorebutton = Button(text='Input Sit-and-Reach Score', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        popupmenu.add_widget(inputscorebutton)
        inputscorebutton.bind(on_release=self.studentscreen_callback)
        self.updatemiles_popup = Popup(title='Record Sit-and-Reach Score', size_hint=(None,None),pos_hint = {'x': .30, 'y':.45}, size = (self.menu_width, self.popup_height2), content = popupmenu)
        self.updatemiles_popup.open()

    def update_stretch(self, textinput1, textinput2):
        self.currentstudent.stretchl = int(textinput1)
        self.currentstudent.stretchr = int(textinput2)
        self.draw_studentscreen(self.currentstudent)
        self.updatemiles_popup.dismiss()

    def curlups_button(self):
        popupmenu =  BoxLayout(orientation= 'vertical',spacing = Window.height/50., size = (self.menu_width, self.popup_height2), pos = (self.menu_x, self.popup_y))
        popuplabel1 = Label(text='Curl-Ups')
        self.curlupsinput = TextInput(multiline = False)
        popupmenu.add_widget(popuplabel1)
        popupmenu.add_widget(self.curlupsinput)
        inputscorebutton = Button(text='Input Curl-Ups Score', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        popupmenu.add_widget(inputscorebutton)
        inputscorebutton.bind(on_release=self.studentscreen_callback)
        self.updatecurlups_popup = Popup(title='Record Curl-Ups Score', size_hint=(None,None),pos_hint = {'x': .30, 'y':.45}, size = (self.menu_width, self.popup_height2), content = popupmenu)
        self.updatecurlups_popup.open()

    def update_curlups(self, textinput1):
        self.currentstudent.curlups = int(textinput1)
        self.draw_studentscreen(self.currentstudent)
        self.updatecurlups_popup.dismiss()

    def pushups_button(self):
        popupmenu =  BoxLayout(orientation= 'vertical',spacing = Window.height/50., size = (self.menu_width, self.popup_height2), pos = (self.menu_x, self.popup_y))
        popuplabel1 = Label(text='Push-Ups')
        self.pushupsinput = TextInput(multiline = False)
        popupmenu.add_widget(popuplabel1)
        popupmenu.add_widget(self.pushupsinput)
        inputscorebutton = Button(text='Input Push-Ups Score', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        popupmenu.add_widget(inputscorebutton)
        inputscorebutton.bind(on_release=self.studentscreen_callback)
        self.updatepushups_popup = Popup(title='Record Push-Ups Score', size_hint=(None,None),pos_hint = {'x': .30, 'y':.45}, size = (self.menu_width, self.popup_height2), content = popupmenu)
        self.updatepushups_popup.open()

    def update_pushups(self, textinput1):
        self.currentstudent.pushups = int(textinput1)
        self.draw_studentscreen(self.currentstudent)
        self.updatepushups_popup.dismiss()


    #Needs a callback for edit_student_button which brings up the fields for name, age, and gender, and then write sthem back
    #see create class in callback function for a similar problem
    def draw_studentscreen(self, studentname):
        self.redraw_canvas()
        self.remove_widget(self.menu)
        self.currentstudent = studentname
        self.studentscreen = StudentScreen(studentname, parent = self)
        self.menu = BoxLayout(orientation = 'horizontal', spacing = Window.width/20., size = (Window.width - Window.width/10, Window.height/10), pos = (Window.width/15, Window.height/30))
        self.edit_student_button = Button(text='Edit Information', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.back_button = Button(text='Back', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.menu.add_widget(self.edit_student_button)
        self.menu.add_widget(self.back_button)
        self.edit_student_button.bind(on_release=self.studentscreen_callback)
        self.back_button.bind(on_release=self.studentscreen_callback)
        self.add_widget(self.menu)
        self.add_widget(self.studentscreen)

    #Needs a callback for add_student_button and remove_student_button which brings up the fields for name, age, and gender, and then write sthem back
    #see create class and remove class (when this is fixed) in callback function for a similar problem
    def draw_report(self, classname):
        self.redraw_canvas()
        self.remove_widget(self.menu)
        self.report = ReportScreen(classname, parent = self)
        self.currentclass = classname
        self.menu = BoxLayout(orientation = 'horizontal', spacing = Window.width/20., size = (Window.width - Window.width/10, Window.height/10), pos = (Window.width/15, Window.height/30))
        self.add_student_button = Button(text='Add Student', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.remove_student_button = Button(text='Remove Student', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.back_button = Button(text='Back', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.menu.add_widget(self.add_student_button)
        self.menu.add_widget(self.remove_student_button)
        self.menu.add_widget(self.back_button)
        self.add_student_button.bind(on_release=self.report_callback)
        self.remove_student_button.bind(on_release=self.report_callback)
        self.back_button.bind(on_release=self.report_callback)
        self.add_widget(self.menu)
        self.add_widget(self.report)

    def report_callback(self, instance):
        print instance.text
        if instance.text == 'Back':
            self.remove_widget(self.report)
            self.reload_menu()
            self.redraw_canvas()
            self.draw_logo()

        if instance.text == 'Add Student':
            self.add_student()

        if instance.text == 'Remove Student':
            self.remove_student()

        if instance.text == 'Create Student':
            self.create_student(self.studentnameinput.text, int(self.studentageinput.text), self.studentgenderinput.text)
            self.addstudent_popup.dismiss()

    def remove_student(self):
        popupmenu =  BoxLayout(orientation= 'vertical',spacing = Window.height/50., size = (self.menu_width, self.popup_height), pos = (self.menu_x, self.popup_y))
        for each in self.currentclass.students:
            studentbutton = Button(text=each.get_name(), size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
            studentbutton.bind(on_release=self.removestudent_callback)
            popupmenu.add_widget(studentbutton)
        backbutton = Button(text='Back', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        popupmenu.add_widget(backbutton)
        self.removestudent_popup = Popup(title='Remove Student', size_hint=(None,None), size = (self.menu_width, self.popup_height), content = popupmenu)
        backbutton.bind(on_release=self.removestudent_callback)
        self.removestudent_popup.open()

    def removestudent_callback(self, instance):
        studentname = instance.text
        if instance.text == 'Back':
            self.removestudent_popup.dismiss()
        else:
            for each in self.currentclass.students:
                internalstudentname = each.get_name()
                if studentname == internalstudentname:
                    self.currentclass.students.remove(each.get_self())
                    self.draw_report(self.currentclass)
                    self.removestudent_popup.dismiss()

    def add_student(self):
        print 'pop up'
        popupmenu =  BoxLayout(orientation= 'vertical',spacing = Window.height/50., size = (self.menu_width, self.popup_height), pos = (self.menu_x, self.popup_y))
        
        popuplabel1 = Label(text='Name the student:')
        popuplabel2 = Label(text='Student age:')
        popuplabel3 = Label(text='Student gender:')
        self.studentnameinput = TextInput(multiline = False)
        self.studentageinput = TextInput(multiline = False)
        self.studentgenderinput = TextInput(multiline = False)
        popupmenu.add_widget(popuplabel1)
        popupmenu.add_widget(self.studentnameinput)
        popupmenu.add_widget(popuplabel2)
        popupmenu.add_widget(self.studentageinput)
        popupmenu.add_widget(popuplabel3)
        popupmenu.add_widget(self.studentgenderinput)
        dismissbutton = Button(text='Create Student', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        popupmenu.add_widget(dismissbutton)
        dismissbutton.bind(on_release=self.report_callback)
        self.addstudent_popup = Popup(title='Add Student', size_hint=(None,None),pos_hint = {'x': .30, 'y':.45}, size = (self.menu_width, self.popup_height), content = popupmenu)
        self.addstudent_popup.open()

    def create_student(self, textinput1, textinput2, textinput3):
        student = Student(textinput1, textinput2, textinput3, 0, 0, 0, 0, 0, 0)
        self.currentclass.students.append(student)
        self.draw_report(self.currentclass)

            

    def draw_logo(self):

        logo_width = Window.width/20
        logo_height = Window.height - Window.height/4

        with self.canvas:
            Color(1.,1.,1.,1.)
            Rectangle(source = 'schoollogo/schoollogo.png', size = (676, 126), pos = (logo_width, logo_height))
            Rectangle(size = (Window.width, Window.height/50), pos = (0,(Window.height - Window.height/3.45)))
            Color(0.360784314, 0.058823529, 0.121568627, 1)
            Rectangle(size = (Window.width, Window.height/80), pos = (0, (Window.height - Window.height/3.5)))


    def redraw_canvas(self):

        self.remove_widget(self.menu)

        with self.canvas:
            Color(0.031372549, 0.11372549, 0.352941176, 1)
            Rectangle(size = (Window.width, Window.height), pos = (0, 0))

        self.add_widget(self.menu)

    def redraw_logo(self):
        self.remove_widget(self.menu)

        with self.canvas:
            Color(1.,1.,1.,1.)
            Rectangle(source = 'schoollogo/schoollogo.png', size = (676, 126), pos = (logo_width, logo_height))
            Rectangle(size = (Window.width, Window.height/50), pos = (0,(Window.height - Window.height/3.45)))
            Color(0.360784314, 0.058823529, 0.121568627, 1)
            Rectangle(size = (Window.width, Window.height/80), pos = (0, (Window.height - Window.height/3.5)))

        self.add_widget(self.menu)
        
    #I will update popup graphics to fit the scheme of things
    def add_class(self):
        print 'pop up'
        popupmenu =  BoxLayout(orientation= 'vertical',spacing = Window.height/50., size = (self.menu_width, self.popup_height2), pos = (self.menu_width, self.popup_y))
        popuplabel = Label(text='Name the class:')
        self.textinput = TextInput(focus = True, multiline = False)
        popupmenu.add_widget(popuplabel)
        popupmenu.add_widget(self.textinput)
        dismissbutton = Button(text='Create Class', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        popupmenu.add_widget(dismissbutton)
        dismissbutton.bind(on_release=self.callback)
        self.addclass_popup = Popup(title='Add Class', size_hint=(None,None),pos_hint = {'x': .30, 'y':.45}, size=(self.menu_width, self.popup_height2), content = popupmenu)
        self.addclass_popup.open()

    #should remove the class specified from the self.classes array, however I cannot figure out how to name the object correctly
    def removeclass_callback(self, instance):
        if instance.text == 'Back':
            self.removeclass_popup.dismiss()
        else:
            classname = instance.text
            for each in self.classes:
                internalclassname = each.get_name()
                if classname == internalclassname:
                    self.classes.remove(each.get_self())
                    self.reload_menu()
            self.removeclass_popup.dismiss()

    #This function loads the list of classes in and then binds remove_callback 
    def remove_class(self):
        popupmenu =  BoxLayout(orientation= 'vertical',spacing = Window.height/50., size = (self.menu_width, self.popup_height), pos = (self.menu_x, self.popup_y))
        for each in self.classes:
            classbutton = Button(text=each.get_name(), size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
            classbutton.bind(on_release=self.removeclass_callback)
            popupmenu.add_widget(classbutton)
        backbutton = Button(text='Back', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        popupmenu.add_widget(backbutton)
        self.removeclass_popup = Popup(title='Remove Student', size_hint=(None,None), size = (self.menu_width, self.popup_height), content = popupmenu)
        backbutton.bind(on_release=self.removeclass_callback)
        self.removeclass_popup.open()




    def create_class(self, textinput):
        classname = Class(textinput)
        self.classes.append(classname)
        self.reload_menu()

    def reload_menu(self):
        self.remove_widget(self.menu)
        self.menu = BoxLayout(orientation= 'vertical',spacing = Window.height/50., size = (self.menu_width, self.menu_height), pos = (self.menu_x, self.menu_y))
        for each in self.classes:
            classbutton = Button(text=each.get_name(), size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
            classbutton.bind(on_release=self.callback)
            self.menu.add_widget(classbutton)
        self.menu.add_widget(self.addclassbutton)
        self.menu.add_widget(self.removeclassbutton)
        self.add_widget(self.menu)






class MenuTestApp(App):
    def build(self):
        mainscreen = MainScreen(pos=(0,0),size=Window.size)
        return mainscreen
        

if __name__ in ('__android__', '__main__'):
    MenuTestApp().run()
