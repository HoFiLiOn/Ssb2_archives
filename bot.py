from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TOKEN = "8786399001:AAF2GODnsIrCluHiFPH8XYC8uVMuPrDiSss"
CHAT_ID = "7040677455"

@app.route('/send_reaction', methods=['POST'])
def send_reaction():
    data = request.get_json()
    tab = data.get('tab', 'неизвестно')
    reaction = data.get('reaction', 'неизвестно')
    time = data.get('time', '')
    
    reaction_emoji = {'useful': '👍', 'neutral': '😐', 'outdated': '👎'}.get(reaction, '')
    
    text = f"📊 Реакция: {reaction_emoji}\nВкладка: {tab}\nВремя: {time}"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={'chat_id': CHAT_ID, 'text': text})
    
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)