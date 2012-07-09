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
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.miletime = 0
        self.pushups = 0
        self.curlups = 0
        self.stretchl = 0
        self.stretchr = 0

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_name(self):
        return self.name

    def get_miletime(self):
        return self.miletime

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
        students = classname.students
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
        for x in students:
            labelname1 = Button(text = x.get_name(), background_normal='buttons/button_normal.png', background_down='buttons/button_down.png') 
            labelname1.bind(on_press=self.parent.student_callback)
            labelname2 = Label(text = x.get_gender()) 
            labelname3 = Label(text = str(x.get_age()))
            labelname4 = Label(text = str(x.get_miletime()))
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
    def __init__(self, student, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)
        self.student = student
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
        milelabel = Label(text = 'Mile Time: ' +str(mile_time))
        pushupslabel = Label(text = 'Push-ups: ' +str(pushups))
        curlupslabel = Label(text = 'Curl-ups: ' +str(curlups))
        stretchlabel = Label(text = 'Stretch L/R: ' +str(stretchl) + '/' + str(stretchr))
        milebutton = Button(text = 'Mile Run', size_hint_y = None, height=157, width = 200 , valign = 'bottom', background_normal='buttons/runninglogo.png', text_size = (None, self.height*1.3))
        pushupsbutton = Button(text ='Push-Ups', size_hint_y = None, height=157, width = 200, valign = 'bottom', background_normal='buttons/pushuplogo.png', text_size = (None, self.height*1.3))
        curlupsbutton = Button(text = 'Curl-Ups', size_hint_y = None, height=157, width = 200 , valign = 'bottom', background_normal='buttons/curlupslogo.png', text_size = (None, self.height*1.3))
        stretchbutton = Button(text = 'Sit-and-Reach', size_hint_y = None, height=157, width = 200, valign = 'bottom', background_normal='buttons/sitandreachlogo.png', text_size = (None, self.height*1.3))
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

class MainScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)
        self.classes = []

        #Creates the Example Class Used for Testing
        self.exampleclass = Class('exampleclass')
        self.student1 = Student('Mark Davis', 9, 'Male')
        self.student2 = Student('Olga Oglethrop', 8, 'Female')
        self.student3 = Student('Jose Cuervo', 9, 'Male')
        self.student4 = Student('The Dog', 24, 'Male')
        self.student5 = Student('Mark Davis', 9, 'Male')
        self.student6 = Student('Olga Oglethrop', 8, 'Female')
        self.student7 = Student('Jose Cuervo', 9, 'Male')
        self.student8 = Student('The Dog', 24, 'Male')
        self.exampleclass.add_student(self.student1)
        self.exampleclass.add_student(self.student2)
        self.exampleclass.add_student(self.student3)
        self.exampleclass.add_student(self.student4)
        self.exampleclass.add_student(self.student5)
        self.exampleclass.add_student(self.student6)
        self.exampleclass.add_student(self.student7)
        self.exampleclass.add_student(self.student8)
        self.classes.append(self.exampleclass)


        self.exampleclass2 = Class('example class 2')
        self.student17 = Student('Mark Davis', 9, 'Male')
        self.student18 = Student('Olga Oglethrop', 8, 'Female')
        self.student19 = Student('Jose Cuervo', 9, 'Male')
        self.student20 = Student('The Dog', 24, 'Male')
        self.exampleclass2.add_student(self.student17)
        self.exampleclass2.add_student(self.student18)
        self.exampleclass2.add_student(self.student19)
        self.exampleclass2.add_student(self.student20)
        self.classes.append(self.exampleclass2)
        ###############################################

        self.currentclass = None
        self.menu_width = Window.width/4.
        self.menu_height = Window.height/3.
        self.menu_x = (Window.width - self.menu_width)/2.
        self.menu_y = (Window.height - self.menu_height)/2.
        self.menu = BoxLayout(orientation= 'vertical',spacing = self.menu_height/15., size = (self.menu_width, self.menu_height), pos = (self.menu_x, self.menu_y))
        for each in self.classes:
            button = Button(text=each.get_name(), size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
            button.bind(on_press=self.callback)
            #This is the corresponding code to load a class see line #224
            self.menu.add_widget(button)
        self.addclassbutton = Button(text='Add Class', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.addclassbutton.bind(on_press=self.callback)
        self.menu.add_widget(self.addclassbutton)
        self.removeclassbutton = Button(text='Remove Class', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.removeclassbutton.bind(on_press=self.callback)
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
            pass
        if instance.text == 'Back':
            self.remove_widget(self.studentscreen)
            self.draw_report(self.currentclass)
            


    #Needs a callback for edit_student_button which brings up the fields for name, age, and gender, and then write sthem back
    #see create class in callback function for a similar problem
    def draw_studentscreen(self, studentname):
        self.redraw_canvas()
        self.remove_widget(self.menu)
        self.studentscreen = StudentScreen(studentname)
        self.menu = BoxLayout(orientation = 'horizontal', spacing = Window.width/15, size = (Window.width - Window.width/10, Window.height/10), pos = (Window.width/15, Window.height/30))
        self.edit_student_button = Button(text='Edit Information', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.back_button = Button(text='Back', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.menu.add_widget(self.edit_student_button)
        self.menu.add_widget(self.back_button)
        self.edit_student_button.bind(on_press=self.studentscreen_callback)
        self.back_button.bind(on_press=self.studentscreen_callback)
        self.add_widget(self.menu)
        self.add_widget(self.studentscreen)

    #Needs a callback for add_student_button and remove_student_button which brings up the fields for name, age, and gender, and then write sthem back
    #see create class and remove class (when this is fixed) in callback function for a similar problem
    def draw_report(self, classname):
        self.redraw_canvas()
        self.remove_widget(self.menu)
        self.report = ReportScreen(classname, parent = self)
        self.currentclass = classname
        self.menu = BoxLayout(orientation = 'horizontal', spacing = Window.width/15, size = (Window.width - Window.width/10, Window.height/10), pos = (Window.width/15, Window.height/30))
        self.add_student_button = Button(text='Add Student', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.remove_student_button = Button(text='Remove Student', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.back_button = Button(text='Back', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.menu.add_widget(self.add_student_button)
        self.menu.add_widget(self.remove_student_button)
        self.menu.add_widget(self.back_button)
        self.add_student_button.bind(on_press=self.report_callback)
        self.remove_student_button.bind(on_press=self.report_callback)
        self.back_button.bind(on_press=self.report_callback)
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
            pass

        if instance.text == 'Remove Student':
            pass

            

    def draw_logo(self):

        logo_width = Window.width/20
        logo_height = Window.height - Window.height/4

        with self.canvas:
            Color(1.,1.,1.,1.)
            Rectangle(source = 'schoollogo/schoollogo.png', size = (676, 126), pos = (logo_width, logo_height))
            Rectangle(size = (Window.width, Window.height/50), pos = (0,(Window.height - Window.height/3.45)))
            Color(0.964705882, 0.721568627, 0.27, mode='hsv')
            Rectangle(size = (Window.width, Window.height/80), pos = (0, (Window.height - Window.height/3.5)))


    def redraw_canvas(self):

        self.remove_widget(self.menu)

        with self.canvas:
            Color(0.623529412, 0.835294118, 0.245000908, mode='hsv')
            Rectangle(size = (Window.width, Window.height), pos = (0, 0))

        self.add_widget(self.menu)

    def redraw_logo(self):
        self.remove_widget(self.menu)

        with self.canvas:
            Color(1.,1.,1.,1.)
            Rectangle(source = 'schoollogo/schoollogo.png', size = (676, 126), pos = (logo_width, logo_height))
            Rectangle(size = (Window.width, Window.height/50), pos = (0,(Window.height - Window.height/3.45)))
            Color(0.964705882, 0.721568627, 0.27, mode='hsv')
            Rectangle(size = (Window.width, Window.height/80), pos = (0, (Window.height - Window.height/3.5)))

        self.add_widget(self.menu)
        
    #I will update popup graphics to fit the scheme of things
    def add_class(self):
        print 'pop up'
        popupmenu =  BoxLayout(orientation= 'vertical',spacing = self.menu_height/15., size = (self.menu_width, self.menu_height), pos = (self.menu_x, self.menu_y))
        
        popuplabel = Label(text='Name the class:')
        self.textinput = TextInput(focus = True, multiline = False)
        popupmenu.add_widget(popuplabel)
        popupmenu.add_widget(self.textinput)
        dismissbutton = Button(text='Create Class', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        popupmenu.add_widget(dismissbutton)
        dismissbutton.bind(on_press=self.callback)
        self.addclass_popup = Popup(title='Add Class', size_hint=(None,None), size=(self.menu_width, self.menu_height), content = popupmenu)
        self.addclass_popup.open()

    #should remove the class specified from the self.classes array, however I cannot figure out how to name the object correctly
    def removeclass_callback(self, instance):
        classname = instance.text
        for each in self.classes:
            internalclassname = each.get_name()
            if classname == internalclassname:
                self.classes.remove(each.get_self())
                self.reload_menu()

    #This function loads the list of classes in and then binds remove_callback 
    def remove_class(self):
        self.remove_widget(self.menu)
        self.menu = BoxLayout(orientation= 'vertical',spacing = self.menu_height/15., size = (self.menu_width, self.menu_height), pos = (self.menu_x, self.menu_y))
        for each in self.classes:
            classbutton = Button(text=each.get_name(), size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
            classbutton.bind(on_press=self.removeclass_callback)
            self.menu.add_widget(classbutton)
        self.add_widget(self.menu)


    def create_class(self, textinput):
        classname = Class(textinput)
        self.classes.append(classname)
        self.reload_menu()

    def reload_menu(self):
        self.remove_widget(self.menu)
        self.menu = BoxLayout(orientation= 'vertical',spacing = self.menu_height/15., size = (self.menu_width, self.menu_height), pos = (self.menu_x, self.menu_y))
        for each in self.classes:
            classbutton = Button(text=each.get_name(), size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
            classbutton.bind(on_press=self.callback)
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