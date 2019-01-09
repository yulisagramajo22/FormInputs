from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

def process_drinks(drinks):
    # if they choose lemonade, sprite= sour
    # if they choose powerade, apple juice, water = sweet
    if drinks=='lemonade' or drinks=='sprite':
        return 'sour'

    if drinks=='powerade' or drinks=='apple juice' or drinks=='water':
        return 'sweet'

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    drinks = request.form.get('drinks', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    return render_template("main_page.html", input_data=name,
                          sour_output="You're a sour person %s." % name,
                           sweet_output="You're a sweet person %s." % name)
