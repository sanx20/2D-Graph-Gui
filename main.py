from matplotlib import pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk

# funtion to collect points entered by user for x and y point
xValues,yValues=[],[]                # creating empty lists for values
def addPoint():
    
    action_label.config(text='Changing graph will reset everything')
    
    if (radioVar.get() == 3):             # this case is for pie chart
        x = x_point.get()                # accessing single slice value  
        y = y_point.get()
        if len(x) != 0:                    # if entered str length is not 0 adding it to list
            xValues.append(eval(x))        # appending value to the list
        if len(y) != 0:                    # same for y (y contains labels for x values)
            yValues.append(y)
        tree.insert("", END, values=[x,y])                           # insertig values in tree
        t = 'Added  (' + x_point.get() + ',' + y_point.get() + ')'   
        action_label.configure(text=t)                               # showing added values in action label box
    
    else:                                # for rest of the graph
        x = x_point.get()                # accessing single value
        y = y_point.get()                # in this comma seprated values will come
        if len(x) != 0:                    # if entered str length is not 0 adding it to list
           xValues.append(eval(x))
        if len(y) != 0:
            cut = y.split(',')           # spliting y values and making list of them using split function
            count = 0
            for value in di.values():     # check ok() function below
                value.append(int(cut[count]))  # appending diff value into diff list with indexing
                count += 1                # increasing count value
            tree.insert("", END, values=[x,y])     # insertig values in tree
            t = 'Added  (' + x_point.get() + ',' + y_point.get() + ')'
            action_label.configure(text=t)          # showing added values in action label box



# selecting charts 
def selectingGraph():                                                 # radio buttons
    if (radioVar.get() == 0):                                         # line chart
        action_label.config(text='Changed to Line chart',width=450)   # changing text of action label
        x_point_label.config(text='X Point: ')                        # changing text of x point label
        y_point_label.config(text='Y Point: ')                        # changing text of y point label
        Npoint.config(state=NORMAL)                                   #changing state of labels 
        x_point.config(state=DISABLED)
        y_point.config(state=DISABLED)
        reset()
    
    elif (radioVar.get() == 1):                                       # bar graph 
        action_label.config(text='Changed to Bar Graph',width=450)    # same as above
        x_point_label.config(text='X Point: ')
        y_point_label.config(text='Y Point: ')
        Npoint.config(state=NORMAL)
        x_point.config(state=DISABLED)
        y_point.config(state=DISABLED)
        reset()

    elif (radioVar.get() == 2):                                                # horizontal bar graph
        action_label.config(text='Changed to Horizontal Bar Graph',width=450)
        x_point_label.config(text='X Point: ')    
        y_point_label.config(text='Y Point: ')
        Npoint.config(state=NORMAL)
        x_point.config(state=DISABLED)
        y_point.config(state=DISABLED)
        reset()

    elif (radioVar.get() == 3):                                         # pie chart
        action_label.config(text='Changed to Pie chart',width=450)
        x_point_label.config(text='Slice',width=6)
        y_point_label.config(text='Labels',width=6)
        Npoint.config(state=DISABLED)
        x_point.config(state=NORMAL)
        y_point.config(state=NORMAL)
        reset()

