# app.py
from flask import Flask, render_template, request
import requests
from collections import Counter
import datetime
import os


app = Flask(__name__)

API_URL = "https://kiwi-com-cheap-flights.p.rapidapi.com/one-way"

HEADERS = {
    "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"), 
    "x-rapidapi-host": "kiwi-com-cheap-flights.p.rapidapi.com"
}

@app.route('/', methods=['GET', 'POST'])
def home():
    flights = []
    insights = {}
    price_trend = []

    if request.method == 'POST':
        from_city = request.form.get('from_city', '').strip().upper()
        to_city = request.form.get('to_city', '').strip().upper()

        query = {
            "source": from_city,               
            "destination": to_city,
            "currency": "usd",
            "locale": "en",
            "adults": "1",
            "children": "0",
            "infants": "0",
            "handbags": "1",
            "holdbags": "0",
            "cabinClass": "ECONOMY",
            "sortBy": "QUALITY",
            "transportTypes": "FLIGHT",
            "limit": "20"
        }

        try:
            res = requests.get(API_URL, headers=HEADERS, params=query)
            data = res.json()
            itineraries = data.get('itineraries', [])

            for i in itineraries:
                try:
                    sector = i.get('sector', {})
                    segments = sector.get('sectorSegments', [])
                    if not segments:
                        continue

                    seg = segments[0].get('segment', {})
                    src = seg.get('source', {})
                    dst = seg.get('destination', {})
                    carrier = seg.get('carrier', {})

                    dep_time = src.get('utcTime', 'Unknown')
                    price_raw = i.get('price', {}).get('amount', 0)

                    try:
                        price = float(price_raw)
                    except:
                        price = 0.0

                    flight = {
                        'airline': carrier.get('name', 'Unknown'),
                        'flight_num': seg.get('code', 'NA'),
                        'from': src.get('station', {}).get('name', 'Unknown'),
                        'to': dst.get('station', {}).get('name', 'Unknown'),
                        'time': dep_time,
                        'price': price
                    }

                    flights.append(flight)

                    if flight['time'] != 'Unknown':
                        price_trend.append({'time': flight['time'], 'price': flight['price']})

                except Exception as e:
                    print("Parsing error:", e)
                    continue

            if flights:
                insights = {
                    'top_routes': Counter([(f['from'], f['to']) for f in flights]).most_common(5),
                    'avg_price': round(sum(f['price'] for f in flights) / len(flights), 2),
                    'peak_hours': Counter([
                        datetime.datetime.fromisoformat(f['time'].replace('Z', '+00:00')).hour
                        for f in flights if f['time'] != 'Unknown'
                    ]).most_common(3)
                }

        except Exception as e:
            print("API error:", e)

    return render_template('index.html', flights=flights, insights=insights, price_trend=price_trend)

