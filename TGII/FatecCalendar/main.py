from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.uix.tabbedpanel import TabbedPanel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.menu import  MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivy.metrics import dp
import pandas as pd
from kivy.properties import ObjectProperty
from siga import acesso_usuario, horario, sobre
from kivy.lang import Builder


Window.size = (600,900)



class MPanel(TabbedPanel):
    def switch(self, tab):
        self.switch_to(tab)
    pass    
    

class Tab(MDFloatLayout,MDTabsBase):
    pass

class Deslogado(Screen):
    def add_table(self, caminho ,dia):
        path = 'FatecCalendar/cursos' + caminho + dia + '.csv'
        tabela = pd.read_csv(path)
        cols = tabela.columns.values
        vals = tabela.values
		# Define Table
        table = MDDataTable(
			pos_hint = {'center_x': 0.5, 'center_y': 0.45},
			size_hint =(0.9, 0.6),
			use_pagination = True,
			rows_num = 10,
			pagination_menu_height = '240dp',
			pagination_menu_pos = "auto",
			background_color = [1,0,0,.5],

			column_data = [
				(col, dp(40))
                for col in cols
			],
			row_data = vals
			)
        self.add_widget(table)

    def navigation(self, tela):
        MDApp.get_running_app().root.current = tela
    ...

class Grade_Deslogado(Screen):


    def add_table(self, curso, sem, dia):

        path = 'grade/' + dia + '.csv'
        tabela = pd.read_csv(path)
        cols = tabela.columns.values
        vals = tabela.values
        screen = Screen()
		# Define Table
        table = MDDataTable(
			pos_hint = {'center_x': 0.5, 'center_y': 0.45},
			size_hint =(0.9, 0.6),
			use_pagination = True,
			rows_num = 10,
			pagination_menu_height = '240dp',
			pagination_menu_pos = "auto",
			background_color = [1,0,0,.5],

			column_data = [
				(col, dp(40))
                for col in cols
			],
			row_data = vals
			)
        self.add_widget(table)
    

class Grade(Screen):
    def add_table(self, arquivo):
        path = 'FatecCalendar/grade/' + arquivo + '.csv'
        tabela = pd.read_csv(path)
        cols = tabela.columns.values
        vals = tabela.values
        screen = Screen()
		# Define Table
        table = MDDataTable(
			pos_hint = {'center_x': 0.5, 'center_y': 0.51},
			size_hint =(0.9, 0.8),
			use_pagination = True,
			rows_num = 10,
			pagination_menu_height = '240dp',
			pagination_menu_pos = "auto",
			background_color = [1,0,0,.5],

			column_data = [
				(col, dp(40))
                for col in cols
			],
			row_data = vals
			)
        self.add_widget(table)
    pass

class Aluno(Screen):
    pass

class Aula(Screen):
    manager = ObjectProperty()
    nav_drawer = ObjectProperty()

    def add_table(self, dia):
        path = 'FatecCalendar/grade/' + dia + '.csv'
        geral = 'FatecCalendar/cursos/geral.csv'
        df_geral = pd.read_csv(geral)
        df = pd.read_csv(path)
        if 'Unnamed: 0' in df.columns:
            df.drop(['Unnamed: 0'], axis=1, inplace=True)
            tabela = df.set_axis(['Horário', 'Disciplina', 'Turma'], axis=1, inplace=False)
            m = pd.merge( tabela, df_geral, on = ['Disciplina', 'Horário'], how='left')
        if 'Unnamed: 0' not in df.columns:
            tabela = df.set_axis(['Horário', 'Disciplina', 'Turma'], axis=1, inplace=False)
            m = pd.merge( tabela, df_geral, on = ['Disciplina', 'Horário'], how='left')
        cols = m.columns.values
        vals = m.values
        screen = Screen()
		# Define Table
        table = MDDataTable(
			pos_hint = {'center_x': 0.5, 'center_y': 0.45},
			size_hint =(0.9, 0.6),
			use_pagination = True,
			rows_num = 10,
			pagination_menu_height = '240dp',
			pagination_menu_pos = "auto",
			background_color = [1,0,0,.5],

			column_data = [
				(col, dp(40))
                for col in cols
			],
			row_data = vals
			)
        self.add_widget(table)
    
    pass

class Faltas(Screen):
    def add_table(self, arquivo):
        path = 'FatecCalendar/info/' + arquivo + '.csv'
        tabela = pd.read_csv(path)
        cols = tabela.columns.values
        vals = tabela.values
        screen = Screen()
		# Define Table
        table = MDDataTable(
			pos_hint = {'center_x': 0.5, 'center_y': 0.51},
			size_hint =(0.9, 0.8),
			use_pagination = True,
			rows_num = 10,
			pagination_menu_height = '240dp',
			pagination_menu_pos = "auto",
			background_color = [1,0,0,.5],

			column_data = [
				(col, dp(40))
                for col in cols
			],
			row_data = vals
			)
        self.add_widget(table)
    pass
    pass

