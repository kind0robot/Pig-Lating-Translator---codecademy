
print ("Welcome to your Pig Lating Translator.")
print ("Pig Latin = any english word with the first letter substracted and added to the end of the word + ay.. because ay not")
#declare your word
original = input('Enter a word:')
#this if function checks if the lenght of the string is 0 and if the string is not a letter
if len(original) > 0 and original.isalpha():
#lowercase the word
  word= original.lower()
  pyg = 'ay'
#copy the first letter of the word
  first=word[0]
#string concatenate
  new_word=word+first+pyg
#slice the word from it`s first letter - begin from letter "1" when py usually runs from "0"
  new_word=new_word[1:len(new_word)]
  print ("Your Pig Latin Translated word is: "+ new_word + ".")
  print ("Now you can summon your pig daemon with it!")
  print ("	p.s. let it lowercase if you`re writing it with blood ")
else:
  print ('Empty or a symbol or a word. Restart script!')
