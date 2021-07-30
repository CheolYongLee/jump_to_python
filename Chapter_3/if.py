# if.py

money = True

if money:
    print("택시를")
    print("타고")
    print("가라")

# --------------------------------------

money = 2000

if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# --------------------------------------

money = 2000
card = True

if money > 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# --------------------------------------

pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# --------------------------------------

if 'card' not in pocket:
    print("걸아 가라")
else:
    print("버스를 타고 가라")


# --------------------------------------

pocket = ['paper', 'money', 'cellphone']

if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")


# --------------------------------------

pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket:
    print("택시를 타고 가라")
elif 'card' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# --------------------------------------

pocket = ['paper', 'money', 'cellphone']

if 'money' in pocket: pass
else: print("카드를 거내라")

# --------------------------------------

score = 65
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)

# --------------------------------------

score = 40
message = "success" if score >= 60 else "failure"
print(message)
