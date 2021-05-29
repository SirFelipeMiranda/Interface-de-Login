from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('DarkBlue3')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login')],
    [sg.Button('Entrar')],
    [sg.Button('Esqueci minha senha')],
    [sg.Text('Criado por Felipe Miranda')]
]

# Janela
win1 = sg.Window('Tela de Login', layout)
win2_active=False
#ler eventos
while True:
    eventos, valores = win1.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores ['usuario'] == 'Felipe' and valores ['senha']== '123456':
            print('Acesso realizado com sucesso!')
        else:
            print('login ou senha errados')
    if eventos == 'Esqueci minha senha' and not win2_active:
        win2_active = True
        win1.Hide()
        
#layout2
        sg.theme('Darkblue3')
        layout2 = [
            [sg.Text('Esqueceu sua senha?')],
            [sg.Text ('É uma sequência númerica')],
            [sg.Text('Não conseguiu lembrar? Diga seu e-mail'), sg.Input(key='e-mail')],
            [sg.Button ('Enviar e-mail')],
            [sg.Button('Voltar')],
            [sg.Text('Criado por Felipe Miranda')]]
#janela2
        win2 = sg.Window('Esqueceu sua senha?', layout2)
        while True:
            ev2, vals2 = win2.read()
            if ev2 == sg.WIN_CLOSED or ev2 == 'Voltar':
                win2.close()
                win2_active = False
                win1.UnHide()
                break
            
