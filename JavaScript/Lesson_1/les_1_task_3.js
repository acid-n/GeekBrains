'use sctrict';

/*
Число 10 прибавляем к числу 10 и получаем результат 20
К 20 прибавляем "10" и получаем строку "2010"
Строку присваиваем переменной result
С помощью console.log выводим результат в консоль
*/

let result = 10 + 10 + "10";
console.log(result);

/*
Число 10 прибавляем к строке "10" и получаем результат строку "1010"
К строке "1010" прибавляем число 10 и получаем строку "101010"
Строку присваиваем переменной result
С помощью console.log выводим результат в консоль
*/

result = 10 + "10" + 10;
console.log(result);

/*
Число 10 прибавляем к числу 10 и получаем результат число 20
К числу 20 с помощью унарного плюса добавляем строку "10" которая преобразуется в число 10, получаем результат 30
Число присваиваем переменной result
С помощью console.log выводим результат в консоль
*/

result = 10 + 10 + +"10";
console.log(result);


/*
Число 10 делим на строку с унарным минусом, строка пустая, получаем -0
Число 10 делим на 0 и Получаем отрицательную бесконечность 
Бесконечность присваиваем переменной result
С помощью console.log выводим результат в консоль
*/

result = 10 / -"";
console.log(result);


/*
Число 10 делим на строку с унарным плюсом и получаем число 2,5 но дроби должны быть с точкой, поправляем
далее 10 делим на 2.5
Результат  присваиваем переменной result
С помощью console.log выводим результат в консоль
*/

result = 10 / +"2.5";
console.log(result);



