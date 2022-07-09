
import re
import time

from urlwatch import filters
from urlwatch import jobs
from urlwatch import reporters
from playwright.sync_api import sync_playwright


class BrowserJS(jobs.UrlJob):
    """Custom login for my webpage test"""

    __kind__ = 'browser-js'
    __optional__ = ('script',)

    def get_location(self):
        return self.url

    def retrieve(self, job_state):
        with sync_playwright() as p:

            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(self.url)

            if self.script != None:
                page.evaluate(self.script)
            html = page.content()
            browser.close()

        return html


