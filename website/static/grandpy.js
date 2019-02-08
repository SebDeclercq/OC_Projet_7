// @note       Script containing all actions correlated to GrandPy, including
//             AJAX querying and HTML page updates
// @author     Sébastien Declercq <sdq@afnor.org>
// @version    0.0.1 (2019-02-06) : init

class GrandPy {
    // Main Class
    constructor() {
        this.form = document.querySelector('form#GrandPy');
        this.input = this.form.querySelector('input#ask-grandpy');
        this.chat_area = document.querySelector('div#chat-area');
    }
    listen() {
        // Sets the event listener up : on form submit, queries
        // the Flask App to retrieve collected infos based on the
        // user input
        this.form.addEventListener('submit', () => {
            let data = new FormData();
            data.append('query', this.input.value);
            let xhr = new XMLHttpRequest();
            xhr.open('POST', '/ask-grandpy');
            xhr.addEventListener('load', () => {
                const answer = JSON.parse(xhr.responseText);
                this.chat_area.appendChild(
                    this._create_chat_entry(
                        this.input.value, answer['title'], answer['summary']
                    )
                );
                this.chat_area.style.display = 'block';
                this.chat_area.querySelector(
                        '.chat-entry:last-child'
                ).scrollIntoView({ block: 'start',  behavior: 'smooth' });
            });
            xhr.send(data);
        });
    }
    _create_chat_entry(query, title, summary) {
        // Creates a new Element representing a chat entry
        // query: string    The input query
        // title: string    The title of the wikipedia article
        // summary: string  The summary of the wikipedia article
        let chat_entry = document.createElement('div');
        chat_entry.setAttribute('class', 'chat-entry');
        const values = [
            ['h3', 'Alors, tu veux savoir ça ?! "' + query + '"'],
            ['h4', title], ['p', summary],
        ];
        for (let value of values) {
            chat_entry.appendChild(this._create_element(...value));
        }
        return chat_entry;
    }
    _create_element(el_name, value) {
        // Simply creates an Element containing a value
        // el_name: string  Tag name
        // value: string    Tag content
        let el = document.createElement(el_name);
        el.appendChild(document.createTextNode(value));
        return el;
    }
}

// Starts GrandPy up
window.addEventListener('load', () => {
    grandpy = new GrandPy();
    grandpy.listen();
});
