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
from random import randint
Config.set('graphics', 'resizable', 0);
Window.size = (450, 800)
Window.clearcolor = (3/255,4/255,3/255,1)
Window.title = "Hello"

bl = BoxLayout(orientation = 'vertical',padding=(5+5,5+5),spacing=0)
blb = BoxLayout(orientation = 'vertical',padding=(35,35),spacing=10,pos_hint={'bottom': 1})
fl = FloatLayout(size_hint=(1, .1))				#size_hint=(0.2, 0.075))
global page

class MainApp(App):
	def build(self):
		self.main_text = Label(text='Name Of Game',size_hint=(1, 0.33), pos_hint={'top': 1}) #maintext
		self.main_secret_text = Label(text = '[text_language == ru_Ru]hello[/text_language]',size_hint=(1, 0.33), pos_hint={ 'bottom': 1 , 'right': 1}) #chnm

		button = Button(text='Новая  игра', size_hint=(1, 0.075), pos_hint={'top': 1})  # maintext
		button0 = Button(text='Продолжить', size_hint=(1, 0.075), pos_hint={'top': 0})
		button1 = Button(text='Об авторе \n        и \n этой игре', size_hint=(1, 0.075), pos_hint={'top': 0})
		button2 = Button(text='Выход', size_hint=(1, 0.075), pos_hint={'top': 0})

		button3 = Button(text='', size_hint=(0.1, 0.57), pos_hint={'bottom': 1,'left' : 1},on_press=self.secret)

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
		super().__init__()

		return

	def click(self, click):
		self.main_text.text='moloii'
		return

	# button n3
	def secret(self, click, *args):
		RND_NUM = randint(0, 100)
		RND_NUM_CLR = randint(0, 255)
		SRT_TXT = open('secret_text.txt','r', encoding='utf-8')
		SKP_TXT = open('skip_text.txt', 'r', encoding='utf-8')
		self.main_secret_text.color = (RND_NUM_CLR, RND_NUM_CLR, RND_NUM_CLR, 1)
		for i in SRT_TXT and SKP_TXT:
			list_sct_txt = SRT_TXT.readlines()
			list_skp_txt = SKP_TXT.readlines()

		if RND_NUM >= 80:
			self.main_secret_text.text = '?txt?  some simbols in asci mb     ' + list_sct_txt[RND_NUM]; 	SRT_TXT.close()

		else:
			self.main_secret_text.text = '                   ' + list_skp_txt[RND_NUM]; 	SKP_TXT.close()
			self.main_secret_text.color = (randint(0, 255), randint(0, 255), randint(0, 255), 1)
			#button n1
	def on_press_button(self):
		self.main_text.text='moloii'

if __name__ == '__main__':
	MainApp().run()


