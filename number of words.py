Sentence = input("Enter your Sentence: ").strip()
words = 0
space = False
flag = False
for char in Sentence:
  if char==" ":
     if space==False:
       words += 1
       space = True
       flag = True
  else:
      space = False

if flag == True:
    print(f"There is {words+1} word in your sentence.")
else:
    print(f"There is no word in your sentence.")
