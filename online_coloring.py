#Ahmet Melih Turkmen , basic coloring program , 06.03.2018

from tkinter import *
from tkinter.colorchooser import askcolor
import tkinter.filedialog
import PIL.Image
import PIL.ImageTk
from PIL import ImageTk
from random import randint

choosenColor = 0, 0, 0
drawingImage = None

width = 1000
height = 700
counter = 0
undolist = []

# This menu function contains menu and all of menu buttons

def main():
    global root
    root = Tk()
    print("Started")
    root.title("Project")
    global width
    global height
    resolution = str(width) + 'x' + str(height)
    root.geometry(resolution)

    background_image = tkinter.PhotoImage(file="mef.png")
    background_label = tkinter.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Add Image", command=fileopen)
    file_menu.add_command(label="Save Image", command=filesave)
    menu_bar.add_cascade(label="File Operations", menu=file_menu)

    image_menu = Menu(menu_bar, tearoff=0)
    image_menu.add_command(label="Clear Image", command=clearimage)
    image_menu.add_command(label="Shuffle Image", command=shuffle)
    menu_bar.add_cascade(label="Image Operations", menu=image_menu)



    root.config(menu=menu_bar)

    groundmenu = Frame(root, bd=3, relief=SUNKEN)

    white = Button(groundmenu, text="White", borderwidth=0, command=lambda: makewhite())
    whiteImg = tkinter.PhotoImage(file="colorbuttons\\white.png")
    white.config(image=whiteImg)
    white.image = whiteImg
    white.pack(side=LEFT, padx=2, pady=2)

    lightgrey = Button(groundmenu, text="Light Grey", borderwidth=0, command=lambda: makelightgrey())
    lightgreyImg = tkinter.PhotoImage(file="colorbuttons\\light grey.png")
    lightgrey.config(image=lightgreyImg)
    lightgrey.image = lightgreyImg
    lightgrey.pack(side=LEFT, padx=2, pady=2)

    darkgrey = Button(groundmenu, text="Dark Grey", borderwidth=0, command=lambda: makedarkgrey())
    darkgreyImg = tkinter.PhotoImage(file="colorbuttons\\dark grey.png")
    darkgrey.config(image=darkgreyImg)
    darkgrey.image = darkgreyImg
    darkgrey.pack(side=LEFT, padx=2, pady=2)

    black = Button(groundmenu, text="Black", borderwidth=0, command=lambda: makeblack())
    blackImg = tkinter.PhotoImage(file="colorbuttons\\black.png")
    black.config(image=blackImg)
    black.image = blackImg
    black.pack(side=LEFT, padx=2, pady=2)

    darkred = Button(groundmenu, text="Dark Red", borderwidth=0, command=lambda: makedarkred())
    darkredImg = tkinter.PhotoImage(file="colorbuttons\\dark red.png")
    darkred.config(image=darkredImg)
    darkred.image = darkredImg
    darkred.pack(side=LEFT, padx=2, pady=2)

    red = Button(groundmenu, text="Red", borderwidth=0, command=lambda: makered())
    redImg = tkinter.PhotoImage(file="colorbuttons\\red.png")
    red.config(image=redImg)
    red.image = redImg
    red.pack(side=LEFT, padx=2, pady=2)

    orange = Button(groundmenu, text="Orange", borderwidth=0, command=lambda: makeorange())
    orangeImg = tkinter.PhotoImage(file="colorbuttons\\orange.png")
    orange.config(image=orangeImg)
    orange.image = orangeImg
    orange.pack(side=LEFT, padx=2, pady=2)

    gold = Button(groundmenu, text="Gold", borderwidth=0, command=lambda: makegold())
    goldImg = tkinter.PhotoImage(file="colorbuttons\\gold.png")
    gold.config(image=goldImg)
    gold.image = goldImg
    gold.pack(side=LEFT, padx=2, pady=2)

    lightyellow = Button(groundmenu, text="Light Yellow", borderwidth=0, command=lambda: makelightyellow())
    lightyellowImg = tkinter.PhotoImage(file="colorbuttons\\light yellow.png")
    lightyellow.config(image=lightyellowImg)
    lightyellow.image = lightyellowImg
    lightyellow.pack(side=LEFT, padx=2, pady=2)

    yellow = Button(groundmenu, text="Yellow", borderwidth=0, command=lambda: makeyellow())
    yellowImg = tkinter.PhotoImage(file="colorbuttons\\yellow.png")
    yellow.config(image=yellowImg)
    yellow.image = yellowImg
    yellow.pack(side=LEFT, padx=2, pady=2)

    darkgreen = Button(groundmenu, text="Dark Green", borderwidth=0, command=lambda: makedarkgreen())
    darkgreenImg = tkinter.PhotoImage(file="colorbuttons\\dark green.png")
    darkgreen.config(image=darkgreenImg)
    darkgreen.image = darkgreenImg
    darkgreen.pack(side=LEFT, padx=2, pady=2)

    green = Button(groundmenu, text="Green", borderwidth=0, command=lambda: makegreen())
    greenImg = tkinter.PhotoImage(file="colorbuttons\\green.png")
    green.config(image=greenImg)
    green.image = greenImg
    green.pack(side=LEFT, padx=2, pady=2)

    cyan = Button(groundmenu, text="Cyan", borderwidth=0, command=lambda: makecyan())
    cyanImg = tkinter.PhotoImage(file="colorbuttons\\cyan.png")
    cyan.config(image=cyanImg)
    cyan.image = cyanImg
    cyan.pack(side=LEFT, padx=2, pady=2)

    turquoise = Button(groundmenu, text="Turquoise", borderwidth=0, command=lambda: maketurquoise())
    turquoiseImg = tkinter.PhotoImage(file="colorbuttons\\turquoise.png")
    turquoise.config(image=turquoiseImg)
    turquoise.image = turquoiseImg
    turquoise.pack(side=LEFT, padx=2, pady=2)

    blue = Button(groundmenu, text="Blue", borderwidth=0, command=lambda: makeblue())
    blueImg = tkinter.PhotoImage(file="colorbuttons\\blue.png")
    blue.config(image=blueImg)
    blue.image = blueImg
    blue.pack(side=LEFT, padx=2, pady=2)

    purple = Button(groundmenu, text="Purple", borderwidth=0, command=lambda: makepurple())
    purpleImg = tkinter.PhotoImage(file="colorbuttons\\purple.png")
    purple.config(image=purpleImg)
    purple.image = purpleImg
    purple.pack(side=LEFT, padx=2, pady=2)

    pink = Button(groundmenu, text="Pink", borderwidth=0, command=lambda: makepink())
    pinkImg = tkinter.PhotoImage(file="colorbuttons\\pink.png")
    pink.config(image=pinkImg)
    pink.image = pinkImg
    pink.pack(side=LEFT, padx=2, pady=2)

    brown = Button(groundmenu, text="Brown", borderwidth=0, command=lambda: makebrown())
    brownImg = tkinter.PhotoImage(file="colorbuttons\\brown.png")
    brown.config(image=brownImg)
    brown.image = brownImg
    brown.pack(side=LEFT, padx=2, pady=2)

    pickcolor = Button(groundmenu, text='Select Color', command=getcolor)
    pickcolorImg = tkinter.PhotoImage(file="colorbuttons\\colorchooser.png")
    pickcolor.config(image=pickcolorImg)
    pickcolor.image = pickcolorImg
    pickcolor.pack(side=LEFT, padx=2, pady=2)

    color = Button(groundmenu, text='Color Chooser', command=learncolor)
    colorImg = tkinter.PhotoImage(file="colorbuttons\\colorpicker.png")
    color.config(image=colorImg)
    color.image = colorImg
    color.pack(side=LEFT,padx=2,pady=2)

    undoimage = Button(groundmenu, text ='Undo Image', command=undo)
    undoImg = tkinter.PhotoImage(file="colorbuttons\\undo.png")
    undoimage.config(image=undoImg)
    undoimage.image = undoImg
    undoimage.pack(side=LEFT,padx=2,pady=2)

    redoimage = Button(groundmenu, text='Redo Image', command=redo)
    redoImg = tkinter.PhotoImage(file="colorbuttons\\redo.png")
    redoimage.config(image=redoImg)
    redoimage.image = redoImg
    redoimage.pack(side=LEFT, padx=2, pady=2)

    groundmenu.pack(side=BOTTOM)

    root.mainloop()


