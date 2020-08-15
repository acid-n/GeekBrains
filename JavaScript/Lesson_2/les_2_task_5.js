'use sctrict';


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


function mathOperation(arg1, arg2, operation) {
	switch(operation) {
		case 'сложение':
			let result = operationAddition(arg1, arg2);
			alert(result);
			break;
		case 'вычитание':
			let result1 = operationSubtraction(arg1, arg2);
			alert(result1);
			break;
		case 'умножение':
			let result2 = operationMultiplication(arg1, arg2);
			alert(result2);
			break;
		case 'деление':
			let result3 = operationDivision(arg1, arg2);
			alert(result3);
			break;
	}
}



let arg1 = Number(prompt("Введите первое число: "));
let arg2 = Number(prompt("Введите второе число: "));
let operation = prompt("Введите операцию над числами: ");

mathOperation(arg1, arg2, operation);
