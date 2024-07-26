import random
import sys
import tkinter as tk
from tkinter import StringVar
from tkinter import ttk
#Sets the a 2D Array with 0s
table=[[0]*4 for i in range (4)]
def startGame():
    addTwo(2)
    addTwo(2)
    printGame()
#prints 2D array
def printGame():
    gameOver=False
    for i in range(4):
        for j in table[i]:
            if j==2048:
                gameOver=True
    #ends Game if 2048 is reached
    if gameOver:
        sys.exit()
#takes an array and returns an array of the same numbers in the same order with 0s removed
def removeZero(row):
    newr=[]
    for i in row:
        if(not i==0):
            newr.append(i)
    return newr
#Adds the number 2 to a random empty(0) space. Ends the game if no tiles available
def addTwo(root):
    possible=[]
    #Makes an array of Tuples representing the index cordinates for all empty(0) spaces
    for i in range(4):
        for j in range(4):
            if (table[i][j]==0):
                possible.append(tuple([i,j]))
    #if there are no empty spaces end game
    if not possible:
        printGame()
        root.destroy()
        sys.exit()
    #Selects a random choice thats possible
    toadd=random.choice(possible)
    table[toadd[0]][toadd[1]]=2
#returns chosen coulmn as a 1d array
def getColumn(z):
    column=[]
    for i in range(4):
        column.append(table[i][z])
    return column
#return chosen column inverted as a 1d array
def getInvertColumn(z):
    column=[]
    for i in range(3,-1,-1):
        column.append(table[i][z])
    return column
    
#merges numbers moving to the left.
def mergeLeft():
    #Reperesents which row is being merged
    counter=0
    #loops through each row one at a time
    for row in table:
        #proxy array to set the root row
        newrow=[]
        #represemts row after merge without 0s
        mergedrow=[]
        #gets a new array representing the row withouut 0s
        tomerge = removeZero(row)
        #how many numbers to merge
        length=len(tomerge)
        #unable to attempt merge if there are not more then 1 numbers
        if length==1:
            #sets the single number to the left filled the rest row with 0s
            for x in range(4):
                if x==0:
                    newrow.append(tomerge[0])
                else:
                    newrow.append(0)
        #if the is not 1 or0 numbers to merge. merge the numbers, leaving unmerged numbers in the array left 
        elif not length==0:
            #loops through array checking one space to the right to potentailly merge
            for i in range(length):
                
                #if the number is the same, merge the two, and set the merged number to 0 so it doesnt merge again
                if (i<length-1 and tomerge[i]==tomerge[i+1]):
                    mergedrow.append(tomerge[i]+tomerge[i])
                    tomerge[i+1]=0
                #if there is not a simillar number to merge, add to array as is
                else:
                    mergedrow.append(tomerge[i])
        #fills the newrow with the mergedrow without 0s
        for x in range(4):
            if x<len(mergedrow) and mergedrow[x]:
                newrow.append(mergedrow[x])
        numofzero=4-len(newrow)
        #adds 0s to fill the row to length 4
        for i in range(0,numofzero):
            newrow.append(0)
        #sets the root to row to the new row
        for i in range(4):
            table[counter][i]=newrow[i]
        counter+=1
def mergeRight():
    #Reperesents which row is being merged
    counter=0
    #loops through each row one at a time
    for row in table:
        #proxy array to set the root row
        newrow=[]
        #represemts row after merge without 0s
        mergedrow=[]
        #invert row to simulate merge left, then invert again to go back to right
        invertrow=[]
        #invert row
        for i in range (3,-1,-1):
            invertrow.append(row[i])
        #gets a new array representing the row withouut 0s
        tomerge = removeZero(invertrow)
        #how many numbers to merge
        length=len(tomerge)
        #unable to attempt merge if there are not more then 1 nuumbers
        if length==1:
            #sets the single number to the left filled the rest row with 0s
            for x in range(4):
                if x==0:
                    newrow.append(tomerge[0])
                else:
                    newrow.append(0)
        #if the is not 1 or 0 numbers to merge. merge the numbers, leaving unmerged numbers in the array left 
        elif not length==0:
            #loops through array checking one space to the right to potentailly merge
            for i in range(length):
                
                #if the number is the same, merge the two, and set the merged number to 0 so it doesnt merge again
                if (i<length-1 and tomerge[i]==tomerge[i+1]):
                    mergedrow.append(tomerge[i]+tomerge[i])
                    tomerge[i+1]=0
                #if there is not a simillar number to merge, add to array as is
                else:
                    mergedrow.append(tomerge[i])
        #fills the newrow with the mergedrow without 0s
        for x in range(4):
            if x<len(mergedrow) and mergedrow[x]:
                newrow.append(mergedrow[x])
        numofzero=4-len(newrow)
        #adds 0s to fill the row to length 4
        for i in range(0,numofzero):
            newrow.append(0)
        #sets the root to row to the new row but inverted back to the right
        for i in range(4):
            table[counter][i]=newrow[3-i]
        counter+=1
