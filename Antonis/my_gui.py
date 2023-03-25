#D://recordings/InteractionHumanAndMachine/background_image.png


import tkinter as tk
from PIL import Image, ImageTk

class AnimatedGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x600')

        # Create frames for the animation and buttons
        self.animation_frame = tk.Frame(self.master)
        self.button_frame = tk.Frame(self.master, bg='black')

        # Load images for the animation
        self.images = []
        for i in range(1, 335):
            image_path = f'D://recordings/InteractionHumanAndMachine/New folder/new_name_{i}.jpg'
            image = Image.open(image_path).convert('RGBA')
            self.images.append(ImageTk.PhotoImage(image))

        # Create a label to display the animation
        self.animation_label = tk.Label(self.animation_frame, image=self.images[0], bg='black')
        self.animation_label.pack()

        # Create buttons
        self.button1 = tk.Button(self.button_frame, text='Button 1', command=self.button1_function)
        self.button2 = tk.Button(self.button_frame, text='Button 2', command=self.button2_function)
        self.button3 = tk.Button(self.button_frame, text='Button 3', command=self.button3_function)
        self.button4 = tk.Button(self.button_frame, text='Button 4', command=self.button4_function)
        self.button5 = tk.Button(self.button_frame, text='Button 5', command=self.button5_function)
        self.button6 = tk.Button(self.button_frame, text='Button 6', command=self.button6_function)

        # Pack buttons
        self.button1.pack(side='left', padx=10, pady=0)
        self.button2.pack(side='left', padx=10, pady=0)
        self.button3.pack(side='left', padx=10, pady=0)
        self.button4.pack(side='left', padx=10, pady=0)
        self.button5.pack(side='left', padx=10, pady=0)
        self.button6.pack(side='left', padx=10, pady=0)

        # Pack frames
        self.button_frame.pack(side='bottom', fill='x')
        self.animation_frame.pack(fill='both', expand=True)
       
       

        # Start animation
        self.current_image = 0
        self.animate()

    def animate(self):
        self.animation_label.config(image=self.images[self.current_image])
        self.current_image = (self.current_image + 1) % len(self.images)
        self.master.after(20, self.animate)

    def button1_function(self):
        print('Button 1 was pressed!')

    def button2_function(self):
        print('Button 2 was pressed!')

    def button3_function(self):
        print('Button 3 was pressed!')

    def button4_function(self):
        print('Button 4 was pressed!')

    def button5_function(self):
        print('Button 5 was pressed!')

    def button6_function(self):
        print('Button 6 was pressed!')

# Create the GUI
root = tk.Tk()
app = AnimatedGUI(root)
root.mainloop()
