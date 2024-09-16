import tkinter as tk
from tkinter import messagebox

"""
                    TRASTEANDO
"""
#Variables del juego
#El primer jugador será el X
player= "X"
game_over= False

#Recorremos la lista de buttons para comprobar si hay un ganador
def check_winner():
    for i in range(3):  
        """
        Comprobamos si las filas son iguales y si no están vacias (si están vacias, también son iguales, no?), por ejemplo
        X|X|X|
         | | |
         | | |
        """
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return True
        """
        hacemos lo mismo pero con las columnas
         X| | |
         X| | |
         X| | |
        """
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return True
    """
    Comprobamos si las dos diagonales hacia la derecha son iguales
    X| | |
     |X| |
     | |X|
    """
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    """
    Comprobamos si las dos diagonales hacia la derecha son iguales
     | |X|
     |X| |
    X| | |
    """
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    return False


#Funcion que se ejecuta cuando se hace click en un button
def button_click(row, col):
    #global player, game_over
    print("fila: ",row,", columna: ", col)
    #buttons[row][col]['text'] = player
    #if buttons[row][col]['text'] == "" and not game_over:
    """
    if not game_over:
        buttons[row][col]['text'] = player
        buttons[row][col]["bg"]="#37474f" if player == "X" else "#455a64"
        if player == "X":
            player = "O"
        else:
            player = "X"
        if check_winner():
            messagebox.showinfo("Juego terminado", f"El jugador {player} ha ganado")
            game_over = True
        #Cuando se llena la pantalla y ya no se puede seguir jugando, el juego termina en empate
        elif all(buttons[row][col]['text'] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Juego terminado", "El juego ha terminado en empate")
            game_over = True
        else:
            player = "O" if player == "X" else "X"
        """
    
def reset_game():
    global player, game_over
    player = "X"
    game_over = False
    for r in range(3):
        for c in range(3):
            buttons[r][c]['text'] = ""
            buttons[r][c]["bg"]="#263238"


root=tk.Tk()
root.title("Tres en raya")
root.resizable(False,False)
root.geometry("400x450")
root.configure(bg="#263238")

frame=tk.Frame(root, bg="#263238")
frame.place(relx=0.5, rely=0.5, anchor="center")


buttons = []
for row in range(3):
    for column in range(3):
        button = tk.Button(frame, text="", width=10, height=5, bg="#263238", command=lambda row=row, column=column: button_click(row, column))
        button.grid(row=row, column=column, padx=5, pady=5)
        buttons.append(button)
    
root.mainloop()