#Function for specific color choosing

def getcolor():
    color = askcolor(parent=root)
    color = str(color)
    start = color.index("((")
    stop = color.index("),")
    color = color[start:stop]
    color = color[2:len(color)]
    r, g, b = color.split(",")
    global choosenColor
    choosenColor = int(float(r)), int(float(g)), int(float(b))

#Clear the all changes on image

def clearimage():

    for uc in range (len(undolist)):
        m, n, p, r = undolist[uc]

        for j in range(1, ySize - 1):
            for i in range(1, xSize - 1):
                if labelValue[i][j] == labelValue[m][n]:
                    pix[i, j] = p
                    drawingImage.putpixel((m, n), p)

    render = ImageTk.PhotoImage(drawingImage)
    img = Label(root, image=render)
    img.image = render
    img.place(x=a, y=c)
    img.bind("<Button-1>", paintcoords)


# Save the image as a .png file in choosen folder

def filesave():

    filename = tkinter.filedialog.asksaveasfilename()
    filename = filename + ".png"
    drawingImage.save(filename)


#Open the image from choosen folder

def fileopen():
    global file_path_string
    file_path_string = tkinter.filedialog.askopenfilename()
    fp = open(file_path_string, "rb")

    global drawingImage
    drawingImage = PIL.Image.open(fp)
    drawingImage = drawingImage.convert('RGB')
    global pix
    pix = drawingImage.load()
    global xSize
    global ySize
    xSize, ySize = drawingImage.size

    for i in range(xSize):
        for j in range(ySize):

           pix[i, j] = clean(pix[i, j])


    pixelValue = [[0 for x in range(ySize)] for y in range(xSize)]

    for i in range(xSize):
        for j in range(ySize):
            pixelValue[i][j] = convertbinary(pix[i, j])

    for i in range(xSize):
        for j in range(ySize):
            if i == 0 or j == 0 or i == xSize - 1 or j == ySize - 1:
                pixelValue[i][j] = 0
        # We made edges as black
    # print "\n\n\n\nbefore labeling pixelValues matrix look like"
    # for j in range(ySize):
    # for i in range(xSize):
    # print pixelValue[i][j],
    # print ""

    global labelValue

    labelValue = [[0 for x in range(ySize)] for y in range(xSize)]
    for i in range(xSize):
        for j in range(ySize):
            labelValue[i][j] = 0

    labelCounter = 2  # labels start from 2

    global list
    list = []
    

    for i in range(1, xSize - 1):
        for j in range(1, ySize - 1):
            if pixelValue[i][j] == 1:  # current is White
                if pixelValue[i - 1][j] == 1 or pixelValue[i][j - 1] == 1 or pixelValue[i - 1][j - 1] == 1 or \
                        pixelValue[i + 1][j - 1] == 1:
                    if pixelValue[i - 1][j] == 1 and pixelValue[i][j - 1] == 1 and pixelValue[i - 1][j - 1] == 1 and \
                            pixelValue[i + 1][j - 1] == 1:
                        if labelValue[i - 1][j] == labelValue[i][j - 1] and labelValue[i - 1][j] == labelValue[i + 1][
                            j - 1] and labelValue[i - 1][j] == labelValue[i - 1][j - 1] and labelValue[i - 1][j] != 0:

                            labelValue[i][j] = labelValue[i - 1][j - 1]
                        else:
                            if labelValue[i - 1][j - 1] != 0:
                                labelValue[i][j] = labelValue[i - 1][j - 1]
                            elif labelValue[i][j - 1] != 0:
                                labelValue[i][j] = labelValue[i][j - 1]
                            elif labelValue[i + 1][j - 1] != 0:
                                labelValue[i][j] = labelValue[i + 1][j - 1]
                            elif labelValue[i - 1][j] != 0:
                                labelValue[i][j] = labelValue[i - 1][j]

                            if [labelValue[i - 1][j], labelValue[i][j - 1]] not in list and [labelValue[i][j - 1],
                                                                                             labelValue[i - 1][
                                                                                                 j]] not in list:
                                list.append([labelValue[i - 1][j], labelValue[i][j - 1]])
                            if [labelValue[i - 1][j], labelValue[i - 1][j - 1]] not in list and [
                                labelValue[i - 1][j - 1], labelValue[i - 1][j]] not in list:
                                list.append([labelValue[i - 1][j], labelValue[i - 1][j - 1]])
                            if [labelValue[i - 1][j], labelValue[i + 1][j - 1]] not in list and [
                                labelValue[i + 1][j - 1], labelValue[i - 1][j]] not in list:
                                list.append([labelValue[i - 1][j], labelValue[i + 1][j - 1]])
                    elif pixelValue[i - 1][j] == 1 and pixelValue[i][j - 1] == 1 and pixelValue[i - 1][j - 1] == 1 and \
                            pixelValue[i + 1][j - 1] == 0:
                        if labelValue[i - 1][j] == labelValue[i][j - 1] and labelValue[i - 1][j] == labelValue[i - 1][
                            j - 1] and labelValue[i - 1][j] != 0:
                            labelValue[i][j] = labelValue[i][j - 1]
                        else:
                            if labelValue[i - 1][j - 1] != 0:
                                labelValue[i][j] = labelValue[i - 1][j - 1]
                            elif labelValue[i][j - 1] != 0:
                                labelValue[i][j] = labelValue[i][j - 1]
                            elif labelValue[i - 1][j] != 0:
                                labelValue[i][j] = labelValue[i - 1][j]
                            if [labelValue[i - 1][j], labelValue[i][j - 1]] not in list and [labelValue[i][j - 1],
                                                                                             labelValue[i - 1][
                                                                                                 j]] not in list:
                                list.append([labelValue[i - 1][j], labelValue[i][j - 1]])
                            if [labelValue[i - 1][j], labelValue[i - 1][j - 1]] not in list and [
                                labelValue[i - 1][j - 1], labelValue[i - 1][j]] not in list:
                                list.append([labelValue[i - 1][j], labelValue[i - 1][j - 1]])
                    elif pixelValue[i - 1][j] == 1 and pixelValue[i][j - 1] == 1 and pixelValue[i - 1][j - 1] == 0 and \
                            pixelValue[i + 1][j - 1] == 1:
                        if labelValue[i - 1][j] == labelValue[i][j - 1] and labelValue[i - 1][j] == labelValue[i + 1][
                            j - 1] and labelValue[i - 1][j] != 0:
                            labelValue[i][j] = labelValue[i][j - 1]
                        else:
                            if labelValue[i + 1][j - 1] != 0:
                                labelValue[i][j] = labelValue[i + 1][j - 1]
                            elif labelValue[i][j - 1] != 0:
                                labelValue[i][j] = labelValue[i][j - 1]
                            elif labelValue[i - 1][j] != 0:
                                labelValue[i][j] = labelValue[i - 1][j]
                            if [labelValue[i - 1][j], labelValue[i][j - 1]] not in list and [labelValue[i][j - 1],
                                                                                             labelValue[i - 1][
                                                                                                 j]] not in list:
                                list.append([labelValue[i - 1][j], labelValue[i][j - 1]])
                            if [labelValue[i - 1][j], labelValue[i + 1][j - 1]] not in list and [labelValue[i - 1][j],
                                                                                                 labelValue[i + 1][
                                                                                                     j - 1]] not in list:
                                list.append([labelValue[i - 1][j], labelValue[i + 1][j - 1]])

                    elif pixelValue[i - 1][j] == 1 and pixelValue[i][j - 1] == 0 and pixelValue[i - 1][j - 1] == 1 and \
                            pixelValue[i + 1][j - 1] == 1:
                        if labelValue[i - 1][j] == labelValue[i - 1][j - 1] and labelValue[i - 1][j] == \
                                labelValue[i + 1][j - 1] and labelValue[i - 1][j] != 0:
                            labelValue[i][j] = labelValue[i + 1][j - 1]
                        else:
                            if labelValue[i - 1][j - 1] != 0:
                                labelValue[i][j] = labelValue[i - 1][j - 1]
                            elif labelValue[i + 1][j - 1] != 0:
                                labelValue[i][j] = labelValue[i + 1][j - 1]
                            elif labelValue[i - 1][j] != 0:
                                labelValue[i][j] = labelValue[i - 1][j]
                            if [labelValue[i - 1][j], labelValue[i + 1][j - 1]] not in list and [
                                labelValue[i + 1][j - 1], labelValue[i - 1][j]] not in list:
                                list.append([labelValue[i - 1][j], labelValue[i + 1][j - 1]])
                            if [labelValue[i - 1][j], labelValue[i - 1][j - 1]] not in list and [
                                labelValue[i - 1][j - 1], labelValue[i - 1][j]] not in list:
                                list.append([labelValue[i - 1][j], labelValue[i - 1][j - 1]])
                    elif pixelValue[i - 1][j] == 0 and pixelValue[i][j - 1] == 1 and pixelValue[i - 1][j - 1] == 1 and \
                            pixelValue[i + 1][j - 1] == 1:
                        if labelValue[i][j - 1] == labelValue[i - 1][j - 1] and labelValue[i][j - 1] == \
                                labelValue[i + 1][j - 1] and labelValue[i][j - 1] != 0:
                            labelValue[i][j] = labelValue[i + 1][j - 1]
                        else:
                            if labelValue[i - 1][j - 1] != 0:
                                labelValue[i][j] = labelValue[i - 1][j - 1]
                            elif labelValue[i + 1][j - 1] != 0:
                                labelValue[i][j] = labelValue[i + 1][j - 1]
                            elif labelValue[i][j - 1] != 0:
                                labelValue[i][j] = labelValue[i][j - 1]
                            if [labelValue[i + 1][j - 1], labelValue[i][j - 1]] not in list and [labelValue[i][j - 1],
                                                                                                 labelValue[i + 1][
                                                                                                     j - 1]] not in list:
                                list.append([labelValue[i + 1][j - 1], labelValue[i][j - 1]])
                            if [labelValue[i - 1][j - 1], labelValue[i][j - 1]] not in list and [labelValue[i][j - 1],
                                                                                                 labelValue[i - 1][
                                                                                                     j - 1]] not in list:
                                list.append([labelValue[i - 1][j - 1], labelValue[i][j - 1]])
                    elif pixelValue[i - 1][j] == 1 and pixelValue[i][j - 1] == 1 and pixelValue[i - 1][j - 1] == 0 and \
                            pixelValue[i + 1][j - 1] == 0:
                        if labelValue[i][j - 1] == labelValue[i - 1][j] and labelValue[i][j - 1] != 0:
                            labelValue[i][j] = labelValue[i - 1][j]
                        else:
                            if labelValue[i - 1][j] != 0:
                                labelValue[i][j] = labelValue[i - 1][j]
                            elif labelValue[i][j - 1] != 0:
                                labelValue[i][j] = labelValue[i][j - 1]
                            if [labelValue[i - 1][j], labelValue[i][j - 1]] not in list and [labelValue[i][j - 1],
                                                                                             labelValue[i - 1][
                                                                                                 j]] not in list:
                                list.append([labelValue[i - 1][j], labelValue[i][j - 1]])

                    elif pixelValue[i - 1][j] == 1 and pixelValue[i][j - 1] == 0 and pixelValue[i - 1][j - 1] == 1 and \
                            pixelValue[i + 1][j - 1] == 0:
                        if labelValue[i - 1][j - 1] == labelValue[i - 1][j] and labelValue[i - 1][j - 1] != 0:
                            labelValue[i][j] = labelValue[i - 1][j]
                        else:
                            if labelValue[i - 1][j - 1] != 0:
                                labelValue[i][j] = labelValue[i - 1][j - 1]
                            elif labelValue[i - 1][j] != 0:
                                labelValue[i][j] = labelValue[i - 1][j]

                            if [labelValue[i - 1][j], labelValue[i - 1][j - 1]] not in list and [
                                labelValue[i - 1][j - 1], labelValue[i - 1][j]] not in list:
                                list.append([labelValue[i - 1][j], labelValue[i - 1][j - 1]])
                    elif pixelValue[i - 1][j] == 1 and pixelValue[i][j - 1] == 0 and pixelValue[i - 1][j - 1] == 0 and \
                            pixelValue[i + 1][j - 1] == 1:
                        if labelValue[i + 1][j - 1] == labelValue[i - 1][j] and labelValue[i - 1][j] != 0:
                            labelValue[i][j] = labelValue[i - 1][j]
                        else:
                            if labelValue[i + 1][j - 1] != 0:
                                labelValue[i][j] = labelValue[i + 1][j - 1]
                            elif labelValue[i - 1][j] != 0:
                                labelValue[i][j] = labelValue[i - 1][j]
                            if [labelValue[i - 1][j], labelValue[i][j - 1]] not in list and [labelValue[i][j - 1],
                                                                                             labelValue[i - 1][
                                                                                                 j]] not in list:
                                list.append([labelValue[i - 1][j], labelValue[i][j - 1]])
                    elif pixelValue[i - 1][j] == 0 and pixelValue[i][j - 1] == 1 and pixelValue[i - 1][j - 1] == 1 and \
                            pixelValue[i + 1][j - 1] == 0:
                        if labelValue[i][j - 1] == labelValue[i - 1][j - 1] and labelValue[i][j - 1] != 0:
                            labelValue[i][j] = labelValue[i][j - 1]
                        else:
                            if labelValue[i - 1][j - 1] != 0:
                                labelValue[i][j] = labelValue[i - 1][j - 1]
                            elif labelValue[i][j - 1] != 0:
                                labelValue[i][j] = labelValue[i][j - 1]
                            if [labelValue[i - 1][j - 1], labelValue[i][j - 1]] not in list and [labelValue[i][j - 1],
                                                                                                 labelValue[i - 1][
                                                                                                     j - 1]] not in list:
                                list.append([labelValue[i - 1][j - 1], labelValue[i][j - 1]])
                    elif pixelValue[i - 1][j] == 0 and pixelValue[i][j - 1] == 1 and pixelValue[i - 1][j - 1] == 0 and \
                            pixelValue[i + 1][j - 1] == 1:
                        if labelValue[i][j - 1] == labelValue[i + 1][j - 1] and labelValue[i][j - 1] != 0:
                            labelValue[i][j] = labelValue[i][j - 1]
                        else:
                            if labelValue[i + 1][j - 1] != 0:
                                labelValue[i][j] = labelValue[i + 1][j - 1]
                            elif labelValue[i][j - 1] != 0:
                                labelValue[i][j] = labelValue[i][j - 1]
                            if [labelValue[i + 1][j - 1], labelValue[i][j - 1]] not in list and [labelValue[i][j - 1],
                                                                                                 labelValue[i + 1][
                                                                                                     j - 1]] not in list:
                                list.append([labelValue[i + 1][j - 1], labelValue[i][j - 1]])


                    elif pixelValue[i - 1][j] == 0 and pixelValue[i][j - 1] == 0 and pixelValue[i - 1][j - 1] == 1 and \
                            pixelValue[i + 1][j - 1] == 1:
                        if labelValue[i - 1][j - 1] == labelValue[i + 1][j - 1] and labelValue[i - 1][j - 1] != 0:
                            labelValue[i][j] = labelValue[i - 1][j - 1]
                        else:
                            if labelValue[i - 1][j - 1] != 0:
                                labelValue[i][j] = labelValue[i - 1][j - 1]
                            elif labelValue[i + 1][j - 1] != 0:
                                labelValue[i][j] = labelValue[i + 1][j - 1]
                            if [labelValue[i + 1][j - 1], labelValue[i - 1][j - 1]] not in list and [
                                labelValue[i - 1][j - 1], labelValue[i + 1][j - 1]] not in list:
                                list.append([labelValue[i - 1][j - 1], labelValue[i + 1][j - 1]])

                    elif pixelValue[i - 1][j] == 0 and pixelValue[i][j - 1] == 0 and pixelValue[i - 1][j - 1] == 0 and \
                            pixelValue[i + 1][j - 1] == 1 and labelValue[i + 1][j - 1] != 0:
                        labelValue[i][j] = labelValue[i + 1][j - 1]
                    elif pixelValue[i - 1][j] == 0 and pixelValue[i][j - 1] == 0 and pixelValue[i - 1][j - 1] == 1 and \
                            pixelValue[i + 1][j - 1] == 0 and labelValue[i - 1][j - 1] != 0:
                        labelValue[i][j] = labelValue[i - 1][j - 1]
                    elif pixelValue[i - 1][j] == 0 and pixelValue[i][j - 1] == 1 and pixelValue[i - 1][j - 1] == 0 and \
                            pixelValue[i + 1][j - 1] == 0 and labelValue[i][j - 1] != 0:
                        labelValue[i][j] = labelValue[i][j - 1]
                    elif pixelValue[i - 1][j] == 1 and pixelValue[i][j - 1] == 0 and pixelValue[i - 1][j - 1] == 0 and \
                            pixelValue[i + 1][j - 1] == 0 and labelValue[i - 1][j] != 0:
                        labelValue[i][j] = labelValue[i - 1][j]
                    else:
                        labelValue[i][j] = labelCounter
                        labelCounter += 1

                else:  ##current is white but neighbors are black
                    labelValue[i][j] = labelCounter
                    labelCounter += 1
            else:
                labelValue[i][j] = 1  # means blacks labels is one


    # Call that clearLabel function for neighbour pixels with diffrent label values


    clearLabel(list)

    #Call addToScreen for display image on screen

    addToScreen(drawingImage)

