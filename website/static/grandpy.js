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
            this.add_query_to_chat(this.input.value);
            let data = new FormData();
            data.append('query', this.input.value);
            let xhr = new XMLHttpRequest();
            xhr.open('POST', '/ask-grandpy');
            xhr.onload = () => {
                const answer = JSON.parse(xhr.responseText);
                let chat_entry = document.createElement('div');
                chat_entry.appendChild(
                    this.create_chat_entry('h4', answer['title'])
                );
                chat_entry.appendChild(
                    this.create_chat_entry('p', answer['summary'])
                );
                this.chat_area.appendChild(chat_entry);
            };
            xhr.send(data);
        });
    }
    create_chat_entry(el_name, value) {
        let el = document.createElement(el_name);
        el.appendChild(document.createTextNode(value));
        return el
    }
    add_query_to_chat(query) {
        let h3 = document.createElement('h3')
        h3.appendChild(document.createTextNode(
            'Alors, tu veux savoir ça ?! "' + query + '"')
        )
        this.chat_area.appendChild(h3)
    }
}

// Starts GrandPy up
window.onload = function() {
    grandpy = new GrandPy();
    grandpy.listen();
}
