import tkinter as tk
from tkinter import messagebox

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")
        
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(master, text=" ", font=("Helvetica", 20), width=6, height=3,
                                   command=lambda row=row, col=col: self.make_move(row, col))
                button.grid(row=row, column=col, sticky="nsew")
                button_row.append(button)
            self.buttons.append(button_row)
        
        reset_button = tk.Button(master, text="Reiniciar", command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")
        
    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].configure(text=self.current_player)
            
            if self.check_winner(self.current_player):
                messagebox.showinfo("Fim do jogo", f"O jogador {self.current_player} venceu!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Fim do jogo", "Empate!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False
    
    def check_draw(self):
        for row in self.board:
            if " " not in row:
                return False
        return True
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.configure(text=" ")
                
root = tk.Tk()
game = Game(root)
root.mainloop()