# That function change the colors between each other randomly

def shuffle():
    for s in range (len(undolist)):
        h = randint(0,len(undolist)-1)

        m, n, p, r = undolist[s]
        m2, n2, p2, r2 = undolist[h]

        for j in range(1, ySize - 1):
            for i in range(1, xSize - 1):
                if labelValue[i][j] == labelValue[m][n]:
                    pix[i, j] = r2
                    drawingImage.putpixel((m, n), r2)

        render = ImageTk.PhotoImage(drawingImage)
        img = Label(root, image=render)
        img.image = render
        img.place(x=a, y=c)
        img.bind("<Button-1>", paintcoords)


#Function for make a dynamic 'for' loop for list

def getmax(list):
    max = 0
    for i in range(len(list)):
        [x, y] = list[i]
        if x > max:
            max = x
        if y > max:
            max = y
    return max

# Make equal neighbours with different label values

def clearLabel(list):
    for z in range(len(list)):
        if [0, z] in list:
            list.remove([0, z])
        if [z, 0] in list:
            list.remove([z, 0])
        if [1, z] in list:
            list.remove([1, z])
        if [z, 1] in list:
            list.remove([z, 1])
        if [z, z] in list:
            list.remove([z, z])

    for a in range(len(list)):
        [x, y] = list[a]

        for b in range(a + 1, len(list)):
            [m, n] = list[b]
            if y == n:
                list[b] = [m, x]
            if y == m:
                list[b] = [x, n]
    for j in range(ySize - 1):
        for i in range(xSize - 1):

            for k in range(len(list)):
                [t, p] = list[k]
                if labelValue[i][j] == p:
                    labelValue[i][j] = t

    return list


