def add(a, b):
    n_add = a+b
    return n_add


def sub(a, b):
    n_sub = a-b
    return n_sub


def mul(a, b):
    n_mul= a*b
    return n_mul


def div(a, b):
    n_div=a/b
    return n_div


def power(base, pow):
    n_power = base**pow 
    return n_power


def square(base):
    n_square=base**2
    return n_square


def greet(이름="낯선자", 나이=20):
    if 나이>=20 and 나이<=40:
        return (f"안녕하신가 {이름}!")
    elif 나이>40:
        return(f"안녕하십니까 {이름}!")
    else:
        return (f"안녕 {이름}!")
    