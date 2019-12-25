from kivy.app import App
from kivy.lang import Builder
from DataModel.hero import Hero

h = Hero(100, 5)

h_kv_string = '''
BoxLayout:
    orientation: 'vertical'
    Label: 
        text: 'Nazwisko'
    BoxLayout:
        height: sp(100)
        orientation: 'horizontal'
        BoxLayout:
            orientation: 'vertical'
            Label: 
                text: 'siła: str'
            Label: 
                text: 'obrona: str'        
            Label: 
                text: 'percepcja: str'
            Label: 
                text: 'zwinnosc: str'        
        BoxLayout:
            orientation: 'vertical'
            Label: 
                text: 'moc: str'
            Label: 
                text: 'healing: srt'        
            Label: 
                text: 'voodoo: str'
            Label: 
                text: 'dekoncentracja: str'        
    Button: 
        text: 'train'
'''

kv = ''' 
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: sp(100)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: e1
                min: -360.
                max: 360.
            Label:
                text: 'angle_start = {}'.format(e1.value)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: e2
                min: -360.
                max: 360.
                value: 360
            Label:
                text: 'angle_end = {}'.format(e2.value)

    BoxLayout:
        size_hint_y: None
        height: sp(100)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: wm
                min: 0
                max: 2
                value: 1
            Label:
                text: 'Width mult. = {}'.format(wm.value)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: hm
                min: 0
                max: 2
                value: 1
            Label:
                text: 'Height mult. = {}'.format(hm.value)
        Button:
            text: 'Reset ratios'
            on_press: wm.value = 1; hm.value = 1

    FloatLayout:
        canvas:
            Color:
                rgb: 1, 250, 111
            Ellipse:
                pos: 100, 100
                size: 200 * wm.value, 201 * hm.value
                source: 'data/logo/kivy-icon-512.png'
                angle_start: e1.value
                angle_end: e2.value

'''


class CircleApp(App):
    def build(self):
        return Builder.load_string(h_kv_string)


CircleApp().run()