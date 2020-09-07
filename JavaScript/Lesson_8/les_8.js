'use strict';



class Table{
    constructor() {
        this.table = document.getElementById('desk');
        this.status = 'playing';
        this.mapValues = [
            ['', '', ''],
            ['', '', ''],
            ['', '', ''],
        ];
        this.step = 'X';
        
    }
    

    init() {
        this.makeTable();
        this.createHandlers();
    }

    makeTable() {
        let table = document.createElement('table');
        for (let j=0; j<3; j++) {
            let tr = document.createElement('tr');
            for (let i=0; i<3; i++) {
                let td = document.createElement('td');
                td.dataset.row = j.toString();
                td.dataset.col = i.toString();
                tr.appendChild(td);
                table.appendChild(tr);
            }
            this.table.appendChild(table);
        }
    }

    createHandlers() {
        this.table.addEventListener('click', event => this.cellClickHandler (event));
    }

    fillCell(event) {
        let row = +event.target.dataset.row;
        let col = +event.target.dataset.col;
        this.mapValues[row][col] = this.step;
        event.target.textContent = this.step;
        this.changeStep();
    }

    cellClickHandler(event) {
        if (!this.isEmpty(event)) {
            return;
        }
        this.fillCell(event);
        if (this.hasWon()) {
            this.changeStep();
            alert(this.step + ' win');
            this.cleanTheMap();
            this.cleanTheDesk();
        } else {
            this.checkCells();
        }
    }

    isEmpty(event) {
        return event.target.textContent === "";
    }

    changeStep() {
        this.step = (this.step == "X") ? "O" : "X";
    }

    hasWon() {
        return this.isLineWon({ x: 0, y: 0 }, { x: 1, y: 0 }, { x: 2, y: 0 }) ||
            this.isLineWon({ x: 0, y: 1 }, { x: 1, y: 1 }, { x: 2, y: 1 }) ||
            this.isLineWon({ x: 0, y: 2 }, { x: 1, y: 2 }, { x: 2, y: 2 }) ||

            this.isLineWon({ x: 0, y: 0 }, { x: 0, y: 1 }, { x: 0, y: 2 }) ||
            this.isLineWon({ x: 1, y: 0 }, { x: 1, y: 1 }, { x: 1, y: 2 }) ||
            this.isLineWon({ x: 2, y: 0 }, { x: 2, y: 1 }, { x: 2, y: 2 }) ||

            this.isLineWon({ x: 0, y: 0 }, { x: 1, y: 1 }, { x: 2, y: 2 }) ||
            this.isLineWon({ x: 0, y: 2 }, { x: 1, y: 1 }, { x: 2, y: 0 });
    }

    isLineWon(a, b, c) {
        let value = this.mapValues[a.y][a.x] + this.mapValues[b.y][b.x] + this.mapValues[c.y][c.x];
        if (value === 'XXX' || value === '000') {
            return true;
        }    
    }

    checkCells() {
        let count = 0;
        for (let j=0; j<3; j++) {
            for (let i=0; i<3; i++) {
                if (this.mapValues[i][j] == 'X' || this.mapValues[i][j] == 'O') {
                    count++;
                }
            }
        }
        if (count == 9) {
            alert('game is over');
            this.cleanTheMap();
            this.cleanTheDesk();
        }
    }

    cleanTheMap() {
        for (let j=0; j<3; j++) {
            for (let i=0; i<3; i++) {
                this.mapValues[i][j] = '';
             }
        }
    }

    cleanTheDesk() {
        let table = document.createElement('table');
        this.table.children[0].remove();
        newTable.init();
    }
}


const newTable = new Table;
newTable.init();