#creates column, makes it a 1d array and merges like mergeUP, then is roated when entered into the table
def mergeUp():
    #Reperesents which column is being merged
    counter=0
    #loops through each row one at a time
    for z in range(4):
        column = getColumn(z)
        #proxy array to set the root column
        newcolumn=[]
        #represemts row after merge without 0s
        mergedcolumn=[]
        #gets a new array representing the column without 0s
        tomerge = removeZero(column)
        #how many numbers to merge
        length=len(tomerge)
        #unable to attempt merge if there are not more then 1 nuumbers
        if length==1:
            #sets the single number to the left filled the rest row with 0s
            for x in range(4):
                if x==0:
                    newcolumn.append(tomerge[0])
                else:
                    newcolumn.append(0)
        #if the is not 1 or0 numbers to merge. merge the numbers, leaving unmerged numbers in the array left 
        elif not length==0:
            #loops through array checking one space to the right to potentailly merge
            for i in range(length):
                
                #if the number is the same, merge the two, and set the merged number to 0 so it doesnt merge again
                if (i<length-1 and tomerge[i]==tomerge[i+1]):
                    mergedcolumn.append(tomerge[i]+tomerge[i])
                    tomerge[i+1]=0
                #if there is not a simillar number to merge, add to array as is
                else:
                    mergedcolumn.append(tomerge[i])
        #fills the newrow with the mergedrow without 0s
        for x in range(4):
            if x<len(mergedcolumn) and mergedcolumn[x]:
                newcolumn.append(mergedcolumn[x])
        numofzero=4-len(newcolumn)
        #adds 0s to fill the row to length 4
        for i in range(0,numofzero):
            newcolumn.append(0)
        #sets the root to row to the new row
        for i in range(4):
            table[i][z]=newcolumn[i]
        counter+=1
#ruuns like merge up but the row is inverted simulating merge up, then is then inverted again when placed back in the table
def mergeDown():
    #Reperesents which column is being merged
    counter=0
    #loops through each row one at a time
    for z in range(4):
        column = getInvertColumn(z)
        #proxy array to set the root column
        newcolumn=[]
        #represemts row after merge without 0s
        mergedcolumn=[]
        #gets a new array representing the row withouut 0s
        tomerge = removeZero(column)
        #how many numbers to merge
        length=len(tomerge)
        #unable to attempt merge if there are not more then 1 nuumbers
        if length==1:
            #sets the single number to the left filled the rest row with 0s
            for x in range(4):
                if x==0:
                    newcolumn.append(tomerge[0])
                else:
                    newcolumn.append(0)
        #if the is not 1 or0 numbers to merge. merge the numbers, leaving unmerged numbers in the array left 
        elif not length==0:
            #loops through array checking one space to the right to potentailly merge
            for i in range(length):
                
                #if the number is the same, merge the two, and set the merged number to 0 so it doesnt merge again
                if (i<length-1 and tomerge[i]==tomerge[i+1]):
                    mergedcolumn.append(tomerge[i]+tomerge[i])
                    tomerge[i+1]=0
                #if there is not a simillar number to merge, add to array as is
                else:
                    mergedcolumn.append(tomerge[i])
        #fills the newrow with the mergedrow without 0s
        for x in range(4):
            if x<len(mergedcolumn) and mergedcolumn[x]:
                newcolumn.append(mergedcolumn[x])
        numofzero=4-len(newcolumn)
        #adds 0s to fill the row to length 4
        for i in range(0,numofzero):
            newcolumn.append(0)
        #sets the root to row to the new row
        for i in range(3,-1,-1):
            table[3-i][z]=newcolumn[i]
        counter+=1
