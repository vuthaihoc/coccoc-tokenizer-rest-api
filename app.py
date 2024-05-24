from flask import Flask, request

import sys
sys.path.append('/app/coccoc-tokenizer/build/python/lib/python3.12/site-packages/CocCocTokenizer-1.4-py3.12-linux-x86_64.egg')

from CocCocTokenizer import PyTokenizer

app = Flask(__name__)
T = PyTokenizer(load_nontone_data=True)

@app.route('/')
def hello():
	# return "HHHH"
	return T.word_tokenize("xin chào, tôi là người Việt Nam", tokenize_option=0)

@app.route('/tokenize')
def tokenize():
	text = request.args['text']
	return T.word_tokenize(text, tokenize_option=0)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)