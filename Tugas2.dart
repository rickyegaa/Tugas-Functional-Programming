// .............................................. Jawaban ................................................................

//  Kode 1
List<int> sequenceGenerator(int start, int stop) {
  List<int> x = [];
  for (int i = start; i <= stop; i++) {
    x.add(i);
  }
  return x;
}

void main() {
  print(sequenceGenerator(1, 10));
}

// Kode 2
List<dynamic> fizzBuzz(int a, int b) {
  List<dynamic> x = [];
  for (int num = a; num < b; num++) {
    if (num % 3 == 0 && num % 5 == 0) {
      x.add('FizzBuzz');
    } else if (num % 3 == 0) {
      x.add('Fizz');
    } else if (num % 5 == 0) {
      x.add('Buzz');
    } else {
      x.add(num);
    }
  }
  return x;
}

void main() {
  print(fizzBuzz(1, 20));
}

// Kode 3
List<int> twoNumber(List<int> l) {
  List<int> res = [];
  for (int i = 0; i < l.length - 1; i++) {
    int z = l[i] + l[i + 1];
    res.add(z);
  }
  return res;
}

void main() {
  print(twoNumber([1, 2, 3, 4, 5]));
}

