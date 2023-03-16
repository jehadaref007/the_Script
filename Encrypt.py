# طلب مكتبت التشفير و مكتبت التلوين

'''
md5(), sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s()
'''

import hashlib,termcolor
# هنا لتلوين
print(termcolor.colored("1 = md5",'green'      ))
print(termcolor.colored("2 = sha1",'green'     ))
print(termcolor.colored("3 = sha224",'green'   ))
print(termcolor.colored("4 = sha256",'green'   ))
print(termcolor.colored("5 = sha384",'green'   ))
print(termcolor.colored("6 = sha512",'green'   ))
print(termcolor.colored("7 = blake2b",'green'  ))
print(termcolor.colored("8 = blake2s",'green'  ))

# طلب من المستخدم نووع التشفير

Encrypt = float(input('{^ % ^} enter your type for Encrypt : '))
# طلب من المستخدم هو النص الذي يريد تشفيره

text = input("{^ & ^} enter your text for Encrypt : ")

One = hashlib.md5(text.encode()).hexdigest()

Two = hashlib.sha1(text.encode()).hexdigest()

three = hashlib.sha224(text.encode()).hexdigest()

four = hashlib.sha256(text.encode()).hexdigest()

five = hashlib.sha384(text.encode()).hexdigest()

six = hashlib.sha512(text.encode()).hexdigest()

Seven = hashlib.blake2b(text.encode()).hexdigest()

eight = hashlib.blake2s(text.encode()).hexdigest()



if Encrypt == 1:
    print(termcolor.colored("Succeeded :)", 'green'))
    print(One)

if Encrypt == 2:
    print(termcolor.colored("Succeeded :)", 'green'))
    print(Two)

if Encrypt ==3:
    print(termcolor.colored("Succeeded :)", 'green'))
    print(three)

if Encrypt == 4:
    print(termcolor.colored("Succeeded :)", 'green'))
    print(four)

if Encrypt == 5:
    print(termcolor.colored("Succeeded :)", 'green'))
    print(five)

if Encrypt == 6:
    print(termcolor.colored("Succeeded :)", 'green'))
    print(six)

if Encrypt == 7:
    print(termcolor.colored("Succeeded :)", 'green'))
    print(Seven)

if Encrypt == 8:
    print(termcolor.colored("Succeeded :)", 'green'))
    print(eight)



# في حال المستخدم لم يدخل شي يعطيه هناك خط بلون الاحمر
if Encrypt > 8:

    print(termcolor.colored("NOT SUCCEEDED :(", 'red'))

    print(termcolor.colored("Pless Enert NUM (1--8) And Agen", "green"))
# في حال المستخدم ادخل مساحة يعطيه هناك خطا بلون الاحمر
if Encrypt < 1:

    print(termcolor.colored("NOT SUCCEEDED :(", 'red'))

    print(termcolor.colored("Pless Enert NUM (1--8) And agen","green"))


print(termcolor.colored(" The property rights By {Jehad Mosa} ", "red",'on_white'))
