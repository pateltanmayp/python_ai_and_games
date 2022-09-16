from tkinter import *
import random
 
class Game:
    def __init__(self, main, dim):
        self.values = []
        self.squares = []
        self.dim = dim
        self.rands = [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.score_val = 0
 
        self.colours = {
            2: "#EEE4DA",
            4: "#EDE0C8",
            8: "#F2B179",
            16: "#F59563",
            32: "#F67C5F",
            64: "#F65E3B",
            128: "#EDCF72",
            256: "#EDCC61",
            512: "#EDC850",
            1024: "#EDC53F",
            2048: "#EDC22E"
        }
 
        self.title = Label(main, text = "2048", padx = 100, pady = 30, font = ("Helvetica", 28), bg = "#D3D3D3", fg = "#3A3B3C")
        self.score = Label(main, text = "SCORE\n" + str(self.score_val), padx = 95, pady = 25, font = ("Helvetica", 15), bg = "#3A3B3C", fg = "#D3D3D3")
        self.title.grid(row = 0, column = 0, columnspan = 2, sticky = N+S+E+W)
        self.score.grid(row = 0, column = 2, columnspan = 2, padx = 5, pady = 5, sticky = N+S+E+W)
 
        self.left_btn = Button(main, text = "LEFT", padx = 50, pady = 20, command = self.left)
        self.right_btn = Button(main, text = "RIGHT", padx = 50, pady = 20, command = self.right)
        self.up_btn = Button(main, text = " UP ", padx = 50, pady = 20, command = self.up)
        self.down_btn = Button(main, text = "DOWN", padx = 50, pady = 20, command = self.down)
        self.left_btn.grid(row = 5, column = 0, sticky = N+S+E+W)
        self.right_btn.grid(row = 5, column = 3, sticky = N+S+E+W)
        self.up_btn.grid(row = 5, column = 1, sticky = N+S+E+W)
        self.down_btn.grid(row = 5, column = 2, sticky = N+S+E+W)
        
        for i in range(self.dim):
            self.squares.append([])
            for j in range(self.dim):
                self.squares[i].append(Label(main, padx = 45, pady = 45, font = ("Helvetica", 15)))
                self.squares[i][j].grid(row = i + 1, column = j, sticky = N+S+E+W, padx = 5, pady = 5)
        self.create_grid()
        self.update()
    
    def create_grid(self):
        for i in range(self.dim):
            self.values.append([])
            for j in range(self.dim):
                rand_index = random.randint(0, len(self.rands) - 1)
                rand = self.rands[rand_index]
                self.values[i].append(rand)
                self.rands.pop(rand_index)
 
    def update(self):
        for i in range(self.dim):
            for j in range(self.dim):
                if self.values[i][j] == 0:
                    self.squares[i][j]['text'] = ""
                    self.squares[i][j]['bg'] = "#f0f0ed"
                else:
                    self.squares[i][j]['text'] = str(self.values[i][j])
                    self.squares[i][j]['bg'] = self.colours[self.values[i][j]]
        self.score['text'] = "SCORE\n" + str(self.score_val)
 
    def add_new(self):
        empty_spaces = []
        for i in range(self.dim):
            for j in range(self.dim):
                if self.values[i][j] == 0:
                    empty_spaces.append([i, j])
        try:
            rand = random.randint(0, len(empty_spaces) - 1)
            self.values[empty_spaces[rand][0]][empty_spaces[rand][1]] = 2
        except Exception as e:
            return
 
    def merge(self):
        for i in range(self.dim):
            for j in range(self.dim - 1):
                if self.values[i][j] == self.values[i][j + 1]:
                    self.values[i][j] *= 2
                    self.score_val += self.values[i][j]
                    self.values[i][j + 1] = 0
 
    def shift(self):
        for i in range(self.dim):
            for j in range(self.dim - 1):
                for k in range(self.dim - j - 1):
                    if self.values[i][j] == 0:
                        for l in range(j, self.dim - 1):
                            self.values[i][l] = self.values[i][l + 1]
                        self.values[i][3] = 0
    
    def reverse(self):
        for i in range(self.dim):
            for j in range(self.dim // 2):
                self.values[i][j], self.values[i][self.dim - j - 1] = self.values[i][self.dim - j - 1], self.values[i][j]
 
    def rotate(self):
        for i in range(self.dim - 1):
            for j in range(i + 1, self.dim):
                self.values[j][i], self.values[i][j] = self.values[i][j], self.values[j][i]
 
    def left(self):
        self.shift()
        self.merge()
        self.shift()
        self.add_new()
        self.update()
 
    def right(self):
        self.reverse()
        self.shift()
        self.merge()
        self.shift()
        self.reverse()
        self.add_new()
        self.update()
    
    def up(self):
        self.rotate()
        self.shift()
        self.merge()
        self.shift()
        self.rotate()
        self.add_new()
        self.update()
 
    def down(self):
        self.rotate()
        self.reverse()
        self.shift()
        self.merge()
        self.shift()
        self.reverse()
        self.rotate()
        self.add_new()
        self.update()
 
    def check_end():
        return
 
root = Tk()
root.title("Play 2048!")
root.configure(bg = "#D3D3D3")
game = Game(root, 4)
root.mainloop()