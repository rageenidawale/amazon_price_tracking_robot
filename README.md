# 🛒 Amazon Price Tracker  

## 📌 Overview  
This project **scrapes** Amazon product prices and sends an **email alert** when the price drops below a target value.  

## 🚀 Features  
- 🌐 **Web Scraping** - Uses `BeautifulSoup` to extract product prices.  
- 📩 **Email Notifications** - Sends an alert via SMTP when the price falls below the set threshold.  
- 🔄 **Automated Monitoring** - Can be scheduled to run at regular intervals using a task scheduler.  

## 🛠️ Technologies Used  
- **Python** 🐍  
- **Requests** 🌐 (to fetch Amazon product page)  
- **BeautifulSoup** 🏗️ (for web scraping)  
- **SMTP** 📧 (for email alerts)  

## 📜 How to Run  
1. Clone the repository:  
   ```
   git clone https://github.com/your-username/amazon-price-tracker.git
   ```
2. Install dependencies:  
   ```
   pip install requests beautifulsoup4
   ```
3. Update the script with your details:  
   - Set `my_email` and `my_password` for sending emails.  
   - Set `senders_email` for receiving alerts.  
   - Update `product_link` with the **Amazon product URL**.  
   - Adjust `target_price` as needed.  

4. Run the script:  
   ```
   python amazon_price_tracker.py
   ```
5. **Automate the script** (optional):  
   - Use **Windows Task Scheduler** or **cron jobs** to run it at regular intervals.  

## ⚠️ Bypassing CAPTCHA Verification  
If you encounter a CAPTCHA check, you can bypass it by manually setting the cookie value from your own browser in the headers:

1. Go to the Amazon website and open Developer Tools (**F12** or **Right-click → Inspect**).
2. Refresh the page.
3. Navigate to the **Application** tab.
4. Under **Storage**, open **Cookies**, then click on `https://amazon.com`.
5. Right-click on a cookie and select **Show requests with this cookie**.
6. Click on one of the requests, then under the **Headers** tab, locate **Request Headers**.
7. Copy the **Cookie** value and use it in your script headers.
   
## 🎯 Future Enhancements  
- 📊 **Price History Tracking** - Store price changes over time in a CSV file.  
- 📱 **Mobile Notifications** - Send alerts via Telegram or WhatsApp.  
- 🔄 **Multi-Product Tracking** - Monitor multiple products at once.  
- 🌍 **Multi-Region Support** - Extend tracking to other Amazon country domains.  
