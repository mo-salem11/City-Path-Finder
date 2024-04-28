import tkinter as tk
from graphs import *


graph = {
    
    'Arad': [('Sibiu',140), ('Zerind',75), ('Timisoara',118)], 
    'Zerind': [('Arad',75), ('Oradea',71)],
    'Oradea': [('Zerind',71), ('Sibiu',151)],
    'Sibiu': [('Arad',140), ('Oradea',151), ('Fagaras',99), ('Rimnicu Vilcea',80)],
    'Timisoara': [('Arad',118), ('Lugoj',111)],
    'Lugoj': [('Timisoara',111), ('Mehadia',70)],
    'Mehadia': [('Lugoj',70), ('Drobeta',75)],
    'Drobeta': [('Mehadia',75), ('Craiova',120)],
    'Craiova': [('Drobeta',120), ('Rimnicu Vilcea',146), ('Pitesti',138)],
    'Rimnicu Vilcea': [('Sibiu',80), ('Craiova',146), ('Pitesti',97)],
    'Fagaras': [('Sibiu',99), ('Bucharest',211)],
    'Pitesti': [('Rimnicu Vilcea',97), ('Craiova',138), ('Bucharest',101)],
    'Bucharest': [('Fagaras',211), ('Pitesti',101), ('Giurgiu',90), ('Urziceni',85)],
    'Giurgiu': [('Bucharest',90)],
    'Urziceni': [('Bucharest',85), ('Vaslui',142), ('Hirsova',98)],
    'Hirsova': [('Urziceni',98), ('Eforie',86)],
    'Eforie': [('Hirsova',86)],
    'Vaslui': [('Iasi',92), ('Urziceni',142)],
    'Iasi': [('Vaslui',92), ('Neamt',87)],
    'Neamt': [('Iasi',87)]
}

def find_path():
    start_county = start_var.get()
    end_county = end_var.get()
    selected_algorithm = algorithm_var.get()

    # call the appropriate algorithm based on the selected option
    if selected_algorithm == "DFS":
        path = dfs(graph, start_county, end_county)
    elif selected_algorithm == "A*":
        
        path = A_star(graph, start_county, end_county)
    elif selected_algorithm =="GBFS":
         path =greedy(graph, start_county, end_county)
    elif selected_algorithm=="BFS":
        path=bfs(graph,start_county,end_county)
    # display the path in the GUI
    path_label.config(text=path)

def select_start_country():
    global start_country_window
    start_country_window = tk.Toplevel(window)
    start_country_window.title("Select Start Country")
    start_country_window.geometry('400x400')
    start_country_window.resizable(False,False)
    title = tk.Label(start_country_window, text="Select the start city", fg='gold', bg='black', font=('tajawal', 16, 'bold'))
    title.pack(fill=tk.X, pady=10)
    F1 = tk.Frame(start_country_window, width=800, height=420, bg='#0B2F3A')
    F1.place(x=0, y=40)



    country_listbox = tk.Listbox(start_country_window)
    country_listbox.configure(width=100)
    for country in countries:
        country_listbox.insert(tk.END, country)
    country_listbox.pack()

    select_button = tk.Button(start_country_window, text="Select", command=lambda: select_country(country_listbox, start_var, start_country_label))
    select_button.configure(padx=35,highlightthickness=10,bg='#DBA901', fg='white')
    
    select_button.pack()

def select_end_country():
    global end_country_window
    end_country_window = tk.Toplevel(window)
    end_country_window.geometry('400x400')
    end_country_window.resizable(False,False)
    end_country_window.title("Select End Country")
    title = tk.Label(end_country_window, text="Select the Goal", fg='gold', bg='black', font=('tajawal', 16, 'bold'))
    title.pack(fill=tk.X, pady=10)
    F1 = tk.Frame(end_country_window, width=800, height=420, bg='#0B2F3A')
    F1.place(x=0, y=40)

    country_listbox = tk.Listbox(end_country_window)
    country_listbox.configure(width=100)
    for country in countries:
        country_listbox.insert(tk.END, country)

    country_listbox.pack()

    select_button = tk.Button(end_country_window, text="Select", command=lambda: select_country(country_listbox, end_var, end_country_label))
    select_button.configure(padx=35,highlightthickness=10,bg='#DBA901', fg='white')
    select_button.pack()

