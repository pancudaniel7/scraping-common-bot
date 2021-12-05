from selenium import webdriver


def new_session(log_level: str, firefox_headless: bool):
    options = webdriver.FirefoxOptions()
    options.log.level = log_level

    if firefox_headless is True: options.add_argument('--headless')

    return webdriver.Firefox(options=options)
