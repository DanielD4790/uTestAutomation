from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="-WwFSS9thvXwoEwiyYM21qnKS8Qm44o-mBFuezZjE3g1",
                              project_name="AutomatedOwns",
                              job_name="Join")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Diligenciamiento de formulario de acceso, para crear un nuevo usuario."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://utest.com/"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'Join Today'
    join_today = driver.find_element(By.XPATH,
                                     "//li[2]/a[. = 'Join Today']")
    join_today.click()

    # 3. Click 'firstName'
    firstname = driver.find_element(By.CSS_SELECTOR,
                                    "#firstName")
    firstname.click()

    # 4. Type 'Jose' in 'firstName'
    firstname = driver.find_element(By.CSS_SELECTOR,
                                    "#firstName")
    firstname.send_keys("Jose")

    # 5. Click 'lastName'
    lastname = driver.find_element(By.CSS_SELECTOR,
                                   "#lastName")
    lastname.click()

    # 6. Type 'Dominguez' in 'lastName'
    lastname = driver.find_element(By.CSS_SELECTOR,
                                   "#lastName")
    lastname.send_keys("Dominguez")

    # 7. Click 'email'
    email = driver.find_element(By.CSS_SELECTOR,
                                "#email")
    email.click()

    # 8. Type 'dnl.47@hotmail.com' in 'email'
    email = driver.find_element(By.CSS_SELECTOR,
                                "#email")
    email.send_keys("vrk.dom@gmail.com")

    # 9. Click 'birthMonth'
    birthmonth = driver.find_element(By.CSS_SELECTOR,
                                     "#birthMonth")
    birthmonth.click()

    # 10. Select the 'number:7' option in 'birthMonth'
    birthmonth = driver.find_element(By.CSS_SELECTOR,
                                     "#birthMonth")
    Select(birthmonth).select_by_value("number:7")

    # 11. Click 'birthMonth'
    birthmonth = driver.find_element(By.CSS_SELECTOR,
                                     "#birthMonth")
    birthmonth.click()

    # 12. Click 'birthDay'
    birthday = driver.find_element(By.CSS_SELECTOR,
                                   "#birthDay")
    birthday.click()

    # 13. Select the 'number:4' option in 'birthDay'
    birthday = driver.find_element(By.CSS_SELECTOR,
                                   "#birthDay")
    Select(birthday).select_by_value("number:4")

    # 14. Click 'birthDay'
    birthday = driver.find_element(By.CSS_SELECTOR,
                                   "#birthDay")
    birthday.click()

    # 15. Click 'birthYear'
    birthyear = driver.find_element(By.CSS_SELECTOR,
                                    "#birthYear")
    birthyear.click()

    # 16. Select the 'number:1990' option in 'birthYear'
    birthyear = driver.find_element(By.CSS_SELECTOR,
                                    "#birthYear")
    Select(birthyear).select_by_value("number:1990")

    # 17. Click 'birthYear'
    birthyear = driver.find_element(By.CSS_SELECTOR,
                                    "#birthYear")
    birthyear.click()

    # 18. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/div/input")
    input.click()

    # 19. Click 'Spanish'
    spanish = driver.find_element(By.XPATH,
                                  "//div[. = 'Spanish']")
    spanish.click()

    # 20. Is 'Next: Location chevron_right' present?
    next_colon_location_chevron_right = driver.find_element(By.XPATH,
                                                            "//a[. = '\n        Next: Location\n        chevron_right\n      ']")

    # 21. Is 'Next: Location chevron_right' is clickable?
    next_colon_location_chevron_right = driver.find_element(By.XPATH,
                                                            "//a[. = '\n        Next: Location\n        chevron_right\n      ']")
    assert next_colon_location_chevron_right.is_enabled()

    # 22. Click 'Next: Location chevron_right'
    next_colon_location_chevron_right = driver.find_element(By.XPATH,
                                                            "//a[. = '\n        Next: Location\n        chevron_right\n      ']")
    next_colon_location_chevron_right.click()

    # 23. Click 'city'
    city = driver.find_element(By.CSS_SELECTOR,
                               "#city")
    city.click()

    # 24. Type 'Arraiján' in 'city'
    #city = driver.find_element(By.CSS_SELECTOR,
                               #"#city")
    #city.send_keys("Arraiján")

    # 25. Click 'zip'
    zip = driver.find_element(By.CSS_SELECTOR,
                              "#zip")
    zip.click()

    # 26. Type '50710' in 'zip'
    zip = driver.find_element(By.CSS_SELECTOR,
                              "#zip")
    zip.send_keys("50710")

    # 27. Click 'SPAN'
    span = driver.find_element(By.XPATH,
                               "//div[4]/div[2]/div/div/div/span")
    span.click()

    # 28. Click 'Panama'
    panama = driver.find_element(By.XPATH,
                                 "//span[. = '\n                    Panama\n                  ']")
    panama.click()

    # 29. Is 'Next: Devices chevron_right' present?
    next_colon_devices_chevron_right = driver.find_element(By.XPATH,
                                                           "//a[. = '\n          Next: Devices\n          chevron_right\n        ']")

    # 30. Is 'Next: Devices chevron_right' is clickable?
    next_colon_devices_chevron_right = driver.find_element(By.XPATH,
                                                           "//a[. = '\n          Next: Devices\n          chevron_right\n        ']")
    assert next_colon_devices_chevron_right.is_enabled()

    # 31. Click 'Next: Devices chevron_right'
    next_colon_devices_chevron_right = driver.find_element(By.XPATH,
                                                           "//a[. = '\n          Next: Devices\n          chevron_right\n        ']")
    next_colon_devices_chevron_right.click()

    # 32. Click 'SPAN1'
    span1 = driver.find_element(By.XPATH,
                                "//div[2]/div[1]/div[2]/div/div/span")
    span1.click()

    # 33. Click 'Oppo'
    oppo = driver.find_element(By.XPATH,
                               "//span[. = '\n                Oppo\n              ']")
    oppo.click()

    # 34. Click 'SPAN2'
    span2 = driver.find_element(By.XPATH,
                                "//div[2]/div[2]/div[2]/div/div/span")
    span2.click()

    # 35. Click 'Reno'
    reno = driver.find_element(By.XPATH,
                               "//span[. = '\n                Reno\n              ']")
    reno.click()

    # 36. Click 'SPAN3'
    span3 = driver.find_element(By.XPATH,
                                "//div[2]/div[3]/div[2]/div/div/span")
    span3.click()

    # 37. Click 'Android 10'
    android_10 = driver.find_element(By.XPATH,
                                     "//span[. = '\n                Android 10\n              ']")
    android_10.click()

    # 38. Is 'Next: Last Step chevron_right' present?
    next_colon_last_step_chevron_right = driver.find_element(By.XPATH,
                                                             "//a[. = '\n        Next: Last Step\n        chevron_right\n      ']")

    # 39. Is 'Next: Last Step chevron_right' is clickable?
    next_colon_last_step_chevron_right = driver.find_element(By.XPATH,
                                                             "//a[. = '\n        Next: Last Step\n        chevron_right\n      ']")
    assert next_colon_last_step_chevron_right.is_enabled()

    # 40. Click 'Next: Last Step chevron_right'
    next_colon_last_step_chevron_right = driver.find_element(By.XPATH,
                                                             "//a[. = '\n        Next: Last Step\n        chevron_right\n      ']")
    next_colon_last_step_chevron_right.click()

    # 41. Type 'Test_pw2022' in 'password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#password")
    password.send_keys("Test_pw2022")

    # 42. Click 'confirmPassword'
    confirmpassword = driver.find_element(By.CSS_SELECTOR,
                                          "#confirmPassword")
    confirmpassword.click()

    # 43. Click 'confirmPassword'
    confirmpassword = driver.find_element(By.CSS_SELECTOR,
                                          "#confirmPassword")
    confirmpassword.click()

    # 44. Type 'Test_pw2022' in 'confirmPassword'
    confirmpassword = driver.find_element(By.CSS_SELECTOR,
                                          "#confirmPassword")
    confirmpassword.send_keys("Test_pw2022")

    # 45. Click 'SPAN4'
    span4 = driver.find_element(By.XPATH,
                                "//div[4]/label/span")
    span4.click()

    # 46. Click 'SPAN5'
    span5 = driver.find_element(By.XPATH,
                                "//div[5]//span[1]")
    span5.click()

    # 47. Click 'SPAN6'
    span6 = driver.find_element(By.XPATH,
                                "//div[6]//span[1]")
    span6.click()

    # 48. Is 'Complete Setup chevron_right' present?
    complete_setup_chevron_right = driver.find_element(By.CSS_SELECTOR,
                                                       "#laddaBtn")

    # 49. Is 'Complete Setup chevron_right' is clickable?
    complete_setup_chevron_right = driver.find_element(By.CSS_SELECTOR,
                                                       "#laddaBtn")
    assert complete_setup_chevron_right.is_enabled()

    # 50. Click 'Complete Setup chevron_right'
    complete_setup_chevron_right = driver.find_element(By.CSS_SELECTOR,
                                                       "#laddaBtn")
    complete_setup_chevron_right.click()

    # 51. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 52. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 53. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 54. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 55. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 56. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 57. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 58. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 59. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 60. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")
