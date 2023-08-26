from tkinter import*
from PIL import ImageTk, Image
root=Tk()

my_img1=ImageTk.PhotoImage(Image.open("C:\\Users\\nkvir\\OneDrive\\Desktop\\alot\\car2.png"))
my_img2=ImageTk.PhotoImage(Image.open("C:\\Users\\nkvir\\OneDrive\\Desktop\\alot\\image2.png"))
my_img3=ImageTk.PhotoImage(Image.open("C:\\Users\\nkvir\\OneDrive\\Desktop\\alot\\thiss.jpeg"))
my_img4=ImageTk.PhotoImage(Image.open("C:\\Users\\nkvir\\OneDrive\\Desktop\\alot\\image2.png"))

img_list=[my_img1, my_img2, my_img3, my_img4]

my_label=Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)



def forward(img_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label=Label(image= img_list[img_number -1]) 
    button_forward=Button(root, text= ">>", command=lambda: forward(img_number + 1))
    button_back=Button(root, text= ">>", command=lambda: back(img_number - 1))
    


    if img_number==4:
        button_forward=Button(root, text= " >>", state= DISABLED)

    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)



def back(img_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label=Label(image= img_list[img_number -1]) 
    button_forward=Button(root, text= ">>", command=lambda: forward(img_number + 1))
    button_back=Button(root, text= ">>", command=lambda: back(img_number - 1))
    


    if img_number==1:
        button_back=Button(root, text= " <<", state= DISABLED)

    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)




 











button_back=Button(root, text="<<",command=back,state=DISABLED)
button_forward=Button(root,text=">>", command=lambda : forward(2))
button_exit=Button(root, text="exit program", command=root.quit)


button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)
button_exit.grid(row=1, column=1)


root.mainloop()
