import ollama
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
client = ollama.Client()




chat = ''''''

app = Flask(__name__, static_folder='static', static_url_path='')

cors = CORS(app, methods=['GET', 'POST'])
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def index():
    return app.send_static_file('index.html')

text_f ="chat.txt"
with open(text_f,'r') as file:
    chat = file.read()

@cross_origin()
@app.route('/getdata',methods =['GET','POST'])
def getdata():
    if request.json and 'chat' in request.json:
        # Store the chat data for other routes to use
        global chat
        chat = request.json['chat']
        return jsonify({"status": "success", "message": "Chat data received successfully"})
    else:
        return jsonify({"status": "error", "message": "No chat data provided"}), 400


@app.route('/persona',methods =['GET','POST'])
def create_persona():
    client = ollama.Client()

    prompt = f"Create a character persona of patient(member){chat}"

    sys_file="system_prompts/persona.txt"
    with open(sys_file,'r') as file:
        content = file.read()

        response = ollama.chat(model='llama3.1:8b', messages=[
        {
            'role': 'system',
            'content': content,
        },
        {
            'role': 'user',
            'content': prompt,
        },
        ])
        return str(response)


@app.route('/progress',methods =['GET','POST'])
def create_progress():
    client = ollama.Client()

    prompt = f"Create health progress of patient {chat}"

    sys_file="system_prompts/progress.txt"
    with open(sys_file,'r') as file:
        content = file.read()

        response = ollama.chat(model='llama3.1:8b', messages=[
        {
            'role': 'system',
            'content': content,
        },
        {
            'role': 'user',
            'content': prompt,
        },
        ])
        return str(response)


@app.route('/decision',methods =['GET','POST'])
def create_decision():
    client = ollama.Client()

    prompt = f"Why Decision were made like medicine, therapy,treatments,diagnostics,etc?{chat}"

    sys_file="system_prompts/decision.txt"
    with open(sys_file,'r') as file:
        content = file.read()

        response = ollama.chat(model='llama3.1:8b', messages=[
        {
            'role': 'system',
            'content': content,
        },
        {
            'role': 'user',
            'content': prompt,
        },
        ])
        return str(response)


@app.route('/track',methods =['GET','POST'])
def create_track():

    client = ollama.Client()

    prompt = f"Track number of hours/consults done by doctors,number of hours spent by coach etc.{chat}"

    sys_file="system_prompts/track.txt"
    with open(sys_file,'r') as file:
        content = file.read()

        response = ollama.chat(model='llama3.1:8b', messages=[
        {
            'role': 'system',
            'content': content,
        },
        {
            'role': 'user',
            'content': prompt,
        },
        ])
        return str(response)
    




if __name__ == "__main__":
    app.run(debug=True)