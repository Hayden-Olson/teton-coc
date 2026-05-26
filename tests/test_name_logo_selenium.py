"""
Make sure you have the dependencies installed:
python -m pip install selenium pytest
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://127.0.0.1:5500/web"

PAGES = [
    "/index.html",
    "/join.html",
    "/directory.html",
    "/admin.html",
]

RESOLUTIONS = [
    (1920, 1080),
    (768, 1024),
    (375, 667),
]


@pytest.fixture
def driver():
    options = Options()
    # Comment out this line if you want to see the browser during testing
    options.add_argument("--headless=new") 
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# -----------------------------
# ✅ Test: Header Text (split elements)
# -----------------------------
@pytest.mark.parametrize("page", PAGES)
@pytest.mark.parametrize("resolution", RESOLUTIONS)
def test_header_text_visible(driver, page, resolution):
    driver.set_window_size(*resolution)
    driver.get(f"{BASE_URL}{page}")

    wait = WebDriverWait(driver, 10)
    header = wait.until(EC.presence_of_element_located((By.TAG_NAME, "header")))

    teton_idaho = header.find_element(By.XPATH, ".//*[normalize-space()='Teton Idaho']")
    chamber = header.find_element(By.XPATH, ".//*[normalize-space()='Chamber of Commerce']")

    assert teton_idaho.is_displayed()
    assert chamber.is_displayed()


# -----------------------------
# ✅ Test: Logo visible + correct alt text
# -----------------------------
@pytest.mark.parametrize("page", PAGES)
@pytest.mark.parametrize("resolution", RESOLUTIONS)
def test_logo_visible(driver, page, resolution):
    driver.set_window_size(*resolution)
    driver.get(f"{BASE_URL}{page}")

    wait = WebDriverWait(driver, 10)
    header = wait.until(EC.presence_of_element_located((By.TAG_NAME, "header")))

    logo = header.find_element(By.CSS_SELECTOR, "img")

    # Visible
    assert logo.is_displayed(), f"Logo not visible on {page} at {resolution}"

    # Has alt text (accessibility + correctness)
    alt_text = logo.get_attribute("alt")
    assert alt_text is not None and alt_text != "", "Logo missing alt text"

    # Optional: stronger check (if consistent across pages)
    assert "Teton" in alt_text or "Chamber" in alt_text


# -----------------------------
# ✅ Test: Browser tab title
# -----------------------------
@pytest.mark.parametrize("page", PAGES)
def test_page_title(driver, page):
    driver.get(f"{BASE_URL}{page}")

    assert driver.title == "Teton Idaho CoC", (
        f"Incorrect title on {page}: {driver.title}"
    )