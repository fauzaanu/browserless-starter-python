### Browserless starter in python

This is a browserless starter in python. 

1. Run Docker browserless

```bash
docker run -d -p 3000:3000 ghcr.io/browserless/firefox
```

2. In your code reference the browserless url

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
  browser = p.firefox.connect('ws://localhost:3000/firefox/playwright')
  context = browser.new_context()
  page = context.new_page()
  page.goto('http://www.example.com', wait_until='domcontentloaded')
  print(page.content())
  context.close()
```