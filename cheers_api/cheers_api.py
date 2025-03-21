from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Simple in-memory storage for Cheers quotes
cheers_quotes = {
     1: {"quote": "It's a dog eat dog world, and I'm wearing Milk-Bone underwear.", "speaker": "Norm"},
     2: {"quote": "Women. You can't live with 'em, pass the beer nuts.", "speaker": "Norm"},
     3: {"quote": "How’s life treating you, Norm? Like it caught me sleeping with its wife.", "speaker": "Norm"}
}

@app.route('/cheers', methods=['GET'])
def get_cheers_quotes():
     return jsonify({"quotes": cheers_quotes})

@app.route('/cheers', methods=['POST'])
def add_cheers_quote():
     """
     Add a new Cheers quote
     ---
     parameters:
       - name: body
         in: body
         required: true
         schema:
           type: object
           properties:
             quote:
               type: string
             speaker:
               type: string
     responses:
       201:
         description: Quote added
     """

     data = request.get_json()
     new_id = max(cheers_quotes.keys()) + 1
     cheers_quotes[new_id] = {"quote": data["quote"], "speaker": data["speaker"]}
     return jsonify({"id": new_id, "quote": cheers_quotes[new_id]}), 201

if __name__ == '__main__':
   app.run(port=2224, host="0.0.0.0", debug=True)


