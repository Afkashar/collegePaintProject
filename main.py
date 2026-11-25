import tkinter as tk
from pixelCanvas import PixelCanvas

root = tk.Tk()
root.title('Shape editor')
root.minsize(1100, 800)
root.maxsize(1100, 800)
root.configure(bg='#E0E0E0')

tk.Label(root, text='Change Color').place(x=50, y=600)
changeColorEntry = tk.Entry(root)
changeColorEntry.place(x=50, y=625)

def SetColor():
    newColor = '#' + changeColorEntry.get()
    app.color = newColor

changeColorButton = tk.Button(root, text='Set Color', command=SetColor).place(x=50, y=650)

app = PixelCanvas(root)

root.mainloop()