from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window

Window.maximize() 

user_name = ''

d_userdt={'Suresh01':['S00resh','Suresh K','1234567890','AB+'], 
          'Sr1ya':['Sriya@101','Sriya Raj','4352617899','O+']}

d_vac={'Suresh01':['MMR'], 
       'Sr1ya':['Polio']}

d_alg={'Suresh01':['Psoriasis'], 
       'Sr1ya':['Dermatitis']} 

d_hins={'Suresh01':[12345], 
       'Sr1ya':[65846]} 

class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)

class LoginPage(Screen):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)
        self.clear_widgets()
        self.add_widget(Label(text='LOGIN',
                              font_size=30,
                              bold=True,
                              pos_hint={'center_x': .5,
                                        'center_y': .8}))

        self.add_widget(Label(text='User Name :',
                              font_size=20,
                              pos_hint={'center_x': .405,
                                        'center_y': .66}))

        self.username = TextInput(multiline=False,
                                  size_hint=(.2, .055),
                                  font_size=20,
                                  pos_hint={'center_x': .55,
                                            'center_y': .66})
        self.add_widget(self.username)

        self.promt_username = Label(text='',
                                    color=[1, 0, 0, 1],
                                    font_size=12,
                                    pos_hint={'center_x': .73,
                                              'center_y': .66})
        self.add_widget(self.promt_username)

        self.add_widget(Label(text=' Password :',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .60}))

        self.ID = TextInput(multiline=False,
                            size_hint=(.2, .055),
                            font_size=20,
                            pos_hint={'center_x': .55,
                                      'center_y': .60})
        self.add_widget(self.ID)

        self.promt_ID = Label(text='',
                              color=[1, 0, 0, 1],
                              font_size=12,
                              pos_hint={'center_x': .73,
                                        'center_y': .60})
        self.add_widget(self.promt_ID) 

        self.add_widget(Label(text="Don't have an Account?",
                              font_size=10,
                              pos_hint={'center_x': .4,
                                        'center_y': .4}))

        self.Create_Acc = Button(text='Create Account', size_hint=(.17, .05),
                                 font_size=15,
                                 pos_hint={'center_x': .4,
                                           'center_y': .35},
                                 on_press=self.Create)
        self.add_widget(self.Create_Acc)

        self.add_widget(Label(text="Don't remember your password?",
                              font_size=10,
                              pos_hint={'center_x': .6,
                                        'center_y': .4}))

        self.Forgot_Password = Button(text='Forgot Password', size_hint=(.17, .05),
                                      font_size=15,
                                      pos_hint={'center_x': .6,
                                                'center_y': .35},
                                      on_press=self.Forgot)
        self.add_widget(self.Forgot_Password) 

        self.add_widget(Button(text='ENTER',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .5,
                                         'center_y': .25},
                               on_press=self.Enter))

        lab1 = Label(text='Contact Information',
                     bold=True,
                     size_hint=(None, None),
                     pos_hint={'center_x': .5,
                               'center_y': .1})
        self.add_widget(lab1)

        lab2 = Label(text='Phone: +91 XXX XXX XXXX',
                     size_hint=(None, None),
                     pos_hint={'center_x': .5,
                               'center_y': .065})
        self.add_widget(lab2)

        lab3 = Label(text='Email: magnumopus@gmail.com',
                     size_hint=(None, None),
                     pos_hint={'center_x': .5,
                               'center_y': .032})
        self.add_widget(lab3) 
        
        self.Logout = Button(text='EXIT',
                           size_hint=(.1, .05),
                           pos_hint={'x': .87, 'y': .9},
                           on_press=self.Exit)
        
        self.add_widget(self.Logout) 
        
        global user_name
        user_name = self.username.text
    
    def Enter(self, *args):
        if self.username.text == '' or self.ID.text == '':
            layout = FloatLayout()  # Pop-Up Part
            yesButton = Button(text="CLOSE",
                               size_hint=(.15, .12),
                               pos_hint={'center_x': .5,
                                         'center_y': .6},
                               font_size=15)
            popupLabel = Label(text="Username & Password Cannot Be Empty",
                               font_size=20,
                               pos_hint={'center_x': .5,
                                         'center_y': .4})
            layout.add_widget(popupLabel)
            layout.add_widget(yesButton)
            popup = Popup(title='ERROR',  # Instantiate the popup and display
                          content=layout,
                          size_hint=(.4, .4))
            popup.open()
            # Attach close button press with popup.dismiss action
            yesButton.bind(on_press=popup.dismiss) 
        else:
            self.manager.current = 'Details'
    
    def Forgot(self, *args):
        self.manager.current = 'Forgot'

    def Create(self, *args):
        self.manager.current = 'Create'

    def Exit(self, *args):
        layout = FloatLayout()  # Pop-Up Part
        noButton = Button(text="CANCEL",
                          size_hint=(.15, .12),
                          pos_hint={'center_x': .63,
                                    'center_y': .6},
                          font_size=15)
        yesButton = Button(text="YES",
                           size_hint=(.15, .12),
                           pos_hint={'center_x': .35,
                                     'center_y': .6},
                           font_size=15)
        popupLabel = Label(text="Are you sure you want to exit?",
                           font_size=20,
                           pos_hint={'center_x': .5,
                                     'center_y': .4})
        layout.add_widget(popupLabel)
        layout.add_widget(noButton)
        layout.add_widget(yesButton)
        popup = Popup(title='EXIT',  # Instantiate the popup and display
                      content=layout,
                      size_hint=(.4, .4))
        popup.open()
        # Attach close button press with popup.dismiss action
        noButton.bind(on_press=popup.dismiss)
        yesButton.bind(on_press=self.Closing)
        yesButton.bind(on_press=popup.dismiss)
    
    def Closing(self, *args):
        App.get_running_app().stop()
        Window.close()
        
