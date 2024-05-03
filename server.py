from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

print(__name__)


@app.route('/')
def my_home():
    return render_template('./index.html')


# the path in the url may can also access name.html (but in this case it needs to be correctly typed in in the browser too)


# this piece over here substitutes all the lines below
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):  # this function stores data that given by a user/customer on the 'contacts' page and writes it to a file called database.txt so that this data won't fet lost
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n\nemail: {email},\nsubject: {
                              subject},\nmessage: {message}')


def write_to_csv(data):  # this function writes data on to a csv file that we created, which will store it in a excel like format
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again!'


# @app.route('/index.html')
# def home_button():
#     return render_template('./index.html')


# @app.route('/components.html')
# def components():
#     return render_template('./components.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('./contact.html')


# @app.route('/thankyou.html')
# def thankyou():
#     return render_template('./thankyou.html')


# @app.route('/work.html')
# def work():
#     return render_template('./work.html')


# @app.route('/works.html')
# def works():
#     return render_template('./works.html')
