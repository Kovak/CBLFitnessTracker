import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, ObjectProperty, StringProperty

Builder.load_file('numpad.kv')

class numpad(Widget):
    #uncomment these if you need them, right now the only thing we're using is the current_value property
    #button_0=ObjectProperty(None)
    #button_1=ObjectProperty(None)
    #button_2=ObjectProperty(None)
    #button_3=ObjectProperty(None)
    #button_4=ObjectProperty(None)
    #button_5=ObjectProperty(None)
    #button_6=ObjectProperty(None)
    #button_7=ObjectProperty(None)
    #button_8=ObjectProperty(None)
    #button_9=ObjectProperty(None)
    #button_ok=ObjectProperty(None)
    
    current_value=NumericProperty(0)
    
    def button_1_press(self):
        self.current_value = 10*self.current_value + 1
    def button_2_press(self):
        self.current_value = 10*self.current_value + 2
    def button_3_press(self):
        self.current_value = 10*self.current_value + 3
    def button_4_press(self):
        self.current_value = 10*self.current_value + 4
    def button_5_press(self):
        self.current_value = 10*self.current_value + 5
    def button_6_press(self):
        self.current_value = 10*self.current_value + 6
    def button_7_press(self):
        self.current_value = 10*self.current_value + 7
    def button_8_press(self):
        self.current_value = 10*self.current_value + 8
    def button_9_press(self):
        self.current_value = 10*self.current_value + 9
    def button_0_press(self):
        self.current_value = 10*self.current_value
        
    
class Controller(FloatLayout):
    '''Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    '''
    label_wid = ObjectProperty(None)
    info = StringProperty('')

    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.info = 'New info text'
    
class MainScreen(Widget):
   
    def on_touch_down(self, touch):
        pad=Controller(info='Test info')
        pad.size=(500,500)
        pad.pos=(800,800)
        self.add_widget(pad)
            
  
            
    

class NumPadApp(App):
    def build(self):
        return numpad()

if __name__ in ('__android__', '__main__'):
    NumPadApp().run()