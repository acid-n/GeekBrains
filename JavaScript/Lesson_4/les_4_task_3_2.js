'use sctrict';

class Post {
    constructor(author, text, date) {
        this.author = author;
        this.text = text;
        this.date = date;
    }

    edit(text) {
        this.text = text;
    }
}

const post1 = new Post('alex', 'new text new text', new Date());
console.log(post1);
post1.edit('edit new post');
console.log(post1);


class AttachedPost extends Post {
    constructor(author, text, date) {
        super(author, text, date);
        this.highlighted = false;
    }

    makeTextHighlighted() {
        this.highlighted = true;
    }
}

const attached1 = new AttachedPost('admin', 'attached new post', new Date());
console.log(attached1);
attached1.makeTextHighlighted();
attached1.edit('edit attached new post');
console.log(attached1);