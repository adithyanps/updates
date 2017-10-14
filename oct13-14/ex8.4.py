import sys
def find(word,letter,d):
 while d < len(word):
  if word[d] == letter:
   print d
  d = d + 1
a = raw_input("enter the string : ")
b = raw_input("enter the letter 2 b searched ")
c = int(input("enter the index from looking up : "))
print find(a,b,c)
if __name__ == "__find__":
 find(a,b,c)