# Undo changes on image

def undo():
    global counter
    if counter !=0:
        counter = counter-1

        m,n,p,r  = undolist[counter]

        for j in range(1, ySize - 1):
            for i in range(1, xSize - 1):
                if labelValue[i][j] == labelValue[m][n]:
                    pix[i, j] = p
                    drawingImage.putpixel((m, n), p)

        render = ImageTk.PhotoImage(drawingImage)
        img = Label(root, image=render)
        img.image = render
        img.place(x=a, y=c)
        img.bind("<Button-1>", paintcoords)

    else:
        m, n, p, r = undolist[0]

        for j in range(1, ySize - 1):
            for i in range(1, xSize - 1):
                if labelValue[i][j] == labelValue[m][n]:
                    pix[i, j] = p
                    drawingImage.putpixel((m, n), p)

        render = ImageTk.PhotoImage(drawingImage)
        img = Label(root, image=render)
        img.image = render
        img.place(x=a, y=c)
        img.bind("<Button-1>", paintcoords)

#Redo changes in image

def redo():
    global counter
    if counter < len(undolist):
        counter = counter + 1

        m, n, p, r = undolist[counter-1]

        for j in range(1, ySize - 1):
            for i in range(1, xSize - 1):
                if labelValue[i][j] == labelValue[m][n]:
                    pix[i, j] = r
                    drawingImage.putpixel((m, n), r)


        render = ImageTk.PhotoImage(drawingImage)
        img = Label(root, image=render)
        img.image = render
        img.place(x=a, y=c)
        img.bind("<Button-1>", paintcoords)
    else:
        m, n, p, r = undolist[len(undolist)-1]

        for j in range(1, ySize - 1):
            for i in range(1, xSize - 1):
                if labelValue[i][j] == labelValue[m][n]:
                    pix[i, j] = r
                    drawingImage.putpixel((m, n), r)

        render = ImageTk.PhotoImage(drawingImage)
        img = Label(root, image=render)
        img.image = render
        img.place(x=a, y=c)
        img.bind("<Button-1>", paintcoords)

