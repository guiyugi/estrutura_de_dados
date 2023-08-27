class Lista:
    def __init__(self):
        self.l = []
    def show_list(self):
        return(self.l, len(self.l))
    def insert_at_index(self, value, index):
        if 0 <= index <= len(self.l):
            if index == len(self.l):
                self.l.append(value)
            else:
                self.l = self.l[:index] + [value] + self.l[index:]
        else:
            print('\n!======= Index out of range of the list =======!')
    def remover(self,index):
        if 0<= index < len(self.l):
            new_list = []
            for newindex, item in enumerate(self.l):
                if newindex != index:
                    new_list.append(item)
            self.l = new_list 
            print()
            print('='*40)
            print('Sucessful operation!')
            print('='*40)
        else:
            print('\n! !======= Element out of range of the list =======!')
    def show_value(self, index):
        if 0 <= index < len(self.l):
            return (self.l[index])
        else:
            return 'Index not found in the list'
    def show_index(self,value):
        position_list = []
        for index, item in enumerate(self.l):
            if item == value:
                position_list.append(index)
        if position_list:
            return position_list
        else:
            return 'Not in list'
    def insert_at_first(self, value):
        self.l[0:0] = [value]
    def insert_at_last(self, value):
        self.l[len(self.l):-1] = [value]
    def remove_at_first(self):
        self.l = self.l[1:]
    def remove_at_last(self):
        self.l = self.l[:-1]
    def modifier_element(self,index,new_value):
        self.l[index] = new_value    
    def remove_element(self, value):
        new_list = []
        for item in self.l:
            if item != value:
                new_list.append(item)
        self.l = new_list
