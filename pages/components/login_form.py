class EmailField:

    def __init__(self, page):
        self.email_field = page.locator("input[data-qa='email']")

class PasswordField:

    def __init__(self, page):
        self.password_field = page.locator("input[data-qa='password']")

class SignInButton:

    def __init__(self, page):
        self.sign_in_button = page.locator("button[data-qa='log-in']")