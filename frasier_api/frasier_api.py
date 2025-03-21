from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# In-memory storage for quotes
quotes = {
    1: {"quote": "I'm listening.", "speaker": "Frasier"},
    2: {"quote": "You may be a psychiatrist, but I’m the one with style.", "speaker": "Niles"},
    3: {"quote": "Hey baby, I hear the blues a-callin'.", "speaker": "Frasier"},
    4: {"quote": "Once a cop, always a cop!", "speaker": "Martin"},
    5: {"quote": "You're not just a snob, you're a snob-snob!", "speaker": "Roz"}
}

@app.route('/quotes', methods=['GET'])
def get_quotes():
    """
    Get all Frasier quotes, optionally filter by speaker
    ---
    parameters:
      - name: speaker
        in: query
        type: string
        required: false
        description: Speaker to filter by (e.g., Frasier, Niles)
    responses:
      200:
        description: A list of quotes
    """
    speaker = request.args.get('speaker')
    if speaker:
        filtered = {k: v for k, v in quotes.items() if v['speaker'].lower() == speaker.lower()}
        return jsonify({"quotes": filtered})
    return jsonify({"quotes": quotes})

@app.route('/quotes', methods=['POST'])
def add_quote():
    """
    Add a new Frasier quote
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
    new_id = max(quotes.keys()) + 1
    quotes[new_id] = {
        "quote": data["quote"],
        "speaker": data["speaker"]
    }
    return jsonify({"id": new_id, "quote": quotes[new_id]}), 201

@app.route('/quotes/<int:quote_id>', methods=['PUT'])
def update_quote(quote_id):
    """
    Update an existing quote
    ---
    parameters:
      - name: quote_id
        in: path
        type: integer
        required: true
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
      200:
        description: Quote updated
    """
    data = request.get_json()
    quotes[quote_id] = {
        "quote": data.get("quote", "No quote provided"),
        "speaker": data.get("speaker", "Unknown")
    }
    return jsonify({"message": "Quote updated", "quote": quotes[quote_id]})

@app.route('/quotes/<int:quote_id>', methods=['DELETE'])
def delete_quote(quote_id):
    """
    Delete a quote
    ---
    parameters:
      - name: quote_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Quote deleted
    """
    if quote_id in quotes:
        deleted_quote = quotes.pop(quote_id)
        return jsonify({"message": f"Deleted: {deleted_quote['quote']} - {deleted_quote['speaker']}"})
    return jsonify({"message": "Quote not found."}), 404

if __name__ == '__main__':
    app.run(port=2224, host="0.0.0.0", debug=True)

