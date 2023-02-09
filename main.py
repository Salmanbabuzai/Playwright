import re
import time
from playwright.sync_api import Playwright, Page, expect
from data import *


def test_order_place(page: Page):
    page.goto(url, timeout=0)
    #Search for Crep
    page.get_by_placeholder("Search").fill(search_item)
    page.get_by_role("heading", name="Crep Protect").nth(1).click()

    #Select Size
    page.locator("span.attribute-options").click()

    #Add to Bag
    page.get_by_title("Add to Bag").nth(0).click()

    #Open new Tab
    Tab = page.context.new_page()
    Tab.goto(url + "/cart/")
    time.sleep(2)
    Tab.reload()

    #Verify Title
    expect(Tab.get_by_text("Shopping bag"))

    #Secure Checkout
    Tab.get_by_text("Secure Checkout").click()

    #Checkout Form
    Tab.locator("#email").fill(email)
    Tab.locator("#firstname").fill(first_name)
    Tab.locator("#lastname").fill(last_name)
    Tab.locator("#phoneNumber").fill(phone)

    Tab.locator("//select[@name='city']").select_option(city)

    Tab.locator("#address1").fill(address1)

    #Tab.locator("//button[4]").click()
    #Tab.get_by_text("18:00 - 22:00").click()

    Tab.get_by_text("Review and pay").click()

    #Checkout Payment by COD
    Tab.get_by_text("Cash on Delivery").click()

    Tab.get_by_text("Place order").click()

    #Get ORDERID
    OrderID = Tab.locator("//p[@class='mb-4']/span[@class='font-medium']").inner_text()
