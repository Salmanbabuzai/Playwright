import re
import time
from playwright.sync_api import Playwright, Page, expect

import data
from data import *

def test_sign_Up(page: Page):
    page.goto(url, timeout=0)

    #Sign-up icon
    page.locator("//li[@class='authorization-link']").click(timeout=300000)

    #Click on Register button
    page.get_by_text("Register").nth(1).click()

    #Registration form
    page.locator("//input[@id='firstname']").fill(first_name)
    page.locator("//input[@id='lastname']").fill(last_name)
    page.locator("//input[@id='email_address']").fill(sign_up_email)
    page.locator("//input[@id='password']").fill(password)
    page.locator("//input[@id='password-confirmation']").fill(confirm_password)
    page.get_by_text("Register").nth(1).click()

    #Validate My Dashobard
    expect(page.locator("//span[@class='base']")).to_have_text("My Dashboard")