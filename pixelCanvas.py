import tkinter as tk

class PixelCanvas:
    def __init__(self, root):
        self.pixels = [["#ffffff"] * 1000 for _ in range(500)]

        self.canvas = tk.Canvas(root, width=1000, height=500, highlightthickness=0)
        self.canvas.place(x=50, y=50)

        self.img = tk.PhotoImage(width=1000, height=500)
        self.canvas.create_image(0, 0, image=self.img, anchor="nw")
        self.img.put("#ffffff", to=(0, 0, 1000, 500))

        self.color = "#000000"

        self.last = None
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", lambda e: setattr(self, "last", None))

    def set_pixel(self, x, y, color):
        if 0 <= x < 1000 and 0 <= y < 500:
            self.pixels[y][x] = color
            self.img.put(color, to=(x, y, (x + 1), (y + 1)))

    def get_pixel(self, x, y):
        return self.pixels[y][x]

    def paint(self, event):
        x, y = event.x, event.y
        if self.last:
            x0, y0 = self.last
            steps = max(abs(x - x0), abs(y - y0), 1)
            for i in range(steps + 1):
                self.set_pixel(x0 + (x - x0) * i // steps, y0 + (y - y0) * i // steps, self.color)
        else:
            self.set_pixel(x, y, self.color)
        self.last = (x, y)