class Graph:
    def __init__(self, data, is_show = True):
        self.data = data.copy()
        self.is_show = is_show
        
    def set_data(self, data):
        self.data = data.copy()
        
    def show_table(self):
        if self.is_show == True:
            print(" ".join(map(str, self.data)))
        else:
            print("Отображение данных закрыто")
            
    def show_graph(self):
        if self.is_show == True:
            print(f'Графическое отображение данных: {" ".join(map(str, self.data))}')
        else:
            print("Отображение данных закрыто")
            
    def show_bar(self):
        if self.is_show == True:
            print(f'Столбчатая диаграмма: {" ".join(map(str, self.data))}')
        else:
            print("Отображение данных закрыто")
            
    def set_show(self, fl_show):
        self.is_show = fl_show
        
# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()