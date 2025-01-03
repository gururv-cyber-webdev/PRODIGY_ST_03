from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Set up Chrome options
chrome_options = Options()

# Set up the ChromeDriver service
service = Service(executable_path=r"C:\\Users\\ADMIN\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

# Start the driver with options
driver = webdriver.Chrome(service=service, options=chrome_options)

def login(username, password):
    """Logs into the application."""
    print(f"Navigating to login page...")
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    print(f"Entering username: '{username}'")
    driver.find_element(By.ID, "user-name").send_keys(username)
    time.sleep(1)

    print(f"Entering password: '{password}'")
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)

    print("Clicking login button...")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

def test_login():
    """Tests various login scenarios."""

    # Case 1: Valid username, valid password
    """Test Case 1: Valid username and password for 'standard_user'."""
    print("\n--- Test Case 1: Valid username and password ---")
    
    login("standard_user", "secret_sauce")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        print("No error message displayed. Login successful ✅.")
    except TimeoutException:
        print("❌ Login failed: Inventory container not found.")
    driver.refresh()
    time.sleep(2)



    """Test Case 2: Valid username and password for 'problem_user'."""
    print("\n--- Test Case 2: Valid username and password ---")
    
    login("problem_user", "secret_sauce")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        print("No error message displayed. Login successful ✅.")
    except TimeoutException:
        print("❌ Login failed: Inventory container not found.")
    driver.refresh()
    time.sleep(2)



    """Test Case 3: Valid username and password for 'performance_glitch_user'."""
    print("\n--- Test Case 3: Valid username and password ---")
   
    login("performance_glitch_user", "secret_sauce")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        print("No error message displayed. Login successful ✅.")
    except TimeoutException:
        print("❌ Login failed: Inventory container not found.")
    driver.refresh()
    time.sleep(2)



    """Test Case 4: Valid username and password for 'error_user'."""
    print("\n--- Test Case 4: Valid username and password ---")
    
    login("error_user", "secret_sauce")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        print("No error message displayed. Login successful ✅.")
    except TimeoutException:
        print("❌ Login failed: Inventory container not found.")
    driver.refresh()
    time.sleep(2)



    """Test Case 5: Valid username and password for 'visual_user'."""
    print("\n--- Test Case 5: Valid username and password ---")
    
    login("visual_user", "secret_sauce")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        print("No error message displayed. Login successful ✅.")
    except TimeoutException:
        print("❌ Login failed: Inventory container not found.")
    driver.refresh()
    time.sleep(2)



    # Case 2: Invalid username, valid password
    print("\n--- Test Case 6: Invalid username, valid password ---")
    driver.refresh()
    time.sleep(2)
    login("invalid_user", "secret_sauce")
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message: {error_message}")
        assert "Epic sadface" in error_message, "Error message not displayed for invalid username"
    except TimeoutException:
        print("No error message displayed.")

    # Case 3: Empty username, valid password
    print("\n--- Test Case 7: Empty username, valid password ---")
    driver.refresh()
    time.sleep(2)
    login("", "secret_sauce")
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message: {error_message}")
        assert "Username is required" in error_message, "Error message not displayed for empty username"
    except TimeoutException:
        print("No error message displayed.")

    # Case 4: Valid username, empty password
    print("\n--- Test Case 8: Valid username, empty password ---")
    driver.refresh()
    time.sleep(2)
    login("standard_user", "")
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message: {error_message}")
        assert "Password is required" in error_message, "Error message not displayed for empty password"
    except TimeoutException:
        print("No error message displayed.")

    # Case 5: Both username and password empty
    print("\n--- Test Case 9: Both username and password empty ---")
    driver.refresh()
    time.sleep(2)
    login("", "")
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message: {error_message}")
        assert "Username is required" in error_message, "Error message not displayed for both fields empty"
    except TimeoutException:
        print("No error message displayed.")

    # Case 6: Locked-out user
    print("\n--- Test Case 10: Locked-out user ---")
    driver.refresh()
    time.sleep(2)
    login("locked_out_user", "secret_sauce")
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message: {error_message}")
        assert "Epic sadface: Sorry, this user has been locked out." in error_message, "Error message not displayed for locked-out user"
    except TimeoutException:
        print("No error message displayed.")

   # Additional test cases
    """Test SQL Injection."""
    print("\n--- Test Case 11: Testing SQL Injection ---")
    login("' OR '1'='1", "anything")
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
	).text
        print(f"Error message displayed: {error_message}. Test successful: SQL Injection blocked ✅.")
    except TimeoutException:
        print("❌ Test failed: SQL Injection not blocked! Potential vulnerability detected.")

    """Test special characters."""
    print("\n--- Test Case 12: Testing special characters ---")
    login("@#$%^&*", "()<>?/{}")
    try:
        error_message = WebDriverWait(driver, 10).until(
	    EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message displayed: {error_message}. Test successful: Special characters blocked ✅.")
    except TimeoutException:
        print("❌ Test failed: Special characters not blocked! Potential vulnerability detected.")

    """Test excessively long inputs."""
    print("\n--- Test Case 13: Testing excessively long inputs ---")
    login("a" * 1000, "b" * 1000)
    try:
        error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message displayed: {error_message}. Test successful: Long inputs blocked ✅.")
    except TimeoutException:
        print("❌ Test failed: Long inputs not blocked! Potential vulnerability detected.")

    """Test whitespace inputs."""
    print("\n--- Test Case 14: Testing whitespace inputs ---")
    login(" ", " ")
    try:
        error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message displayed: {error_message}. Test successful: Whitespace inputs blocked ✅.")
    except TimeoutException:
        print("❌ Test failed: Whitespace inputs not blocked! Potential vulnerability detected.")

    """Test case sensitivity."""
    print("\n--- Test Case 15: Testing case sensitivity ---")
    login("STANDARD_USER", "SECRET_SAUCE")
    try:
        error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message displayed: {error_message}. Test successful: Case sensitivity enforced ✅.")
    except TimeoutException:
        print("❌ Test failed: Case sensitivity not enforced! Potential vulnerability detected.")

    """Test password field masking."""
    print("\n--- Test Case 16: Testing password field masking ---")
    driver.get("https://www.saucedemo.com/")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    if password_field.get_attribute("type") == "password":
        print("Test successful: Password field is masked ✅.")
    else:
        print("❌ Test failed: Password field is not masked! Potential security issue.")

    """Test browser back button functionality."""
    print("\n--- Test Case 17: Testing browser back button ---")
    login("standard_user", "secret_sauce")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inventory_container")))
    driver.back()
    time.sleep(2)
    current_url = driver.current_url
    if "saucedemo.com" in current_url:
        print("Test successful: Browser back button handled correctly ✅.")
    else:
        print("❌ Test failed: Browser back button allowed unauthorized access!")


    """Test logout functionality."""
    print("\n--- Test Case 18: Testing logout functionality ---")
    login("standard_user", "secret_sauce")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inventory_container")))
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(2)
    current_url = driver.current_url
    if "saucedemo.com" in current_url:
        print("Test successful: Logout functionality works as expected ✅.")
    else:
        print("❌ Test failed: Logout functionality not working properly!")



    # Add a sleep to keep the browser open
    print("\nTests completed. Keeping the browser open for review.")
    time.sleep(10)  # Keeps the browser open for 10 seconds

    # Closing the browser
    driver.quit()
    print("Browser closed.")

# Run the tests
test_login()
