kv_minimalista = '''
ScreenManager:
    TelaInicio:
    TelaLogin:

<TelaInicio>:
    name: 'tela_inicio'
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 30
        canvas.before:
            Color:
                rgba: 0.9, 0.9, 0.9, 1
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [20]

        Label:
            text: "The Writing Board"
            font_size: 32
            bold: True
            color: (0, 0.5, 1, 1)

        Image:
            source: 'sua_imagem.png'  # Substitua pelo caminho da sua imagem
            size_hint: (1, 0.5)

        Button:
            text: "Iniciar"
            font_size: 18
            size_hint: (0.5, 0.2)
            pos_hint: {"center_x": 0.5}
            background_color: (0, 0.7, 0.3, 1)
            on_release: app.root.current = 'tela_login'

<TelaLogin>:
    name: 'tela_login'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [20]

        Label:
            text: "Login"
            font_size: 24
            color: (0, 0, 0, 1)

        TextInput:
            hint_text: "E-mail"
            size_hint_y: None
            height: 40

        TextInput:
            hint_text: "Senha"
            size_hint_y: None
            height: 40
            password: True

        Button:
            text: "Entrar"
            font_size: 18
            size_hint: (0.5, 0.2)
            pos_hint: {"center_x": 0.5}
            background_color: (0, 0.5, 1, 1)
            on_release: app.root.current = 'tela_inicio'
'''
