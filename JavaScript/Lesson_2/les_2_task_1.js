'use sctrict';

// пример 1
let a = 1, b = 1, c, d;
c = ++a;
// переменная "а" увеличилась на 1 (инкремент) и результат присвоен переменной "с" (префиксная форма возврщает новое значение)
alert(c);

// пример 2
d = b++;
// переменная "b" увеличилась на 1 (инкремент), но так как это постфиксная форма, то в переменную "d" вернулось старое значение (до увеличения)
alert(d);

// пример 3
c = 2 + ++a;
// переменная "а" увеличилась на 1 (инкремент) и к ней прибавили еще 2, в переменную "с" записали 5, а в переменно "а" осталось 3
alert(c);

// пример 4
d = 2 + b++;
// переменная "b" увеличилась на 1 после операции сложения, в переменную "d" записали 4, так как на момент сложения в переменной "b" было 2
alert(d);

alert(a);
alert(b);