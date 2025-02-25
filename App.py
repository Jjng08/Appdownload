from flask import Flask, render_template, request, jsonify
from model import descargar_reel
import os
from pathlib import Path

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/descargar', methods=['POST'])
def descargar():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'URL no proporcionada'}), 400

    # Crear carpeta para los reels
    output_path = str(Path.home() / "Downloads" / "InstagramReels")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    try:
        descargar_reel(url, output_path)
        return jsonify({'success': True, 'message': 'Reel descargado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)