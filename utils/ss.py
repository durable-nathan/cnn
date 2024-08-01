from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time
import base64

html_header = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tailwind CSS Example</title>
    <!-- Tailwind CSS CDN -->
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body>"""
html_footer = "</body></html>"

def take_screenshot(html, filename, output_dir, width=1400, height=720):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Set up Selenium with Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless Chrome
    chrome_options.add_argument(f"--window-size={width},{height}")
    
    # Set up the webdriver
    service = Service('/usr/local/bin/chromedriver')  # Replace with the path to your chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    html = html_header + html + html_footer

    # Convert the HTML string to a data URL
    data_url = f"data:text/html;base64,{base64.b64encode(html.encode('utf-8')).decode('utf-8')}"
    
    # Open the HTML content in the browser
    driver.get(data_url)
    time.sleep(1)  # Give time for the page to load

    # Take a screenshot
    screenshot_path = os.path.join(output_dir, filename)
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

    # Clean up
    driver.quit()


#html_string = """<section class="h-screen p-8 bg-yellow-500">\n  <nav class="flex justify-between py-3 bg-pink-600 shadow-lg">\n    <div class="text-3xl text-white ml-5">Logo</div>\n    <ul class="flex space-x-3 mr-5 text-xl text-gray-900">\n      <li>Home</li>\n      <li>About</li>\n      <li>Contact</li>\n    </ul>\n  </nav>\n  \n  <div class="flex flex-col md:flex-row justify-start items-center h-full">\n    <div class="flex-1 p-6">\n      <h1 class="text-7xl font-bold text-gray-50 leading-tight mb-1">Welcome</h1>\n      <p class="text-base text-green-900 leading-loose mb-8">This is the hero section with an image on the right. Everything here is poorly designed to showcase what NOT to do in a website layout.</p>\n      <button class="bg-gray-900 text-sm text-yellow-200 px-4 py-2 border-green-500 border-4 rounded">Click Me!</button>\n    </div>\n    \n    <div class="flex-1 m-10">\n      <img src="https://via.placeholder.com/400" alt="Placeholder Image" class="rounded shadow-lg">\n    </div>\n  </div>\n</section>"""
#take_screenshot(html_string, "screenshot.png", "screenshots")
