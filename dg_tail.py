import pyautogui
import pygetwindow as gw
import time

def encontrar_icone(imagem_icone):
    localizacao = pyautogui.locateCenterOnScreen(imagem_icone, confidence=0.8)
    return localizacao

def clicar_icone(imagem_icone, pixel_to_move = None):
    posicao = encontrar_icone(imagem_icone)
    if posicao is not None:
        if pixel_to_move:
            pyautogui.moveRel(0, -pixel_to_move)
        pyautogui.moveTo(posicao)
        time.sleep(0.5)
        pyautogui.click(duration=0.2)
    else:
        print(f"Ícone {imagem_icone} não encontrado.")

def auth():
    try:
        encontrar_icone("assets/number_password.png")
    except:
        print("Inserindo a senha...")
        clicar_icone("assets/auth.png")
        pyautogui.write('9595', interval=0.1)

def trocar_para_janela(nome_janela):
    janela = gw.getWindowsWithTitle(nome_janela)
    if janela:
        janela[0].activate()
        print(f"Janela {nome_janela} ativada.")
    else:
        print(f"Janela {nome_janela} não encontrada.")

def mover_mouse_direita(distancia):
    pyautogui.moveRel(distancia, 0)

def mover_mouse_cima(distancia):
    pyautogui.moveRel(0, -distancia)

def mover_mouse_centro():
    tela_largura, tela_altura = pyautogui.size()
    centro_x = tela_largura / 2
    centro_y = tela_altura / 2
    pyautogui.moveTo(centro_x, centro_y)

def scroll_down(times_to_scroll):
    for time in range(times_to_scroll):
        pyautogui.scroll(-500)


dg_type = "isobu" # Available: isobu, yonbi, kokuou, nibi
icones = ['dg.png', 'create.png', f'{dg_type}.png']
base_window_name = "Split - "
chars = ['El Copas', "El Debito", "El Credito"]
main_name = "El Cartas"
runs = 10

if __name__ == "__main__":
    for run in range(runs):
        print(f"Run {run+1}/{runs}")
        try:
            trocar_para_janela(f"{base_window_name}{main_name}")
        except:
            print("Falhou em trocar janela")
        time.sleep(1)
        mover_mouse_centro()
        time.sleep(2)

        for icone in icones:
            if icone in ["yonbi.png", "kokuou.png"]:
                mover_mouse_cima(100)
                time.sleep(1)
                scroll_down(4)

            clicar_icone(f"assets/{icone}")
            time.sleep(2)

        auth()
        clicar_icone("assets/done.png")
        print("Lobby criado...")

        for char in chars:
            time.sleep(0.5)
            mover_mouse_centro()
            trocar_para_janela(f"{base_window_name}{char}")
            time.sleep(0.5)
            clicar_icone(f"assets/dg.png")
            time.sleep(1)
            clicar_icone(f"assets/locked.png")
            mover_mouse_direita(530)
            time.sleep(0.5)
            pyautogui.click()
            clicar_icone("assets/auth_maker_dg.png")
            pyautogui.write('9595', interval=0.1)
            clicar_icone("assets/join_dg.png")
            time.sleep(2)
        
        print("Começando a DG")
        trocar_para_janela(f"{base_window_name}{main_name}")
        time.sleep(1)
        clicar_icone("assets/start_dg.png", 0)
        time.sleep(610)