class CreatePage(Screen):
    def __init__(self, **kwargs):
        super(CreatePage, self).__init__(**kwargs)
        self.clear_widgets()
        
        self.add_widget(Button(text='BACK',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .9,
                                         'center_y': .9},
                               on_press=self.Back))
        
        self.add_widget(Label(text='Enter Username :',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .7}))
        self.uname = TextInput(multiline=False,
                                  size_hint=(.2, .055),
                                  font_size=20,
                                  pos_hint={'center_x': .6,
                                            'center_y': .7})
        self.add_widget(self.uname) 
        
        self.add_widget(Label(text='Enter Password :',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .6}))
        self.pasw = TextInput(multiline=False,
                                  size_hint=(.2, .055),
                                  font_size=20,
                                  pos_hint={'center_x': .6,
                                            'center_y': .6})
        self.add_widget(self.pasw)
        
        self.add_widget(Label(text='Enter Patient Name :',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .5}))
        self.pname = TextInput(multiline=False,
                                  size_hint=(.2, .055),
                                  font_size=20,
                                  pos_hint={'center_x': .6,
                                            'center_y': .5})
        self.add_widget(self.pname)
        
        self.add_widget(Label(text='Enter Aadhar Number :',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .4}))
        self.aadhar = TextInput(multiline=False,
                                  size_hint=(.2, .055),
                                  font_size=20,
                                  pos_hint={'center_x': .6,
                                            'center_y': .4})
        self.add_widget(self.aadhar)
        
        self.add_widget(Label(text='Enter Blood Group :',
                              font_size=20,
                              pos_hint={'center_x': .4,
                                        'center_y': .3}))
        self.bg = TextInput(multiline=False,
                                  size_hint=(.2, .055),
                                  font_size=20,
                                  pos_hint={'center_x': .6,
                                            'center_y': .3})
        self.add_widget(self.bg)
        
        self.add_widget(Button(text='ENTER',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .5,
                                         'center_y': .195},
                               on_press=self.Enter)) 
        
    def Enter(self, *args):
        l=[] # value
        u = self.uname.text #key
        l.append(self.pasw.text)
        l.append(self.pname.text)
        l.append(self.aadhar.text)
        l.append(self.bg.text) 
        global d_userdt
        d_userdt[u]=l
        layout = FloatLayout()  # Pop-Up Part
        yesButton = Button(text="CLOSE",
                           size_hint=(.15, .12),
                           pos_hint={'center_x': .5,
                                     'center_y': .6},
                           font_size=15)
        popupLabel = Label(text="Account Successfuly Created",
                           font_size=20,
                           pos_hint={'center_x': .5,
                                     'center_y': .4})
        layout.add_widget(popupLabel)
        layout.add_widget(yesButton)
        popup = Popup(title='POPUP',  # Instantiate the popup and display
                      content=layout,
                      size_hint=(.4, .4))
        popup.open()
        # Attach close button press with popup.dismiss action
        yesButton.bind(on_press=popup.dismiss) 
        self.manager.current = 'Login'
        
    def Back(self, *args):
        self.manager.current='Login'
        

class ForgotPage(Screen):
    def __init__(self, **kwargs):
        super(ForgotPage, self).__init__(**kwargs)
        self.clear_widgets()
        
        self.add_widget(Button(text='BACK',
                               size_hint=(.1, .05),
                               font_size=15,
                               pos_hint={'center_x': .9,
                                         'center_y': .9},
                               on_press=self.Back))
    def Back(self, *args):
        self.manager.current='Login'

class DetailsPage(Screen):
    def __init__(self, **kwargs):
        super(DetailsPage, self).__init__(**kwargs)
        self.clear_widgets()

        global d_userdt    
        global user_name
        un = user_name
        
        i = d_userdt.keys() 
        for j in i:
            if j == un:
                global d_vac
                vacc = d_vac.values()
                for k in vacc:
                    k1 = str(k)
                    self.add_widget(Label(text=k1,
                                          font_size=20,
                                          pos_hint={'center_x': .4,
                                                    'center_y': .7}))
                global d_alg
                alerg = d_alg.values()
                for l in alerg:
                    l1=str(l)
                    self.add_widget(Label(text=l1,
                                          font_size=20,
                                          pos_hint={'center_x': .4,
                                                    'center_y': .5}))
                global d_hins
                insure=d_hins.values()
                for m in insure:
                    m1=str(m)
                    self.add_widget(Label(text=m1,
                                          font_size=20,
                                          pos_hint={'center_x': .4,
                                                    'center_y': .3})) 
                    
        self.Logout = Button(text='LOGOUT',
                           size_hint=(.1, .05),
                           pos_hint={'x': .87, 'y': .9},
                           on_press=self.Exit)
        
        self.add_widget(self.Logout)
        
    def Exit(self, *args):
        self.manager.current = 'Login'
        

class Application(App):
    def build(self):
        sm = ScreenManagement(transition=SlideTransition())
        sm.add_widget(LoginPage(name='Login')) 
        sm.add_widget(CreatePage(name='Create')) 
        sm.add_widget(ForgotPage(name='Forgot')) 
        sm.add_widget(DetailsPage(name='Details'))
        return sm

if __name__ == "__main__":
    Application().run() 