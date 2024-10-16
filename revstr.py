class class_reverse:

    def __init__(self,s):
        self.s = s
    
    def reverse_word(self):
        return self.s[::-1]

str = input("Enter the word to be reversed: ")
revObj = class_reverse(str)

print(f"Reversed String is : {revObj.reverse_word()}")