def createGraph():
    if graph_title.get() == '':
        action_label.configure(text='Graph tittle can\'t be empty')
    else:
        if (radioVar.get() == 0):                          # line chart
            xLabelValue = x_axis.get()                     # accesing values
            yLabelValue = y_axis.get()
            graphTitle = graph_title.get()
            plt.style.use('fivethirtyeight') 

            plt.xlabel(xLabelValue)
            plt.ylabel(yLabelValue)
            plt.title(graphTitle)
            for value in di.values():                                       # it will get each list in dictionary
                plt.plot(xValues, value, linewidth = 1.5, marker='.')       # and plot its value (x remains same)
            plt.tight_layout()
            plt.show()
    
    
        elif (radioVar.get() == 1):                   # bar graph
            xLabelValue = x_axis.get()                # same logic as above
            yLabelValue = y_axis.get()
            graphTitle = graph_title.get()
            plt.style.use('fivethirtyeight') 
        
            plt.xlabel(xLabelValue)
            plt.ylabel(yLabelValue)
            plt.title(graphTitle)
            width = 0.50

            if int(Npoint.get()) ==2:
                width = 0.35

            if int(Npoint.get()) ==3:
                width = 0.25

            if int(Npoint.get()) ==4:
                width = 0.18

            space = 0
            x_indexs = np.arange(len(xValues))
            for value in di.values():
                plt.bar(x_indexs + space, value,width)
                space += width
            plt.xticks(ticks=x_indexs + space/2, labels=xValues)
            plt.legend()
            plt.tight_layout()
            plt.show()
    
    
        elif (radioVar.get() == 2):                        # horizontal bar graph
            xLabelValue = x_axis.get()                     # same as above
            yLabelValue = y_axis.get()
            graphTitle = graph_title.get()
            plt.style.use('fivethirtyeight') 

            plt.xlabel(xLabelValue)
            plt.ylabel(yLabelValue)
            plt.title(graphTitle)
            width = 0.50

            if int(Npoint.get()) ==2:
                width = 0.35

            if int(Npoint.get()) ==3:
                width = 0.25

            if int(Npoint.get()) ==4:
                width = 0.18

            space = 0
            x_indexs = np.arange(len(xValues))
            for value in di.values():
                plt.barh(x_indexs + space,value,width)
                space+=width
            plt.xticks(ticks=x_indexs + space/2, labels=xValues)
            plt.tight_layout()
            plt.show()
    
        elif (radioVar.get() == 3):                             # pie
            xLabelValue = x_axis.get()
            yLabelValue = y_axis.get()
            graphTitle = graph_title.get()
            plt.style.use('fivethirtyeight') 

            plt.xlabel(xLabelValue)
            plt.ylabel(yLabelValue)
            plt.title(graphTitle)
            plt.pie(xValues,labels=yValues,wedgeprops={'edgecolor':'black'})
            plt.tight_layout()
            plt.show()
        di.clear()
        reset()


def reset():
    xValues.clear()             # clearing entire vlaues of list
    yValues.clear()
    y_axis.delete(0,END)        # deleting labels
    x_axis.delete(0,END)
    graph_title.delete(0,END)
    tree.delete(*tree.get_children())       # deleting all the tree values
    if (radioVar.get() == 3):               # pie 
        x_point.config(state=NORMAL)        # changing states
        y_point.config(state=NORMAL)
        Npoint.config(state=DISABLED)
    else:
        x_point.config(state=DISABLED)
        y_point.config(state=DISABLED)
        Npoint.config(state=NORMAL)

def ok():
    action_label.configure(text='change graph to add diff value')        # changing action label text
    global di 
    di = {}
    if (radioVar.get() == 1 or radioVar.get() == 2):
        if int(Npoint.get()) <=4 :
            Npoint.configure(state=DISABLED)                                     # disabling label after getting the value
            x_point.config(state=NORMAL)                                      # setting to noraml label after getting the value
            y_point.config(state=NORMAL)                                      # setting to normal label after getting the value
            for i in range(int(Npoint.get())):                                   # it will for number of n point user enterd 
                di['yLst'+str(i)] = list()                                       # and create that much new list 
        else:
            action_label.configure(text='Max limit for y Points is 4')
    else:
        Npoint.configure(state=DISABLED)                                     # disabling label after getting the value
        x_point.config(state=NORMAL)                                         # setting to noraml label after getting the value
        y_point.config(state=NORMAL)                                    # setting to normal label after getting the value
        for i in range(int(Npoint.get())):                                   # it will for number of n point user enterd 
            di['yLst'+str(i)] = list()
#gui from here
window = Tk()
window.maxsize(1000,650)
window.minsize(1000,650)
window.title("Graph")

action_label = Label(window,text='Enter Values for plotting desired graph',font=('Comic Sans',18),fg='#164A41', bg='#9DC88D',relief=RAISED, bd=3,justify='center')
action_label.place(x=490, y=20, width=450)

