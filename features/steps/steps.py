from behave import given, when, then
from selenium import webdriver
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Helper function to write results to PDF
def write_to_pdf(content):
    c = canvas.Canvas("test_results.pdf", pagesize=letter)
    width, height = letter
    c.drawString(100, height - 100, "Test Results")
    y = height - 150
    for line in content:
        c.drawString(100, y, line)
        y -= 20
    c.save()

@given('I am on the clinical records search page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('http://localhost:5000/buscar_historia')  # Cambiar la URL al entorno correcto
    context.test_results = ["Given I am on the clinical records search page"]

@when('I enter the ID "{id}"')
def step_impl(context, id):
    context.driver.find_element_by_name('cedula').send_keys(id)
    context.test_results.append(f'When I enter the ID "{id}"')

@when('I click the search button')
def step_impl(context):
    context.driver.find_element_by_xpath('//button[@type="submit"]').click()
    context.test_results.append("And I click the search button")

@then('I should see the clinical record')
def step_impl(context):
    try:
        context.driver.find_element_by_id('record')
        context.test_results.append("Then I should see the clinical record")
        context.test_results.append("Test passed")
    except:
        context.test_results.append("Then I should see the clinical record")
        context.test_results.append("Test failed")
    finally:
        write_to_pdf(context.test_results)
        context.driver.quit()

@then('I should see an error message')
def step_impl(context):
    try:
        context.driver.find_element_by_id('error_message')
        context.test_results.append("Then I should see an error message")
        context.test_results.append("Test passed")
    except:
        context.test_results.append("Then I should see an error message")
        context.test_results.append("Test failed")
    finally:
        write_to_pdf(context.test_results)
        context.driver.quit()