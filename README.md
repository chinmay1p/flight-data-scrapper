# ✈️ Flight Data Viewer

## 📖 Description
This is a simple web app built with Flask and Chart.js that allows users to explore airline demand and pricing trends between two airports using live flight data from the Kiwi RapidAPI. It is useful for market research, dynamic pricing analysis, or just general travel planning insights.
Live demo - 
---

## 🚀 Features
- 🔍 Search flights by entering source and destination IATA codes (e.g., DEL → BOM)
- 📋 View flight details like airline, number, departure/arrival time, and price
- 📊 See price trends over time using an interactive line chart
- 📈 Insights like:
  - Top 5 most common routes
  - Average ticket price
  - Peak demand hours

---

## 🛠️ Tech Used
- **Flask** – For backend routing and logic
- **Jinja2** – For dynamic HTML rendering
- **HTML/CSS** – For frontend layout and form
- **Chart.js** – To visualize price trends
- **Kiwi.com RapidAPI** – To fetch real-time flight data

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/chinmay1p/flight-data-scrapper.git
   cd air-demand-viewer
   ```
2. ```
   pip install flask requests
   ```
3. Set your RapidAPI Key
   Open app.py
   Replace "YOUR_API_KEY_HERE" with your actual RapidAPI key
4. Run app.py
   ```bash
   python app.py
   ```
5. Visit - http://localhost:5000

---

## ScreenShots

![image](https://github.com/user-attachments/assets/c20cd6bc-7acf-4dc4-a5e0-4c26aa281e36)

![image](https://github.com/user-attachments/assets/3223487b-a2fb-47f1-83f2-c2a176f06309)

![image](https://github.com/user-attachments/assets/149fe2e3-5714-42f3-9959-4a7963c83245)


