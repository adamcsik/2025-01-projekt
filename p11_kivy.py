from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window
import requests

# opcionálisan beállítjuk a háttérszínt
Window.clearcolor = (0.95, 0.95, 0.95, 1)


class KockaFrontend(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        #self.api_url = "http://localhost:5000/api"
        self.api_url = "http://192.168.1.9:5000/api" #MOBILON
        # Cím
        self.add_widget(Label(text="Kockadobás Flask API-val", font_size=24, size_hint=(1, 0.2), color=(0,0,0,1)))

        # Véletlen szám gomb + címke
        btn_data = Button(text="Véletlen szám lekérése")
        btn_data.bind(on_press=self.get_data)
        self.add_widget(btn_data)

        self.data_label = Label(text="...", font_size=20, color=(0,0,0,1))
        self.add_widget(self.data_label)

        # Dobás bemenet
        self.input = TextInput(text="10", multiline=False, halign="center", font_size=18, size_hint=(1, None))
        self.add_widget(self.input)

        btn_dobas = Button(text="Dobás a backendben")
        btn_dobas.bind(on_press=self.api_dobas)
        self.add_widget(btn_dobas)

        self.result_label = Label(text="", font_size=18, color=(1,0,0,1) )
        self.result_label.bind(texture_size=self.result_label.setter("size"))
        self.add_widget(self.result_label)

        # Összesítés
        btn_osszes = Button(text="Összesítés lekérése")
        btn_osszes.bind(on_press=self.api_osszes)
        self.add_widget(btn_osszes)

        self.osszes_label = Label(text="", font_size=18, color=(0,1,0,1))
        self.add_widget(self.osszes_label)

    # ---- Flask API hívások ----

    def show_error(self, msg):
        Popup(title="Hiba", content=Label(text=msg), size_hint=(0.7, 0.4)).open()

    def get_data(self, instance):
        try:
            r = requests.get(f"{self.api_url}/data", timeout=3)
            r.raise_for_status()
            data = r.json()
            self.data_label.text = f"Véletlen szám: {data['uzenet']}"
            self.input.text = str(data["uzenet"])
        except Exception as e:
            self.show_error(f"Nem sikerült az adatlekérés:\n{e}")

    def api_dobas(self, instance):
        try:
            dbszam = int(self.input.text)
            r = requests.get(f"{self.api_url}/dobas/{dbszam}", timeout=3)
            r.raise_for_status()
            data = r.json()
            eredmenyek = data["eredmenyek"]
            self.result_label.text = "\n".join(f"{i + 1} - {eredmenyek[i]}" for i in range(6))
        except Exception as e:
            self.show_error(f"Nem sikerült a dobás:\n{e}")

    def api_osszes(self, instance):
        try:
            r = requests.get(f"{self.api_url}/osszesites", timeout=3)
            r.raise_for_status()
            data = r.json()
            osszes = data["osszesites"]
            self.osszes_label.text = "\n".join(f"{i + 1} - {osszes[i]}" for i in range(6))
        except Exception as e:
            self.show_error(f"Nem sikerült az összesítés:\n{e}")


class KockaApp(App):
    def build(self):
        return KockaFrontend()


if __name__ == "__main__":
    KockaApp().run()
