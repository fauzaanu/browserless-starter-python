from playwright.sync_api import sync_playwright

with sync_playwright() as p:
  browser = p.firefox.connect('ws://localhost:3000/firefox/playwright')
  context = browser.new_context()
  page = context.new_page()
  page.goto('http://www.example.com', wait_until='domcontentloaded')
  print(page.content())
  context.close()