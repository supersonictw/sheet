from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


class MySelf:
    def __init__(self, processEngine):
        self.processEngine = processEngine

    def address(self):
        self.processEngine.get("https://bgp.he.net/")
        page = bs(self.processEngine.page_source, "html.parser")
        data = page.find(
            "a", class_="boldlink"
        ).get("href").replace("/ip/", "")
        return data


class MainObject:
    def __init__(self, path="./phantomjs"):
        useragent = UserAgent()
        useragent.update()
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap['phantomjs.page.settings.userAgent'] = useragent.random
        self.processEngine = webdriver.PhantomJS(
            executable_path=path, desired_capabilities=dcap
        )
        self.myself = MySelf(self.processEngine)
