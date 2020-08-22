'use sctrict';

function numberCheck(number) {
    if (!Number.isInteger(number) || number < 0 || number > 999) {
        console.log('Не верное значение. Цисло должно быть целым от 0 до 999.');
        return {};
    }

    return {
        units: number % 10,
        tens: Math.floor(number / 10) % 10,
        hundreds: Math.floor(number / 100),
    }
}

console.log(numberCheck(425));