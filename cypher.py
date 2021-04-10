# def greet(name):
#   print(f'Hello {name}')
#   print(f'Lovely weather we are having today, {name}')
#   print(f'You are a magnificent god of awesomeness, {name}')
  
# greet('Jonny')

# def greet_with(name = 'Jonny', location = 'Asgard'):
#   print(f'Hello {name} of {location}')
#   print(f'Lovely weather we are having today, {name} of {location}')
#   print(f'You are a magnificent god of awesomeness, {name} of {location}')
  
# greet_with()

# def prime_checker(number):
#   acc = 0
#   for num in range(1,10):
#     if number % num == 0:
#       acc += 1
#     else:
#       acc
#   if number < 10:
#     if acc != 2:
#       print('Not a prime number!')
#     else:
#       print('Prime number!')
#   else:
#     if acc != 1:
#       print('Not a prime number!')
#     else:
#       print('Prime number!')



# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
  text_list = list(text)
  new_list = []
  for letter in text_list:
    if letter in alphabet:
      if alphabet.index(letter) + shift < len(alphabet):
        text_list[text_list.index(letter)] = alphabet[alphabet.index(letter) + shift]
        new_list.append(alphabet[alphabet.index(letter) + shift])
      elif alphabet.index(letter) + shift >= len(alphabet):
        ind_val = len(alphabet) - alphabet.index(letter)
        ind = shift - ind_val
        new_list.append(alphabet[ind])
        text_list[text_list.index(letter)] = alphabet[ind]
    else:
      new_list.append(letter)
        
      
  encoded_text = ''.join(new_list)
  print(f'The encoded text is: {encoded_text}')
  
def decrypt(text, shift):
  text_list = list(text)
  new_list = []
  for letter in text_list:
    if letter in alphabet:
      text_list[text_list.index(letter)] = alphabet[alphabet.index(letter) - shift]
      new_list.append(alphabet[alphabet.index(letter) - shift])
    else:
      new_list.append(letter)
  decoded_text = ''.join(new_list)
  print(f'The decoded text is: {decoded_text}')
  
if direction == 'encode':
  encrypt(text, shift)
elif direction == 'decode':
  decrypt(text, shift)
  

