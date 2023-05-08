class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    
    def __str__(self):
        return str(self.items)

    
    def __iter__(self):
        return iter(self.items)

    def __getitem__(self,index):
        return self.items[index]

#    def __setitem__(self,index,new_item):
#        self.items[index] = new_item

