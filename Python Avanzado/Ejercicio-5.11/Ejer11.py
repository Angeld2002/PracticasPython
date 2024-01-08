import csv
import hashlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class LoginApp(App):
    def build(self):
        self.cargarUsuarios()

        # Crear widgets
        self.username_input = TextInput(hint_text='Usuario')
        self.password_input = TextInput(hint_text='Contraseña', password=True)
        self.result_label = Label(text='')

        login_button = Button(text='Comprobar', on_press=self.comprobarUsuario)

        # Crear diseño
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)
        layout.add_widget(self.result_label)

        return layout

    def cargarUsuarios(self):
        self.users = {}
        with open('users.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar="'")
            for row in reader:
                self.users[row[0]] = row[1]

    def comprobarUsuario(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        if username in self.users and self.comprobarContrasena(username, password):
            self.result_label.text = 'OK'
        else:
            self.result_label.text = 'ERROR'

    def comprobarContrasena(self, username, plain_password):
        hashed_password = hashlib.sha1(plain_password.encode('utf-8')).hexdigest()
        return hashed_password == self.users[username]

if __name__ == '__main__':
    LoginApp().run()