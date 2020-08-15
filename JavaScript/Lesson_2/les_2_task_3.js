'use sctrict';

// Объявить две переменные и задать им целочисленные произвольные начальные значения
let a = 3;
let b = -10;
let c = 0;

let x = Math.sign(a);
let y = Math.sign(b);


if (a > 0 && b > 0) {
	c = a - b;
} else if (a < 0 && b < 0) {
	c = a * b;
} else if (x != y) {
	c = a + b;
} else {
	alert('Все не так!');
}
