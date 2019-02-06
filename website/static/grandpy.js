// @note       Script containing all actions correlated to GrandPy, including
//             AJAX querying and HTML page updates
// @author     Sébastien Declercq <sdq@afnor.org>
// @version    0.0.1 (2019-02-06) : init

class GrandPy {
    // Main Class
    constructor() {
        this.form = document.querySelector('form#GrandPy')
        this.input = this.form.querySelector('input#ask-grandpy')
    }
    listen() {
        // Sets the event listener up : on form submit, queries
        // the Flask App to retrieve collected infos based on the
        // user input
        this.form.addEventListener('submit', () => {
            let data = new FormData()
            data.append('query', this.input.value)
            let xhr = new XMLHttpRequest()
            xhr.open('POST', '/ask-grandpy')
            xhr.onload = function() {
                console.log(this.responseText)
            }
            xhr.send(data)
        })
    }
}

// Starts GrandPy up
window.onload = function() {
    grandpy = new GrandPy()
    grandpy.listen()
}
