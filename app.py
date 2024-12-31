from flask import Flask, request, jsonify

app = Flask(__name__)

def validate_json(data, optional_fields=None):

    invalid_fields = []
    optional_fields = optional_fields or set()

    def check_field(value, path):
        """Recursive helper function to check fields."""
        if value is None:
            # Add to invalid fields if not in optional fields
            if path not in optional_fields:
                invalid_fields.append(path)
        elif isinstance(value, dict):
            # Recursively check dictionary fields
            for key, val in value.items():
                check_field(val, f"{path}.{key}" if path else key)
        elif isinstance(value, list):
            # Recursively check list elements
            for index, item in enumerate(value):
                check_field(item, f"{path}[{index}]" if path else f"[{index}]")

    # Start validation from the root
    check_field(data, "")

    if invalid_fields:
        return {"status": "error", "invalid_fields": invalid_fields}
    return {"status": "success"}

@app.route('/validate', methods=['POST'])
def validate():
    try:
        # Get JSON data from request
        data = request.get_json()
        if data is None:
            return jsonify({"status": "error", "message": "Invalid JSON input."}), 400

        # Optional fields can be passed as a query parameter, comma-separated
        optional_fields_param = request.args.get('optional_fields', '')
        optional_fields = set(optional_fields_param.split(',')) if optional_fields_param else set()

        # Validate JSON
        result = validate_json(data, optional_fields=optional_fields)
        return jsonify(result)

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
    