# Display choosen image file to screen

def addToScreen(drawingImage):

    render = ImageTk.PhotoImage(drawingImage)
    img = Label(root, image=render)
    img.image = render
    global a
    global c
    a = int((width - xSize) / 2)
    c = int((height - ySize) / 2)
    img.place(x=a, y=c)
    img.bind("<Button-1>", paintcoords)


# A transition function for colorpicker

def learncolor():


    render = ImageTk.PhotoImage(drawingImage)
    img = Label(root, image=render)
    img.image = render
    img.place(x=a, y=c)
    img.bind("<Button-1>", learncoords)


# Get current color from colorpicker

def learncoords(event):
    global choosenColor
    choosenColor = pix[event.x,event.y]
    addToScreen(drawingImage)

# A transition function for paintRegion function

def paintcoords(event):
    paintRegion(event.x, event.y)

# Paint the image using choosen color

def paintRegion(x, y):
    global choosenColor
    global xSize
    global ySize
    global counter
    global undolist

    counter = counter+1

    undolist.append([x, y, pix[x, y],choosenColor])


    for j in range(1, ySize - 1):
        for i in range(1, xSize - 1):
            if labelValue[i][j] == labelValue[x][y]:
                pix[i, j] = choosenColor
                drawingImage.putpixel((x, y), choosenColor)



    render = ImageTk.PhotoImage(drawingImage)
    img = Label(root, image=render)
    img.image = render
    img.place(x=a, y=c)
    img.bind("<Button-1>", paintcoords)


