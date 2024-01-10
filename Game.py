import tkinter as tk
from tkinter import messagebox

def print_board(board, buttons):
    for i in range(9):
        if board[i] == 'X':
            buttons[i].config(text='X', state='disabled', bg='light blue')
        elif board[i] == 'O':
            buttons[i].config(text='O', state='disabled', bg='light green')

def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    return False

def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'

    def animate(i):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        buttons[i].config(bg=colors[i%7])
        if board[i] == ' ':
            window.after(100, animate, i)

    def on_click(i):
        nonlocal current_player
        if board[i] != ' ':
            messagebox.showinfo("Invalid move", "Try again.")
            return
        board[i] = current_player
        print_board(board, buttons)
        if check_win(board):
            messagebox.showinfo("Game over", f"Player {current_player} wins!")
            window.quit()
        elif ' ' not in board:
            messagebox.showinfo("Game over", "It's a draw!")
            window.quit()
        current_player = 'O' if current_player == 'X' else 'X'

    window = tk.Tk()
    buttons = []
    for i in range(9):
        button = tk.Button(window, text=' ', command=lambda i=i: on_click(i), height=3, width=6)
        button.grid(row=i//3, column=i%3)
        buttons.append(button)
        window.after(100, animate, i)
    window.mainloop()

tic_tac_toe()