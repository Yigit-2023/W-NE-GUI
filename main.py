#Yazan Yiğit çıtak
import tkinter as tk
from os import system

sürüm = 1.0

logo = """
               /\\
              /  \\
             /    \\
            /      \\
           /        \\
          /          \\
         / \\         /\\
        /   \\       /  \\
       /     \\     /    \\
      /       \\   /      \\
     /         \\ /        \\
    /           |          \\
   /            |           \\
  /             |            \\
 /              |             \\
/______________________________\\
"""

print(f"Sürüm: 1.0\nHazırlayan: Yiğit Çıtak\n{logo}")

def wine_start():
	system(f"wine exe/{wine_start_entry.get()}")

def wine_install():
	system("sudo apt install wine")

pencere = tk.Tk()

boyutX = 600
boyutY = 700
pencere.title("Wine gui")
pencere.minsize(boyutX,boyutY)
pencere.maxsize(boyutX,boyutY)

bosluk0 = tk.Label(pencere,text="\n\n")
bosluk0.pack()

wine_install_button = tk.Button(pencere,text="Wine kur",font="italic 40",command=wine_install)
wine_install_button.pack()

bosluk1 = tk.Label(pencere,text="\n\n\n\n\n")
bosluk1.pack()

wine_start_entry = tk.Entry(pencere)
wine_start_entry.pack()

wine_start_button = tk.Button(pencere,text="Çalıştır",font="italic 20",command=wine_start)
wine_start_button.pack()

#bosluk1 = tk.Label(pencere,text=f"\n\n\n{logo}")
#bosluk1.pack()

pencere.mainloop()