# Function for specify lines

def convertbinary(rgbValues):
    if len(rgbValues) == 4:
        r, g, b, f = rgbValues
    else:
        r, g, b = rgbValues
    average = (r + g + b) / 3
    if average == 255:
        return 1  # means white
    return 0  # means black

# Function for make lines much more cleaner

def clean(rgbvalues):
    # some pictures has another information that's the blur affect r,g,b,and F
    # but we are interested in only R,G,B values to clean noise

    if (type(rgbvalues)) == int:
       r =rgbvalues
       g = rgbvalues
       b = rgbvalues
       l=[r,g,b]

       return tuple(l)
    else:
        if len(rgbvalues) == 4:
            r, g, b, f = rgbvalues

        else:
            r, g, b = rgbvalues
        average = (r + g + b) / 3
        if average > 200:
            return 255, 255, 255
        else:
            return 0, 0, 0


# All lambda functions below are for easy color choosing in gui

lambda: makegreen()


def makegreen():
    global choosenColor
    choosenColor = (0, 255, 0)
    return choosenColor


lambda: makeblue()


def makeblue():
    global choosenColor
    choosenColor = (0, 0, 255)
    return choosenColor


lambda: makered()


def makered():
    global choosenColor
    choosenColor = (255, 0, 0)
    return choosenColor


