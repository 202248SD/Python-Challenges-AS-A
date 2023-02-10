letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
a = 0
def encode(plaintext,key):
  cipher = ""
  text = plaintext.lower()
  for lettersintext in text:
      if lettersintext == " ":
          cipher+= " "
      else:
          for i in range(len(letter)):
              if letter[i] == lettersintext:
                if i+key>26:
                  a = i+key-26
                else:
                  a = i+key
                print(a,letter[i+key])
                cipher+= letter[i+key]
                break
  return cipher
print(encode("Hi",3))
#AS07
