from flask import Flask, render_template, request , redirect, escape
import search4letter

app = Flask(__name__)

#log_request function
def log_request(req:'flask requests', res:str) -> None:
    with open('search.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep="|")

#routing ip to the main page
@app.route('/')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to my search4letter website')

#search4letter action is being performed here
@app.route('/search4', methods=['POST'])
def s4letter() -> 'html':
    phrase = request.form['phrase']
    letter = request.form['letters']
    title = 'Here are your search results'
    result = search4letter.search4letter(phrase, letter)
    log_request(request, result)
    return render_template('result.html',the_title=title, the_phrase=phrase,
                    the_results = result, the_letters = letter)

#view logs of the requests and responses
@app.route('/viewlog')
def viewlog() -> 'html':
    content = []
    with open('search.log', 'r') as file:
        for line in file:
            content.append([])
            for i in line.split("|"):
                content[-1].append(escape(i))
    titles = ('Form Data', 'Remote Address', 'User Agent', 'Results')
    return render_template('viewlog.html', the_title = 'View Logs',
                                the_row_titles = titles,
                                the_data = content,)

#running our webapp
if __name__ == '__main__':
    app.run(debug=True)
