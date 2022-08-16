
class DataType:
    def __init__(self, type, description):
        self.type = type
        self.description = description

    def __del__ (self):
        print("Instancia eliminada")

    def get_info(self):
        print(self.type, self.description)

    def get_data_type(self):
        return self.type

    def show_description(self):
        print(self.description)

    def change_description(self, new_description):
        self.description = new_description
        print(self.description)

class MyArray(DataType):
    def __init__(self):
        DataType.__init__(self, "Array", "Enables storing a collection of multiple items under a single variable name, and has members for performing common array operations")
        self.length = 0
        self.data = {}
    
    def __del__(self):
        pass

    # Polimorfismo
    def get_info(self):
        print(self.type, self.length, self.data)

    def get(self, index):
        if index < self.length:
            return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self
    
    def pop(self):
        item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return item
    
    def indexOf(self, item):
        for i, e in self.data.items():
            if e == item:
                return i
    
    def includes(self, item):
        for e in self.data.values():
            if e == item:
                return True
        return False
    
    def forEach(self, func):
        for e in self.data.values():
            func(e)

class IntArray(MyArray):
    def __init__(self):
        MyArray.__init__(self)
    
    def __del__(self):
        pass
    
    # Suma todos los elementos del arreglo y retorna el resultado
    def add(self):
        addition = 0
        for e in self.data.values():
            addition += e 
        return addition
    
    # Resta todos los elementos del arreglo y retorna el resultado
    def sub(self):
        substrac = 0
        for e in self.data.values():
            substrac -= e 
        return substrac

    # Multiplica todos los elementos del arreglo y retorna el resultado
    def mul(self):
        product = 0
        for e in self.data.values():
            product *= e 
        return product

    # Polimorfismo
    def push(self, item):
        if type(item) is int:
            return super().push(item)
        print("NaN")
        
    def indexOf(self, item):
        if type(item) is int:
            return super().indexOf(item)
        else:
            print("NaN")
        
    def includes(self, item):
        if type(item) is int:
            return super().includes(item)
        else:
            print("NaN")
    

def main():

    my_int = DataType("Integer", "An integer (pronounced IN-tuh-jer) is a whole number (not a fractional number) that can be positive, negative, or zero")
    my_int.change_description("Is a number")
    print(my_int.get_data_type())

    my_array = MyArray()
    my_array.push(10)
    my_array.push(20)
    my_array.forEach(print)

    int_array = IntArray()
    int_array.push("1")
    int_array.push(2)
    int_array.push(3)
    int_array.push(4)
    result = int_array.add()
    print(int_array.indexOf(2))

if __name__ == "__main__":
    main()