lambda: makeyellow()


def makeyellow():
    global choosenColor
    choosenColor = (230, 218, 0)
    return choosenColor


lambda: makepurple()


def makepurple():
    global choosenColor
    choosenColor = (166, 55, 167)
    return choosenColor


lambda: makeorange()


def makeorange():
    global choosenColor
    choosenColor = (255, 127, 39)
    return choosenColor


lambda: makepink()


def makepink():
    global choosenColor
    choosenColor = (255, 174, 200)
    return choosenColor


lambda: makecyan()


def makecyan():
    global choosenColor
    choosenColor = (140, 255, 251)
    return choosenColor


lambda: makeblack()


def makeblack():
    global choosenColor
    choosenColor = (0, 0, 0)
    return choosenColor


lambda: makewhite()


def makewhite():
    global choosenColor
    choosenColor = (255, 255, 255)
    return choosenColor


lambda: makelightgrey()


def makelightgrey():
    global choosenColor
    choosenColor = (195, 195, 195)
    return choosenColor


lambda: makedarkgrey()


def makedarkgrey():
    global choosenColor
    choosenColor = (88, 88, 88)
    return choosenColor


lambda: makedarkred()


def makedarkred():
    global choosenColor
    choosenColor = (136, 0, 27)
    return choosenColor


lambda: makegold()


def makegold():
    global choosenColor
    choosenColor = (255, 202, 24)
    return choosenColor


lambda: makeblue()


def makeblue():
    global choosenColor
    choosenColor = (0, 0, 255)
    return choosenColor


lambda: makelightyellow()


def makelightyellow():
    global choosenColor
    choosenColor = (253, 236, 166)
    return choosenColor


lambda: makedarkgreen()


def makedarkgreen():
    global choosenColor
    choosenColor = (60, 78, 10)
    return choosenColor


lambda: maketurquoise()


def maketurquoise():
    global choosenColor
    choosenColor = (0, 168, 243)
    return choosenColor


lambda: makebrown()


def makebrown():
    global choosenColor
    choosenColor = (185, 122, 86)
    return choosenColor

if __name__ == '__main__':
    main()
