# class Divisibility:
    
#     def __init__(self) -> None:
#         a = int(input("Input first number: "))
#         b = int(input("Input second number: "))
        
#         if a % b == 0:
#             print(f"{a} divine on {b}")
#         else:
#             print(f"{a} not divine on{b}")
            
# if __name__ == '__main__':
#     Divisibility()

#====================================================================================

# from datetime import datetime
# class ActualDate:
    
#     def __init__(self) -> None:
#         now_date = datetime.now()
#         print(f"Today {now_date.day}.{now_date.month}.{now_date.year}")
        
# if __name__ == '__main__':
#     ActualDate()

#====================================================================================

class Cargo:
    
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        
    def printCurrent(self):
        return print(self.name, self.count)
    
    def getPrice(self):
        return print(f"Общая стоимость товара: {self.price} * {self.count}")
    