graph_title_label = Label(window,text='Graph title: ',font=('Comic Sans',15),fg='white', bg='#4D774E',relief=RAISED, bd=3)
graph_title_label.place(x=20,y=20)
graph_title = Entry(window,font=('Comic Sans',15),bg='#9DC88D')
graph_title.place(x=140,y=20,width=300)

x_axis_label = Label(window,text='X-Axis Label: ',font=("Comic Sans",15),fg='white', bg='#4D774E',relief=RAISED, bd=3)
x_axis_label.place(x=20,y=72)
x_axis = Entry(window,font=('Comic Sans',15),fg='#164A41',bg='#9DC88D')              
x_axis.place(x=160,y=73,width=300)

y_axis_label = Label(window,text='Y-Axis Label: ',font=("Comic Sans",15),fg='white', bg='#4D774E',relief=RAISED, bd=3)
y_axis_label.place(x=500,y=72)
y_axis = Entry(window,font=('Comic Sans',15),fg='#164A41',bg='#9DC88D')              
y_axis.place(x=640,y=73,width=300)

x_point_label = Label(window,text='X Point: ',font=('Comic Sans',18),fg='white', bg='#4D774E',relief=RAISED, bd=3)
x_point_label.place(x=20,y=132)
x_point = Entry(window,font=('Comic Sans',18),fg='#164A41',bg='#9DC88D',width=10,state=DISABLED)     #this will provide x axis values one at a time
x_point.place(x=125,y=133)

y_point_label = Label(window,text='Y Point: ',font=('Comic Sans',18),fg='white', bg='#4D774E',relief=RAISED, bd=3)
y_point_label.place(x=300,y=132)
y_point = Entry(window,font=('Comic Sans',18),fg='#164A41',bg='#9DC88D',width=10,state=DISABLED)      #this will provide y axis values one at a time
y_point.place(x=405,y=133)

#for bar
Npointlabel = Label(window,text='No. of Points: ',font=('Comic Sans',18),fg='white', bg='#4D774E',relief=RAISED, bd=3)
Npointlabel.place(x=580,y=132)
Npoint = Entry(window,font=('Comic Sans',18),fg='#164A41',bg='#9DC88D',width=10)      #this will provide y axis values one at a time
Npoint.place(x=750,y=133)

ok_button = Button(window,text='ok',font=('Comic Sans',13),relief=RAISED, bd=5,bg='#F1B24A',command = ok)
ok_button.place(x=895,y=133)

add_button = Button(window,text='Add',font=('bold',15),width=10,relief=RAISED, bd=5,bg='#F1B24A',command = addPoint)
add_button.place(x=600,y=200)                                          

#tree view
tree = ttk.Treeview(window, columns=('1','2'),  show='headings', height=18)
tree.column('#1', anchor=CENTER, width=250, )
tree.heading("#1", text='X')

tree.column('#2', anchor=CENTER, width=250)
tree.heading("#2", text='Y')
tree.place(x=60,y=200)

vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
vsb.place(x=550, y=200, height=390)

tree.configure(yscrollcommand=vsb.set)

style = ttk.Style(window)
style.theme_use("clam")
style.configure("Treeview", background="#9DC88D", fieldbackground="#9DC88D")


create_graph_button = Button(window,text="Create Graph",font=('bold',18),relief=RAISED, bd=5,bg='#F1B24A',command=createGraph)
create_graph_button.place(x=600,y=580)

reset_button = Button(window,text="Reset",font=('bold',18),width=9,relief=RAISED, bd=5,bg='#F1B24A',command=reset)
reset_button.place(x=800,y=580)




#radio buttons for different graph
global radioVar
radioVar = IntVar()
val = 0
graphs = ['Line','Bar','Horizontal Bar','Pie Chart']
for index in range(len(graphs)):
    radiobutton = Radiobutton(window, text=graphs[index], variable=radioVar, value=index, font=('Comic Sans',18),width=12,indicatoron=0,fg='#164A41',bg='#F1B24A',relief=RAISED, bd=5,command=selectingGraph)
    radiobutton.place(x=650,y=280+val)
    val+=55



window.config(background='#164A41')
window.mainloop()