# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.popup import Popup
import webbrowser
from bands import bands

class Myapp(App):
    def build(self):
        #中文顯示
        #resource_add_path('./wt011.ttf') #引入字體檔案
        #LabelBase.register('Roboto', 'wt011.ttf') #將kivy默認的字體替換成自己下載的字體
        self.letter = ''
        self.number = []
        self.color = []

        self.colors = {'Red': 'R', 'Green': 'G', 'Blue': 'B', 'White': 'W', 'Yellow': 'Y', 'Orange': 'O', 'Sky Blue': 'S', 'Light Green': 'H', 'Brown': 'C'}

        main_layout = BoxLayout(orientation="vertical")

        self.target = ''
        self.bandedbfs = Button(text ="", size_hint=(1, None), size=(Window.width*0.85, Window.width*0.85))
        self.bandedbfs.bind(on_press=self.linkto)
        self.popupimg = Popup(title='', content=self.bandedbfs, size_hint=(0.9, None), size=(Window.width*0.9, Window.width))

        # Header
        header = BoxLayout(size_hint=(1, .5))
        header.add_widget(Image(source='images/bfsa_log.png', size_hint=(.2, 1)))
        header.add_widget(Label(text='BFSA', size_hint=(.2, 1)))
        self.query = TextInput(multiline=False, readonly=True, font_size=header.height/3, halign="right", size_hint=(.6, 1))
        header.add_widget(self.query)
        main_layout.add_widget(header)

        # Body
        self.body = ScrollView(size_hint=(1, None), size=(Window.width*0.9, Window.height*0.8), scroll_wheel_distance=100)
        self.calculator = BoxLayout(orientation="vertical", size_hint=(1, 1))
        h_layout = BoxLayout(size_hint=(1, .25))
        for label in ['K', 'S', 'E']:
            button = Button(
                text=label,
            background_normal='images/red.png',
            background_down='images/grey.png',
            )
            button.bind(on_press=self.on_button_press_letter)
            h_layout.add_widget(button)
        self.calculator.add_widget(h_layout)
        
        h_layout = BoxLayout(size_hint=(1, .25))
        for label in ['H', 'V', 'Y']:
            button = Button(
                text=label,
            background_normal='images/red.png',
            background_down='images/grey.png',
            )
            button.bind(on_press=self.on_button_press_letter)
            h_layout.add_widget(button)
        self.calculator.add_widget(h_layout)
        
        h_layout = BoxLayout(size_hint=(1, .25))
        for label in ['T', 'N']:
            button = Button(
                text=label,
            background_normal='images/blue.png',
            background_down='images/grey.png',
            )
            button.bind(on_press=self.on_button_press_letter)
            h_layout.add_widget(button)
        button = Button(
            text='J',
            color=[0,0,0,1],
            background_normal='images/yellow.png',
            background_down='images/grey.png',
        )
        button.bind(on_press=self.on_button_press_letter)
        h_layout.add_widget(button)
        self.calculator.add_widget(h_layout)

        h_layout = BoxLayout(size_hint=(1, .25))
        button = Button(
            text='A',
            background_normal='images/green.png',
            background_down='images/grey.png',
        )
        button.bind(on_press=self.on_button_press_letter)
        h_layout.add_widget(button)
        for label in ['RU', 'R']:
            button = Button(
                text=label,
                color=[0,0,0,1],
            background_normal='images/white.png',
            background_down='images/grey.png',
            )
            button.bind(on_press=self.on_button_press_letter)
            h_layout.add_widget(button)
        self.calculator.add_widget(h_layout)

        buttons = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["0", "X"],
        ]
        for row in buttons:
            h_layout = BoxLayout(size_hint=(1, .25))
            for label in row:
                button = Button(
                    text=label,
                )
                button.bind(on_press=self.on_button_press_number)
                h_layout.add_widget(button)
            self.calculator.add_widget(h_layout)

        h_layout = BoxLayout(size_hint=(1, .25))
        button = Button(
            text='Red',
            background_normal='images/red.png',
            background_down='images/grey.png',
        )
        button.bind(on_press=self.on_button_press_color)
        h_layout.add_widget(button)
        button = Button(
            text='Green',
            background_normal='images/green.png',
            background_down='images/grey.png',
        )
        button.bind(on_press=self.on_button_press_color)
        h_layout.add_widget(button)
        button = Button(
            text='Blue',
            background_normal='images/blue.png',
            background_down='images/grey.png',
        )
        button.bind(on_press=self.on_button_press_color)
        h_layout.add_widget(button)
        self.calculator.add_widget(h_layout)

        h_layout = BoxLayout(size_hint=(1, .25))
        button = Button(
            text='White',
            color=[0,0,0,1],
            background_normal='images/white.png',
            background_down='images/grey.png',
        )
        button.bind(on_press=self.on_button_press_color)
        h_layout.add_widget(button)
        button = Button(
            text='Yellow',
            color=[0,0,0,1],
            background_normal='images/yellow.png',
            background_down='images/grey.png',
        )
        button.bind(on_press=self.on_button_press_color)
        h_layout.add_widget(button)
        button = Button(
            text='Orange',
            color=[0,0,0,1],
            background_normal='images/orange.png',
            background_down='images/grey.png',
        )
        button.bind(on_press=self.on_button_press_color)
        h_layout.add_widget(button)
        self.calculator.add_widget(h_layout)

        h_layout = BoxLayout(size_hint=(1, .25))
        button = Button(
            text='Sky Blue',
            color=[0,0,0,1],
            background_normal='images/skyblue.png',
            background_down='images/grey.png',
        )
        button.bind(on_press=self.on_button_press_color)
        h_layout.add_widget(button)
        button = Button(
            text='Light Green',
            color=[0,0,0,1],
            background_normal='images/lightgreen.png',
            background_down='images/grey.png',
        )
        button.bind(on_press=self.on_button_press_color)
        h_layout.add_widget(button)
        button = Button(
            text='Brown',
            background_normal='images/brown.png',
            background_down='images/grey.png',
        )
        button.bind(on_press=self.on_button_press_color)
        h_layout.add_widget(button)
        self.calculator.add_widget(h_layout)

        self.body.add_widget(self.calculator)
        main_layout.add_widget(self.body)

        # footer
        footer = BoxLayout(size_hint=(1, .5))
        clear_button = Button(
            text="Clear", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        clear_button.bind(on_press=self.clear_query)
        footer.add_widget(clear_button)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        footer.add_widget(equals_button)
        main_layout.add_widget(footer)

        return main_layout

    def query_code(self):
        if len(self.number) > 3:
            self.number = self.number[-3:]
        if len(self.color) > 3:
            self.color = self.color[-3:]
        self.query.text = "[%s] + [%s] + [%s]" %(self.letter, ''.join(self.number), '-'.join(self.color))

    def clear_query(self, instance):
        self.letter = ''
        self.number = []
        self.color = []
        self.query_code()
        #self.body.size_hint=(1, 1)
        self.body.clear_widgets()
        self.body.add_widget(self.calculator)

    def on_button_press_letter(self, instance):
        self.letter = instance.text
        self.query_code()

    def on_button_press_number(self, instance):
        self.number.append(instance.text)
        self.query_code()

    def on_button_press_color(self, instance):
        self.color.append(self.colors[instance.text])
        self.query_code()

    def on_solution(self, instance):
        code = self.letter
        if self.number:
            code += ''.join(self.number)
        if self.color:
            color = ''.join(self.color)
        else:
            color = ''
        results = []
        for k, v in bands.items():
            if code:
                if k.find(code) > -1 and (not color or bands[k][0].find(color) > -1):
                    results.append(k)
            else:
                if not color or bands[k][0].find(color) > -1:
                    results.append(k)
        if results:
            self.bfs(results)
        else:
            self.body.clear_widgets()
            self.body.add_widget(Button(text='Nothing!'))
        
    def bfs(self, bandno):
        self.body.clear_widgets()
        #self.body.size_hint=(1, len(bandno)/6)
        images = GridLayout(cols=2, row_default_height=Window.width/2, size_hint=(1, None), size=(Window.width, Window.width/2*len(bandno)/2))
        for i in range(len(bandno)):
            band = bandno[i]
            #img =  Image(source='images/%s.png' %band)
            img = Button(text ="",
                     background_normal = 'images/%s.png' %band,
                     background_down ='images/%s.png' %band,
                     size=(Window.width/2, Window.width/2),
                     size_hint=(None, None)
                   )
            img.bind(on_press=self.popup)
            images.add_widget(img)
        self.body.add_widget(images)

    def popup(self, instance):
        self.target = instance.background_normal.replace('images/', '').replace('.png', '')
        self.bandedbfs.background_normal = instance.background_normal
        self.bandedbfs.background_down = instance.background_down
        #self.popupimg.content = Image(source= instance.background_normal)
        self.popupimg.title = self.target + ': ' + bands[self.target][1] + '@' + bands[self.target][2]
        self.popupimg.open()

    def linkto(self, instance):
        webbrowser.open('https://bfsn.bfsa.org.tw/bandbfs.php?markedbfs=%s'%self.target)

if __name__ == '__main__':
    Myapp().run()