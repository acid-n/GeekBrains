'use sctrict';

// Реализовать основные 4 арифметические операции (+,-,/,*) в виде функций с двумя параметрами.
// Т.е., например, функция для сложения должна принимать два числа, складывать их и возвращать результат.
// Обязательно использовать оператор return.

function operationAddition (a, b) {
	return a + b;
}


function operationSubtraction (a, b) {
	return a - b;
}

function operationMultiplication (a, b) {
	return a * b;
}

function operationDivision (a, b) {
	return a / b;
}

let resultSum = operationAddition(2, 2);
alert(resultSum);

let resultSub = operationSubtraction(2, 2);
alert(resultSub);

let resultMult = operationMultiplication(2, 2);
alert(resultMult);

let resultDiv = operationDivision(2, 2);
alert(resultDiv);
