from tkinter import *

windows = Tk()
Label(windows, text="너비").grid(row=0)
Label(windows, text="높이").grid(row=1)
e1 = Entry(windows)
e2 = Entry(windows)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
photo = PhotoImage(file="Y:\\스크린샷 2024-10-29 170309.png")
label = Label(windows, image=photo)
label.grid(row=0, column=2, columnspan=2, rowspan=2)
Button(windows, text="이미지 저장").grid(row=2, column=0, columnspan=2)
Button(windows, text="확대").grid(row=2, column=2)
Button(windows, text="축소").grid(row=2, column=3)
windows.mainloop()
