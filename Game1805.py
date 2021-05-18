import kivy
from kivy.core.window import Window
from kivy.config import Config
from kivy.app import App
	#layouts
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
	#widgets
from kivy.uix.button import Button
from kivy.uix.label import Label
	#check
from kivy.uix.image import Image 	# бббббббб   img = Image(source='/path/to/real_python.png',  FloatLayout
from kivy.properties import ObjectProperty

Config.set('graphics', 'resizable', 0);
Window.size = (450, 800)

bl = BoxLayout(orientation = 'vertical',padding=(5+5,5+5),spacing=0)
blb = BoxLayout(orientation = 'vertical',padding=(35,35),spacing=10,pos_hint={'bottom': 1})
fl = FloatLayout(size_hint=(1, .1))				#size_hint=(0.2, 0.075))
global page

class MainApp(App):
	def build(self):
		self.main_text = Label(text='Name Of Game',size_hint=(1, 0.33), pos_hint={'top': 1}) #maintext
		self.main_secret_text = Label(text == [text_language == ru_Ru] 'хуј' [/text_language],size_hint=(1, 0.33), pos_hint={ 'bottom': 1 , 'right': 1}) #chnm

		button = Button(text='Новая  игра', size_hint=(1, 0.075), pos_hint={'top': 1})  # maintext
		button0 = Button(text='Продолжить', size_hint=(1, 0.075), pos_hint={'top': 0})
		button1 = Button(text='Об авторе \n        и \n этой игре', size_hint=(1, 0.075), pos_hint={'top': 0})
		button2 = Button(text='Выход', size_hint=(1, 0.075), pos_hint={'top': 0})

		button3 = Button(text='', size_hint=(0.1, 0.57), pos_hint={'bottom': 1,'left' : 1},on_press=self.rnd_func)

		blb.add_widget(self.main_text);
		blb.add_widget(button)
		blb.add_widget(button0)
		blb.add_widget(button1)
		blb.add_widget(button2)

		bl.add_widget(blb)
		bl.add_widget(fl)
		fl.add_widget(button3)
		fl.add_widget(self.main_secret_text);
		return bl

	def __inti__(self):
		return

	def click(self, click):
		self.main_text.text='moloii'
		return

	def rnd_func(self, click):
		from random import randint
		a = open('secret_text.txt')
		for i in a:
			tmp = a.readlines()
		txt = []
		# txt.split(tmp)
		i = 0
		i = randint(0, 10)
		print( tmp[i])
		self.main_secret_text.text = '?txt?                   ' + str(tmp[i])
		 #Rint [text_language: ru_Ru][ / text_language]
		#SRT_TXT = open("secret_text.txt") #open in var

		#RND_NUM = randint(0, 100)
		#i = SRT_TXT.readline(RND_NUM) #in var rline


		#self.main_secret_text.text = '?txt?' + str(RND_NUM) + '    '  + i
		#SRT_TXT.close()

	def on_press_button(self):
		self.main_text.text='moloii'

if __name__ == '__main__':
	MainApp().run()