class Avaliacoes(Screen):
    def add_table(self, arquivo):
        path = 'FatecCalendar/info/' + arquivo + '.csv'
        tabela = pd.read_csv(path)
        cols = tabela.columns.values
        vals = tabela.values
        screen = Screen()
		# Define Table
        table = MDDataTable(
			pos_hint = {'center_x': 0.5, 'center_y': 0.51},
			size_hint =(0.9, 0.8),
			use_pagination = True,
			rows_num = 10,
			pagination_menu_height = '240dp',
			pagination_menu_pos = "auto",
			background_color = [1,0,0,.5],

			column_data = [
				(col, dp(40))
                for col in cols
			],
			row_data = vals
			)
        self.add_widget(table)
    pass

class Notas(Screen):
    def add_table(self, arquivo):
        path = 'FatecCalendar/info/' + arquivo + '.csv'
        tabela = pd.read_csv(path)
        cols = tabela.columns.values
        vals = tabela.values
        screen = Screen()
		# Define Table
        table = MDDataTable(
			pos_hint = {'center_x': 0.5, 'center_y': 0.51},
			size_hint =(0.9, 0.8),
			use_pagination = True,
			rows_num = 10,
			pagination_menu_height = '240dp',
			pagination_menu_pos = "auto",
			background_color = [1,0,0,.5],

			column_data = [
				(col, dp(40))
                for col in cols
			],
			row_data = vals
			)
        self.add_widget(table)
    pass

class Extrato(Screen):
    def add_table(self, arquivo):
        path = 'FatecCalendar/info/' + arquivo + '.csv'
        tabela = pd.read_csv(path)
        cols = tabela.columns.values
        vals = tabela.values
        screen = Screen()
		# Define Table
        table = MDDataTable(
			pos_hint = {'center_x': 0.5, 'center_y': 0.51},
			size_hint =(0.9, 0.8),
			use_pagination = True,
			rows_num = 10,
			pagination_menu_height = '240dp',
			pagination_menu_pos = "auto",
			background_color = [1,0,0,.5],

			column_data = [
				(col, dp(40))
                for col in cols
			],
			row_data = vals
			)
        self.add_widget(table)
    pass

class Content(BoxLayout):
    manager = ObjectProperty()
    nav_drawer = ObjectProperty()

    def navigation(self, tela):
        MDApp.get_running_app().root.current = tela

class DemoProject(ScreenManager):

    def home(self):
        MDApp.get_running_app().root.current = "login"

    Clock.schedule_once(home, 8)
    
    def navigation(self, tela):
        MDApp.get_running_app().root.current = tela

    def on_start(self):
        #Cria o dorp menu
        self.dropdown = MDDropdownMenu(width_mult=4)

        for i in range(6):
            self.dropdown.items.append(
                {
                    "viewclass": "MDMenuItem",
                    "text": "Option" + str(i),
                    "callback": self.option_callback
                }
            )


    
    
class Splash(Screen):  
    ...

class Logado(Screen):  
    ...

class Login(Screen):  
    ...

class Myapp(MDApp):
    dropdown = ObjectProperty()
    dialog = None
    
    def logar_siga(self):
        usuario = self.root.ids.user.text
        senha = self.root.ids.senha.text
        navegador = acesso_usuario(usuario,senha)
        horario(navegador)
        return print(f'usuario: {usuario}, senha: {senha}')
    

    def option_callback(self, text_of_the_option):
        print(text_of_the_option)

    def show_alert_dialog(self):
        curso = self.root.ids.btn.text
        semestre = self.root.ids.sem.text

        if (curso == 'Clique para selecionar') or (semestre == 'Clique para selecionar'):
            if not self.dialog:
                self.dialog = MDDialog(
                    title = "Erro!!! Você não selecionou os campos corretamente!",
                    text = "Selecione um Curso e um Semestre para proseguir...",
                    buttons =[
                        MDRectangleFlatButton(
                            text="OK", text_color=self.theme_cls.primary_color, on_release = self.close_dialog
                            ),
                        ],
                    )
            self.dialog.open()
            return True
        else:
            #caminho = '/' + curso + '/' + semestre
            return False

    def alerta_user(self):
        usuario = self.root.ids.user.text
        senha = self.root.ids.senha.text

        if (usuario == '') or (senha == ''):
            if not self.dialog:
                self.dialog = MDDialog(
                    title = "Erro!!! Você Precisa digitar todos os campos!",
                    text = "Digite seu Usuário e Senha do SIGA para proseguir...",
                    buttons =[
                        MDRectangleFlatButton(
                            text="OK", text_color=self.theme_cls.primary_color, on_release = self.close_dialog
                            ),
                        ],
                    )
            self.dialog.open()
            return True
        else:
            #caminho = '/' + curso + '/' + semestre
            return False
    

    def path(self):
        curso = self.root.ids.btn.text
        semestre = self.root.ids.sem.text
        path = '/' + curso + '/' + semestre + '/'
        return path

    def close_dialog(self, obj):
        self.dialog.dismiss()

    

    def build(self):
        self.theme_cls.primary_palette = 'DeepOrange'
        #self.theme_cls.primary_light = ""
        Builder.load_file('interface.kv')
        return DemoProject()

Myapp().run()