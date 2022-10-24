from flask import Flask, request
import os
app = Flask(__name__)

@app.route("/")
def start():
    '''
    Para fazer chamadas: 
    http://127.0.0.1:5000/?nome=gustavo&idade=28
    http://127.0.0.1:5000/?nome=gustavo
    http://127.0.0.1:5000/

    '''
    arg = request.args.to_dict()
    print(arg)

    if len(arg) == 0:
        return f"Message: Application executed successfully without parameters. arg pass in build {os.environ['projeto_id_gcp']}"
    elif len(arg) == 2 and 'nome' in arg.keys() and 'idade' in arg.keys():
        return f"Message: Application executed successfully with parameters. Two parameters: {arg}"
    elif len(arg) == 1 and 'nome' in arg.keys():
        return f"Message: Application executed successfully with parameters. One parameters: {arg}"
    else:   
        return f"Message: Not found parameter"
    # else:
    #     return f"Message: Application executed successfully with parameters. Parameters: {arg}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(8080))
