# ................................................ Soal ..................................................................

# Kode 1
def sequenceGenerator(start, stop):
    x = []
    for i in range(start, stop+1):
        x.append(i)
    return x
print(sequenceGenerator(1, 10))

# Kode 2
def fizzBuzz(a, b):
    x = []
    for num in range(a, b):
        if num % 3 == 0 and num % 5 == 0:
            x.append('FizzBuzz')
        elif num % 3 == 0:
            x.append('Fizz')
        elif num % 5 == 0:
            x.append('Buzz')
        else:
            x.append(num)
    return x

# Kode 3
def twoNumber(l):
    res : []
    for i in l:
        if l.index(i) == len(l)-1:
            break
        z = i + l[i+1]
        res.append(z)
    return res





# .............................................. Jawaban ................................................................

# Kode 1
sequenceGenerator = lambda start, stop: list(range(start, stop+1))
print(sequenceGenerator(1, 10))

# Kode 2
fizzBuzz = lambda a, b: ['FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(a, b)]

# Kode 3
twoNumber = lambda l: [l[i] + l[i+1] for i in range(len(l)-1)]








