from kivy.app import App
from kivy.lang import Builder
from DataModel.hero import Hero
from kivy.uix.boxlayout import BoxLayout


class RootWidget(BoxLayout):
    h = Hero()

    def setHero(self, hero):
        self.h = hero

    def pressed(self):
        self.h.train(20)
        self.update_labels()

    def update_labels(self):

        self.lbl_strenght.text = "Siła: " +  str(self.h.skills[0].value)
        self.lbl_defence.text = "Obrona: " +  str(self.h.skills[1].value)
        self.lbl_perception.text = "Percepcja: " +  str(self.h.skills[2].value)
        self.lbl_agility.text = "Zwinność: " +  str(self.h.skills[3].value)
        self.lbl_power.text = "Moc: " +  str(self.h.skills[4].value)
        self.lbl_healing.text = "Uzdrawianie: " +  str(self.h.skills[5].value)
        self.lbl_voodoo.text = "Voodoo: " +  str(self.h.skills[6].value)
        self.lbl_deconcentration.text = "Dekoncentracja: " +  str(self.h.skills[7].value)


class CircleApp(App):
    h = Hero(100, 5)
    index = 0


    def build(self):
       ### Builder.load_string(h_kv_string)
        r = RootWidget()
        r.setHero(self.h)
        return r



CircleApp().run()