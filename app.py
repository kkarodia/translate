from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator
import os

app = Flask(__name__)
CORS(app)

@app.route('/translate/to-arabic', methods=['POST'])
def translate_to_arabic():
    # Get data from request
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'Please provide text to translate'}), 400
    
    text_to_translate = data['text']
    
    # Initialize translator
    translator = Translator()
    
    try:
        # Translate to Arabic
        translation = translator.translate(text_to_translate, dest='ar')
        
        # Prepare response
        response = {
            'original': text_to_translate,
            'translated': translation.text,
            'source_language': translation.src,
            'target_language': 'ar'
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': f'Translation error: {str(e)}'}), 500

@app.route('/translate/to-english', methods=['POST'])
def translate_to_english():
    # Get data from request
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'Please provide text to translate'}), 400
    
    text_to_translate = data['text']
    
    # Initialize translator
    translator = Translator()
    
    try:
        # Translate to English
        translation = translator.translate(text_to_translate, dest='en')
        
        # Prepare response
        response = {
            'original': text_to_translate,
            'translated': translation.text,
            'source_language': translation.src,
            'target_language': 'en'
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': f'Translation error: {str(e)}'}), 500

@app.route('/translate', methods=['POST'])
def translate_generic():
    # Get data from request
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'Please provide text to translate'}), 400
    
    text_to_translate = data['text']
    source_lang = data.get('source', 'auto')
    target_lang = data.get('target', 'en')
    
    # Initialize translator
    translator = Translator()
    
    try:
        # Translate text
        translation = translator.translate(text_to_translate, src=source_lang, dest=target_lang)
        
        # Prepare response
        response = {
            'original': text_to_translate,
            'translated': translation.text,
            'source_language': translation.src,
            'target_language': target_lang
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': f'Translation error: {str(e)}'}), 500

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'service': 'Translation API',
        'endpoints': {
            '/translate/to-arabic': 'Translates text to Arabic',
            '/translate/to-english': 'Translates text to English',
            '/translate': 'Generic translation with source and target language parameters'
        },
        'usage': {
            'to-arabic': 'POST /translate/to-arabic with JSON body {"text": "your text here"}',
            'to-english': 'POST /translate/to-english with JSON body {"text": "نص باللغة العربية"}',
            'generic': 'POST /translate with JSON body {"text": "your text", "source": "auto", "target": "fr"}'
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
