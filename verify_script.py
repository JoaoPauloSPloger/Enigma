from playwright.sync_api import sync_playwright
import sys
import os

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/verification.html")
        
        # Click the run button
        page.click("button[onclick='runAllTests()']")
        
        # Wait for summary to have text
        page.wait_for_function("document.getElementById('summary').innerText.includes('Concluído')")
        
        # Get result
        summary_text = page.inner_text("#summary")
        print(summary_text)
        
        # Check for failures
        failures = page.locator(".status.fail").count()
        
        browser.close()
        
        if failures > 0:
            print(f"FAILED: {failures} tests failed.")
            sys.exit(1)
        else:
            print("SUCCESS: All tests passed.")
            sys.exit(0)

if __name__ == "__main__":
    run_verification()
