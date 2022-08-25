class AcceptButton:

    def __init__(self, page):
        self.accept_button = page.locator("button[id='onetrust-accept-btn-handler']")

class CookieBanner:

    def __init__(self, page):
        self.banner = page.locator("div[id='onetrust-banner-sdk']")
        self.accept_button = AcceptButton(page)
    
    def consent_to_cookies(self):
        self.accept_button.click()