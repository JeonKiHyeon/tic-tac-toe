from tkinter import *

def checked(i) :
      global player
      button = list[i]
      win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"
      
      for x in win:
            if player == list[x[0]]["text"] == list[x[1]]["text"] == list[x[2]]["text"]:
                  tkinter.messagebox.showinfo("game over", "{0} player win!".format(player))

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


