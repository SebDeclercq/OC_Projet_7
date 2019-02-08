// @note       Script containing all actions correlated to GrandPy, including
//             AJAX querying and HTML page updates
// @author     Sébastien Declercq <sdq@afnor.org>
// @version    0.0.1 (2019-02-06) : init
/*jshint esversion: 6 */

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
                let chat_entry;
                if (xhr.status == 200) {
                    chat_entry = this._create_chat_entry(
                        this.input.value, answer.title, answer.summary,
                        answer.coord, answer.url
                    );
                }
                else if (xhr.status == 400) {
                    chat_entry = document.createElement('div');
                    chat_entry.setAttribute('class', 'chat-entry');
                    chat_entry.appendChild(
                        document.createTextNode(answer.answer)
                    );
                }
                this.chat_area.appendChild(chat_entry);
                this.chat_area.style.display = 'block';
                this.chat_area.querySelector(
                    '.chat-entry:last-child'
                ).scrollIntoView({ block: 'start',  behavior: 'smooth' });
            });
            xhr.send(data);
        });
    }

    _create_chat_entry(query, title, summary, coord, url) {
        // Creates a new Element representing a chat entry
        // query: string    The input query
        // title: string    The title of the wikipedia article
        // summary: string  The summary of the wikipedia article
        // coord: object    The object containing latitude and longitude
        //                  for google map display
        let chat_entry = document.createElement('div');
        chat_entry.setAttribute('class', 'chat-entry');
        const values = [
            ['h3', 'Alors, tu veux savoir ça ?! "' + query + '"'],
            ['h4', title], ['p', summary],
        ];
        for (let value of values) {
            chat_entry.appendChild(this._create_element(...value));
        }
        let url_el = document.createElement('a');
        url_el.setAttribute('href', url);
        url_el.setAttribute('_target', 'blank');
        url_el.appendChild(
            document.createTextNode(" Tu veux encore plus d'infos ?")
        );
        chat_entry.querySelector('p').appendChild(url_el);
        chat_entry.appendChild(this._create_map(coord));
        return chat_entry;
    }

    _create_map(coord) {
        // Creates a new Element containing the Google Map
        // coord: object    The object containing latitude and longitude
        //                  for google map display
        let div_map = document.createElement('div');
        div_map.setAttribute('class', 'map');
        let coord_obj = {lat: coord.latitude, lng: coord.longitude};
        let map = new google.maps.Map(div_map, {
          zoom: 15,
          center: coord_obj
        });
        let marker = new google.maps.Marker({
          position: coord_obj,
          map: map,
          title: "Ce que tu cherches, c'est là, mon gars !!!"
        });
        return div_map;
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
    let grandpy = new GrandPy();
    grandpy.listen();
});
