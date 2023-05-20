from behave import given, when, then
from selenium import webdriver
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given('I am on the Quran.com Surah page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://quran.com/1")

@then("Surah Name is Present")
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        name = context.browser.find_element(By.XPATH, "//span[normalize-space()='001']")
    
        assert True, "Name Present"
    except:
        assert False, "Name Missing" 

@then("Translator Name is Present")
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        translator = context.browser.find_element(By.XPATH, "//div[@class='ChapterHeader_translationBy__DDZAE'] ")
    
        assert True, "Translator Name Present"
    except:
        assert False, "Translator Name Missing" 

@then("Change Translator is Availabe")
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        change = context.browser.find_element(By.CLASS_NAME, "ChapterHeader_changeTranslation__UlDJ5")
    
        assert True, "Change Translator Name Present"
    except:
        assert False, "Change Translator Name Missing" 

@then("Surah Info is Present")
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        info = context.browser.find_element(By.XPATH, "//span[normalize-space()='Surah Info']")
    
        assert True, "Surah Info Name Present"
    except:
        assert False, "Surah Info Name Missing" 

@when("I Press Change Translation Button")
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        change = context.browser.find_element(By.CLASS_NAME, "ChapterHeader_changeTranslation__UlDJ5")
        change.click()
        assert True, "Change Translator Name Present"
    except:
        assert False, "Change Translator Name Missing" 

@then("The list of Translators is Given")
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        list = context.browser.find_element(By.XPATH, "//div[@class='SettingsDrawer_headerContainer__kJY4F']")
        assert True, "Change Translator List Present"
    except:
        assert False, "Change Translator List Missing" 

@when('I switch to "{tab}" in Surah Page')  
def step_impl(context, tab):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.presence_of_element_located(
            (By.XPATH, tab)))
    tab_element = context.browser.find_element(By.XPATH, tab)
    tab_element.click()


@then('the "{view}" is switched in Surah Page')
def step_impl(context, view):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, view)))
        assert True, "Tab Switched"
    except:
        assert False, "Tab Not Switched"
