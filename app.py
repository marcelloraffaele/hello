from flask import Flask, jsonify, request, send_from_directory, abort
import os
import datetime

app = Flask(__name__, static_folder='.', static_url_path='')

# Health flags (defaults: true)
is_ready = True
is_live = True
is_started = True

@app.route('/')
def root():
    color_mode = os.environ.get('COLOR_MODE', 'INDEX').upper()
    if color_mode == 'BLUE':
        filename = 'blue.html'
    elif color_mode == 'GREEN':
        filename = 'green.html'
    elif color_mode == 'MAINTENANCE':
        filename = 'maintenance.html'
    else:
        filename = 'index.html'
    return send_from_directory('./html', filename)

@app.route('/api/hello')
def api_hello():
    return jsonify({"message": "hello world"})

@app.route('/api/test')
def api_test():
    return jsonify({"message": "this is a test"})

@app.route('/api/version')
def api_version():
    return jsonify({"version": "1.1", "date": "20250617"})

@app.route('/api/time')
def api_time():
    now = datetime.datetime.now()
    return jsonify({
        "status": "success",
        "time": now.strftime('%a, %d %b %Y %H:%M:%S'),
        "msec": str(int(now.timestamp() * 1000))
    })

@app.route('/api/env')
def api_env():
    var_name = request.args.get('name')
    if not var_name:
        return jsonify({"error": "Missing name parameter"}), 400
    value = os.environ.get(var_name)
    return jsonify({"name": var_name, "value": value})

@app.route('/api/all-env')
def api_all_env():
    return jsonify(dict(os.environ))

@app.route('/api/headers')
def api_headers():
    return jsonify(dict(request.headers))

@app.route('/api/error')
def api_error():
    abort(500)

@app.route('/api/error401')
def api_error401():
    abort(401)

@app.route('/api/error403')
def api_error403():
    abort(403)


def _str_to_bool(s: str):
    if s is None:
        return None
    s = s.strip().lower()
    if s in ('1', 'true', 't', 'yes', 'y', 'on'):
        return True
    if s in ('0', 'false', 'f', 'no', 'n', 'off'):
        return False
    return None


@app.route('/liveness', methods=['GET'])
def get_liveness():
    # Per user's mapping: liveness -> is_ready
    if is_ready:
        return ('', 200)
    return ('', 500)


@app.route('/readiness', methods=['GET'])
def get_readiness():
    # Per user's mapping: readiness -> is_live
    if is_live:
        return ('', 200)
    return ('', 500)


@app.route('/started', methods=['GET'])
def get_started():
    if is_started:
        return ('', 200)
    return ('', 500)


@app.route('/liveness/<status>', methods=['POST'])
def post_liveness(status: str):
    global is_ready
    val = _str_to_bool(status)
    if val is None:
        return jsonify({'error': 'invalid status, use true/false'}), 400
    is_ready = val
    return jsonify({'liveness': is_ready})


@app.route('/readiness/<status>', methods=['POST'])
def post_readiness(status: str):
    global is_live
    val = _str_to_bool(status)
    if val is None:
        return jsonify({'error': 'invalid status, use true/false'}), 400
    is_live = val
    return jsonify({'readiness': is_live})


@app.route('/started/<status>', methods=['POST'])
def post_started(status: str):
    global is_started
    val = _str_to_bool(status)
    if val is None:
        return jsonify({'error': 'invalid status, use true/false'}), 400
    is_started = val
    return jsonify({'started': is_started})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
