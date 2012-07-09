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
        self.students = classname.students
        self.parent = parent
        self.studentlayout = BoxLayout(orientation='vertical', spacing = 10, size_hint_x = 2)
        self.overalllayout = BoxLayout(orientation='horizontal', pos=(Window.width/10,Window.height/5), size=(Window.width - Window.width/5, Window.height - Window.height/5))
        self.studentgenderlayout = BoxLayout(orientation='vertical')
        self.studentagelayout = BoxLayout(orientation='vertical')
        self.miletimelayout = BoxLayout(orientation = 'vertical')
        self.pushupslayout = BoxLayout(orientation = 'vertical')
        self.curlupslayout = BoxLayout(orientation = 'vertical')
        self.stretchlayout = BoxLayout(orientation = 'vertical')
        self.numstudents = 0
        genderlabel = Label(text = 'Gender')
        studentnamelabel = Label(text = '')
        agelabel = Label(text = 'Age')
        miletimelabel = Label(text = 'Mile Time')
        pushupslabel = Label(text = 'Push Ups')
        curlupslabel = Label(text = 'Curl Ups')
        stretchlabel = Label(text = 'Stretch L/R')
        self.studentlayout.add_widget(studentnamelabel)
        self.studentgenderlayout.add_widget(genderlabel)
        self.studentagelayout.add_widget(agelabel)
        self.miletimelayout.add_widget(miletimelabel)
        self.pushupslayout.add_widget(pushupslabel)
        self.curlupslayout.add_widget(curlupslabel)
        self.stretchlayout.add_widget(stretchlabel)

        #This loop adds in the scores for each student
        for x in self.students:
            labelname1 = 'studentlabel' + str(self.numstudents)
            labelname2 = 'genderlabel' + str(self.numstudents)
            labelname3 = 'agelabel' + str(self.numstudents)
            labelname4 = 'miletimelabel' + str(self.numstudents)
            labelname5 = 'pushupslabel' + str(self.numstudents)
            labelname6 = 'curlupslabel' + str(self.numstudents)
            labelname7 = 'stretchlabel' + str(self.numstudents)
            vars()[labelname1] = Button(text = x.get_name(), background_normal='buttons/button_normal.png', background_down='buttons/button_down.png') 
            vars()[labelname1].bind(on_press=self.parent.student_callback)
            vars()[labelname2] = Label(text = x.get_gender()) 
            vars()[labelname3] = Label(text = str(x.get_age()))
            vars()[labelname4] = Label(text = str(x.get_miletime()))
            vars()[labelname5] = Label(text = str(x.get_pushups()))  
            vars()[labelname6] = Label(text = str(x.get_curlups()))
            vars()[labelname7] = Label(text = str(x.get_stretchl()) + '/' + str(x.get_stretchr())) 

            #Color Text Based on Scores, this is just sample code. We need to expand this based on the standards and age
            #Pass
            if x.get_pushups() >= 0:
                vars()[labelname5].color = (0.031372549, 0.768627451, 0.109803922, 1)
            #Fail
            if x.get_curlups() <= 10:
                vars()[labelname6].color = (0.82745098, 0.003921569, 0.02745098, 1)

            #Super Saiyan
            if x.get_miletime() >= 0:
                vars()[labelname4].color = (1, 0.847058824, 0.109803922, 1)



            self.numstudents += 1
            self.studentlayout.add_widget(vars()[labelname1])
            self.studentgenderlayout.add_widget(vars()[labelname2])
            self.studentagelayout.add_widget(vars()[labelname3])
            self.miletimelayout.add_widget(vars()[labelname4])
            self.pushupslayout.add_widget(vars()[labelname5])
            self.curlupslayout.add_widget(vars()[labelname6])
            self.stretchlayout.add_widget(vars()[labelname7])



        self.overalllayout.add_widget(self.studentlayout)
        self.overalllayout.add_widget(self.studentgenderlayout)
        self.overalllayout.add_widget(self.studentagelayout)
        self.overalllayout.add_widget(self.miletimelayout)
        self.overalllayout.add_widget(self.pushupslayout)
        self.overalllayout.add_widget(self.curlupslayout)
        self.overalllayout.add_widget(self.stretchlayout)
        self.add_widget(self.overalllayout)


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
        self.gender = self.student.get_gender()
        self.age = self.student.get_age()
        self.mile_time = self.student.get_miletime()
        self.pushups = self.student.get_pushups()
        self.top_boxlayout = BoxLayout(orientation = 'horizontal', spacing = Window.width/15, size = (Window.width - Window.width/5., Window.height/10.), pos = (Window.width/10, Window.height - Window.height/10))
        genderlabel = Label(text = self.student.get_gender())
        studentnamelabel = Label(text = self.student.get_name())
        agelabel = Label(text = 'Age: ' + str(self.student.get_age()))
        self.top_boxlayout.add_widget(studentnamelabel)
        self.top_boxlayout.add_widget(agelabel)
        self.top_boxlayout.add_widget(genderlabel)
        self.main_boxlayout = BoxLayout(orientation = 'horizontal', spacing = (Window.width - Window.width/3.5 - 400.), size =(Window.width - Window.width/3.5, Window.height - Window.height/3.33), pos = (Window.width/7., Window.height/6.66))
        self.column1 = BoxLayout(orientation = 'vertical')
        self.column2 = BoxLayout(orientation = 'vertical')
        self.milelabel = Label(text = 'Mile Time: ' +str(self.student.get_miletime()))
        self.pushupslabel = Label(text = 'Push-ups: ' +str(self.student.get_pushups()))
        self.curlupslabel = Label(text = 'Curl-ups: ' +str(self.student.get_curlups()))
        self.stretchlabel = Label(text = 'Stretch L/R: ' +str(self.student.get_stretchl()) + '/' + str(self.student.get_stretchr()))
        self.milebutton = Button(text = 'Mile Run', size_hint_y = None, height=157, width = 200 , valign = 'bottom', background_normal='buttons/runninglogo.png', text_size = (None, self.height*1.3))
        self.pushupsbutton = Button(text ='Push-Ups', size_hint_y = None, height=157, width = 200, valign = 'bottom', background_normal='buttons/pushuplogo.png', text_size = (None, self.height*1.3))
        self.curlupsbutton = Button(text = 'Curl-Ups', size_hint_y = None, height=157, width = 200 , valign = 'bottom', background_normal='buttons/curlupslogo.png', text_size = (None, self.height*1.3))
        self.stretchbutton = Button(text = 'Sit-and-Reach', size_hint_y = None, height=157, width = 200, valign = 'bottom', background_normal='buttons/sitandreachlogo.png', text_size = (None, self.height*1.3))
        self.column1.add_widget(self.milebutton)
        self.column1.add_widget(self.milelabel)
        self.column1.add_widget(self.pushupsbutton)
        self.column1.add_widget(self.pushupslabel)
        self.column2.add_widget(self.curlupsbutton)
        self.column2.add_widget(self.curlupslabel)
        self.column2.add_widget(self.stretchbutton)
        self.column2.add_widget(self.stretchlabel)
        self.main_boxlayout.add_widget(self.column1)
        self.main_boxlayout.add_widget(self.column2)
        self.add_widget(self.top_boxlayout)
        self.add_widget(self.main_boxlayout)
        
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
        self.student9 = Student('Mark Davis', 9, 'Male')
        self.student10 = Student('Olga Oglethrop', 8, 'Female')
        self.student11 = Student('Jose Cuervo', 9, 'Male')
        self.student12 = Student('The Dog', 24, 'Male')
        self.student13 = Student('Mark Davis', 9, 'Male')
        self.student14 = Student('Olga Oglethrop', 8, 'Female')
        self.student15 = Student('Jose Cuervo', 9, 'Male')
        self.student16 = Student('The Dog', 24, 'Male')
        self.exampleclass.add_student(self.student9)
        self.exampleclass.add_student(self.student10)
        self.exampleclass.add_student(self.student11)
        self.exampleclass.add_student(self.student12)
        self.exampleclass.add_student(self.student13)
        self.exampleclass.add_student(self.student14)
        self.exampleclass.add_student(self.student15)
        self.exampleclass.add_student(self.student16) 
        self.classcount = 1
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
        self.classcount = 2
        ###############################################
        self.currentclass = None
        self.menu_width = Window.width/4.
        self.menu_height = Window.height/3.
        self.menu_x = (Window.width - self.menu_width)/2.
        self.menu_y = (Window.height - self.menu_height)/2.
        self.menu = BoxLayout(orientation= 'vertical',spacing = self.menu_height/15., size = (self.menu_width, self.menu_height), pos = (self.menu_x, self.menu_y))
        for each in self.classes:
            classname = 'self.' + each.get_name()
            vars()[classname] = Button(text=each.get_name(), size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
            vars()[classname].bind(on_press=self.callback)
            #This is the corresponding code to load a class see line #224
            self.menu.add_widget(vars()[classname])
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
        self.popupmenu =  BoxLayout(orientation= 'vertical',spacing = self.menu_height/15., size = (self.menu_width, self.menu_height), pos = (self.menu_x, self.menu_y))
        
        self.popuplabel = Label(text='Name the class:')
        self.textinput = TextInput(focus = True, multiline = False)
        self.popupmenu.add_widget(self.popuplabel)
        self.popupmenu.add_widget(self.textinput)
        self.dismissbutton = Button(text='Create Class', size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
        self.popupmenu.add_widget(self.dismissbutton)
        self.dismissbutton.bind(on_press=self.callback)
        self.addclass_popup = Popup(title='Add Class', size_hint=(None,None), size=(self.menu_width, self.menu_height), content = self.popupmenu)
        self.addclass_popup.open()

    #should remove the class specified from the self.classes array, however I cannot figure out how to name the object correctly
    def removeclass_callback(self, instance):
        classname = 'self.' + instance.text
        for each in self.classes:
            internalclassname = 'self.' + each.get_name()
            if classname == internalclassname:
                self.classes.remove(each.get_self())
                self.classcount -= 1
                self.reload_menu()

    #This function loads the list of classes in and then binds remove_callback 
    def remove_class(self):
        self.remove_widget(self.menu)
        self.menu = BoxLayout(orientation= 'vertical',spacing = self.menu_height/15., size = (self.menu_width, self.menu_height), pos = (self.menu_x, self.menu_y))
        for each in self.classes:
            classname = 'self.' + each.get_name()
            vars()[classname] = Button(text=each.get_name(), size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
            vars()[classname].bind(on_press=self.removeclass_callback)
            self.menu.add_widget(vars()[classname])
        self.add_widget(self.menu)


    def create_class(self, textinput):
        classnamestr = 'self.' + textinput
        print classnamestr
        vars()[classnamestr] = Class(textinput)
        self.classes.append(vars()[classnamestr])
        self.classcount += 1
        self.reload_menu()

    def reload_menu(self):
        self.remove_widget(self.menu)
        self.menu = BoxLayout(orientation= 'vertical',spacing = self.menu_height/15., size = (self.menu_width, self.menu_height), pos = (self.menu_x, self.menu_y))
        for each in self.classes:
            classname = 'self.' + each.get_name()
            vars()[classname] = Button(text=each.get_name(), size_hint_y=None, height=40, background_normal='buttons/button_normal.png', background_down='buttons/button_down.png')
            vars()[classname].bind(on_press=self.callback)
            self.menu.add_widget(vars()[classname])
        self.menu.add_widget(self.addclassbutton)
        self.menu.add_widget(self.removeclassbutton)
        self.add_widget(self.menu)






class MenuTestApp(App):
    def build(self):
        mainscreen = MainScreen(pos=(0,0),size=Window.size)
        return mainscreen
        

if __name__ in ('__android__', '__main__'):
    MenuTestApp().run()