#sets up the GUI
def setGui():
    #configures window
    root= tk.Tk()
    root.title("2048")
    root.geometry("800x1000")
    root.columnconfigure(0,weight = 1)
    root.columnconfigure(1,weight = 1)
    root.columnconfigure(2,weight = 1)
    root.columnconfigure(3,weight = 1)
    root.rowconfigure(0,weight = 1)
    root.rowconfigure(1,weight = 1)
    root.rowconfigure(2,weight = 1)
    root.rowconfigure(3,weight = 1)
    root.rowconfigure(4,weight = 1)  
    
    #sets changeable labels 
    lbl00txt = StringVar()
    lbl01txt = StringVar()
    lbl02txt = StringVar()
    lbl03txt = StringVar()
    lbl10txt = StringVar()
    lbl11txt = StringVar()
    lbl12txt = StringVar()
    lbl13txt = StringVar()
    lbl20txt = StringVar()
    lbl21txt = StringVar()
    lbl22txt = StringVar()
    lbl23txt = StringVar()
    lbl30txt = StringVar()
    lbl31txt = StringVar()
    lbl32txt = StringVar()
    lbl33txt = StringVar()
    
    #make 2d array to send to setLabels
    labels=[[lbl00txt,lbl01txt,lbl02txt,lbl03txt],[lbl10txt,lbl11txt,lbl12txt,lbl13txt],[lbl20txt,lbl21txt,lbl22txt,lbl23txt],[lbl30txt,lbl31txt,lbl32txt,lbl33txt]]
    #update the Gui to show the new table state
    setLabels(labels)
    
    #add labels to window
    lbl00=ttk.Label(root, textvariable = lbl00txt, background="red",font ="Impact 25")
    lbl00.configure(anchor="center")
    lbl00.grid(row=0,column=0, sticky='nsew')
    lbl01=ttk.Label(root, textvariable = lbl01txt, background="red",font ="Impact 25")
    lbl01.configure(anchor="center")
    lbl01.grid(row=0, column=1, sticky='nsew')
    lbl02=ttk.Label(root,textvariable = lbl02txt, background="red",font ="Impact 25")
    lbl02.configure(anchor="center")
    lbl02.grid(row=0, column=2, sticky='nsew')
    lbl03=ttk.Label(root, textvariable = lbl03txt, background="red",font ="Impact 25")
    lbl03.configure(anchor="center")
    lbl03.grid(row=0, column=3, sticky='nsew')
    lbl10=ttk.Label(root, textvariable = lbl10txt, background="red",font ="Impact 25")
    lbl10.configure(anchor="center")
    lbl10.grid(row=1, column=0, sticky='nsew')
    lbl11=ttk.Label(root, textvariable = lbl11txt, background="red",font ="Impact 25")
    lbl11.configure(anchor="center")
    lbl11.grid(row=1, column=1, sticky='nsew')
    lbl12=ttk.Label(root, textvariable = lbl12txt, background="red",font ="Impact 25")
    lbl12.configure(anchor="center")
    lbl12.grid(row=1, column=2, sticky='nsew')
    lbl13=ttk.Label(root, textvariable = lbl13txt, background="red",font ="Impact 25")
    lbl13.configure(anchor="center")
    lbl13.grid(row=1, column=3, sticky='nsew')
    lbl20=ttk.Label(root, textvariable = lbl20txt, background="red",font ="Impact 25")
    lbl20.configure(anchor="center")
    lbl20.grid(row=2, column=0, sticky='nsew')
    lbl21=ttk.Label(root, textvariable = lbl21txt, background="red",font ="Impact 25")
    lbl21.configure(anchor="center")
    lbl21.grid(row=2, column=1, sticky='nsew')
    lbl22=ttk.Label(root, textvariable = lbl22txt, background="red",font ="Impact 25")
    lbl22.configure(anchor="center")
    lbl22.grid(row=2, column=2, sticky='nsew')
    lbl23=ttk.Label(root, textvariable = lbl23txt, background="red",font ="Impact 25")
    lbl23.configure(anchor="center")
    lbl23.grid(row=2, column=3, sticky='nsew')
    lbl30=ttk.Label(root, textvariable = lbl30txt, background="red",font ="Impact 25")
    lbl30.configure(anchor="center")
    lbl30.grid(row=3, column=0, sticky='nsew')
    lbl31=ttk.Label(root, textvariable = lbl31txt, background="red",font ="Impact 25")
    lbl31.configure(anchor="center")
    lbl31.grid(row=3, column=1, sticky='nsew')
    lbl32=ttk.Label(root, textvariable = lbl32txt, background="red",font ="Impact 25")
    lbl32.configure(anchor="center")
    lbl32.grid(row=3, column=2, sticky='nsew')
    lbl33=ttk.Label(root, textvariable = lbl33txt, background="red",font ="Impact 25")
    lbl33.configure(anchor="center")
    lbl33.grid(row=3, column=3, sticky='nsew')
    
    #set input buttons
    buttonLeft= ttk.Button(root, text= "Left", command= lambda: [mergeLeft(),addTwo(root),setLabels(labels)])
    buttonLeft.grid(row=4, column=0,sticky='nswe')
    buttonRight= ttk.Button(root, text= "Right", command= lambda: [mergeRight(),addTwo(root),setLabels(labels)])
    buttonRight.grid(row=4, column=1,sticky='nswe')
    buttonUp= ttk.Button(root, text= "Up", command= lambda: [mergeUp(),addTwo(root),setLabels(labels)])
    buttonUp.grid(row=4, column=2,sticky='nswe')
    buttonDown= ttk.Button(root, text= "Down", command= lambda: [mergeDown(),addTwo(root),setLabels(labels)])
    buttonDown.grid(row=4, column=3,sticky='nswe')
    
    #start gui
    root.mainloop()
#update the variable label text to reflect current table state
def setLabels(labels):
    for i in range(4):
        for j in range(4):
            labels[i][j].set(table[i][j])
#run the game
startGame()
setGui()