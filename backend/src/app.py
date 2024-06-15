# src/app.py
from flask import Flask, jsonify
from config import db
from data_processor import process_and_save_restaurant_data

app = Flask(__name__)

@app.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = list(db.restaurants.find({}, {'_id': 0}))
    return jsonify(restaurants)

if __name__ == '__main__':
    location = '40.748817,-73.985428'  # 设置你想要搜索的地理位置
    radius = 5000  # 设置搜索半径
    keyword = None  # 你可以设置关键词进行更精细的搜索

    print("Starting Flask app...")
    process_and_save_restaurant_data(location, radius, keyword)
    app.run(debug=True, port=5001)