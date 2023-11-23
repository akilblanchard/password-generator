import random

uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase = ["a", "b", "c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2"," 3", "4", "5", "6", "7", "8"," 9"," 0"]
symbols = ["!", "@", "$", ">", "(", "*"]

all = uppercase + lowercase + numbers +symbols

length = 12

password = " ".join(random.sample(all, length))

print(f"Your password is {password}")