def select_country(listbox, var, label):
    selected_country = listbox.get(tk.ACTIVE)
    var.set(selected_country)
    label.config(text=selected_country)
    listbox.master.destroy()

window = tk.Tk()
window.geometry('1150x500+280+50')
window.resizable(False,False)
window.title('Searching On the map')
# create a new Label widget for the title
title = tk.Label(window, text="AI Project GUI", fg='gold', bg='black', font=('tajawal', 16, 'bold'))

# use the pack method to add the title to the window
title.pack(fill=tk.X, pady=10)

# create a new Frame widget
F1 = tk.Frame(window, width=1150, height=420, bg='#0B2F3A')
F1.place(x=0, y=40)

# create a new Label widget for the title of the frame
Title1 = tk.Label(F1, text='Select any two cities', bg='#0B2F3A', fg='white', font=('tajawal', 12, 'bold'))
Title1.place(x=500, y=10)





start_frame = tk.Frame(window)
start_label = tk.Label(start_frame, text="Start City:")
start_label.configure(height=3,font=('tajawal', 12, 'bold'))
start_button = tk.Button(start_frame, text="Select", command=select_start_country)
start_country_label = tk.Label(start_frame, text="")

end_frame = tk.Frame(window)
end_label = tk.Label(end_frame, text="End City:")
end_label.configure(height=3,font=('tajawal', 12, 'bold'))
end_button = tk.Button(end_frame, text="Select", command=select_end_country)
end_country_label = tk.Label(end_frame, text="")

algorithm_frame = tk.Frame(window)
algorithm_label = tk.Label(algorithm_frame, text="Select Search Algorithm:")
algorithm_label.configure(height=3,font=('tajawal', 12, 'bold'))
algorithm_var = tk.StringVar()
algorithm_menu = tk.OptionMenu(algorithm_frame, algorithm_var, "DFS", "A*","GBFS","BFS")


find_path_button = tk.Button(window, text="Find Path", command=find_path)
find_path_button.configure(height=3,font=('tajawal', 12, 'bold'))

# define the variables that will hold the selected countries and algorithm
start_var = tk.StringVar()
end_var = tk.StringVar()



# pack the widgets into the frames

# configure the background color of the frames, buttons, and labels
start_frame.configure(bg='#DBA901')
end_frame.configure(bg='#DBA901')
algorithm_frame.configure(bg='#DBA901')
start_button.configure(bg='#DBA901')
end_button.configure(bg='#DBA901')
algorithm_menu.configure(bg='#DBA901')
start_label.configure(bg='#DBA901', fg='white')
end_label.configure(bg='#DBA901', fg='white')
start_country_label.configure(bg='#DBA901', fg='white')
end_country_label.configure(bg='#DBA901', fg='white')
algorithm_label.configure(bg='#DBA901', fg='white')

# pack the widgets into the frames
start_label.pack(side=tk.LEFT, padx=10, anchor='w')
start_button.pack(side=tk.RIGHT, padx=10, anchor='e')
start_country_label.pack(side=tk.RIGHT, padx=10, anchor='e')
end_label.pack(side=tk.LEFT, padx=10, anchor='w')
end_button.pack(side=tk.RIGHT, padx=10, anchor='e')
end_country_label.pack(side=tk.RIGHT, padx=10, anchor='e')
algorithm_label.pack(side=tk.LEFT, padx=10, anchor='w')
algorithm_menu.pack(side=tk.RIGHT, padx=10, anchor='e')

# pack the frames into the window
start_frame.pack(pady=10, anchor='w')
end_frame.pack(pady=10, anchor='w')
algorithm_frame.pack(pady=10, anchor='w')
find_path_button.configure(bg='#DBA901')
find_path_button.pack(pady=10, anchor='w')
# define the list of countries
countries =["Arad", "Zerind", "Oradea",'Sibiu','Timisoara','Lugoj','Mehadia','Drobeta','Craiova','Rimnicu Vilcea','Fagaras','Pitesti','Bucharest', 'Giurgiu','Urziceni','Hirsova','Eforie','Vaslui',"Iasi", "Neamt"]

# add a label to display the path
path_label = tk.Label(window, text="")
path_label.configure(font=('tajawal', 12, 'bold'))
path_label.pack(pady=10)






# start the event loop
window.mainloop()