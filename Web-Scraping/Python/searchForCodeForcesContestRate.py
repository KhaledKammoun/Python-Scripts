from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def find_your_name_selenium(contest_id, your_handle):
    base_url = f"https://codeforces.com/contestRegistrants/{contest_id}/page/"
    service = Service("C:\\Drivers\\chromedriver.exe")  # Chemin vers votre ChromeDriver

    options = Options()
    options.add_argument("--headless")  # Run browser in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU for headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=service, options=options)

    page = 1
    found = False
    try:
        while not found:
            driver.get(f"{base_url}{page}")
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "datatable"))
            )
            rows = driver.find_elements(By.CSS_SELECTOR, "table.datatable tr")[1:]  # Skip the header row
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                handle = cells[1].text.strip()
                if handle == your_handle:
                    print(f"Found {your_handle} at position {cells[0].text.strip()} with rating {cells[2].text.strip()}")
                    found = True
                    break
            if not found:
                page += 1
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()
    
    if not found:
        print(f"{your_handle} not found in the contest registrants list.")

# Replace with the contest ID and your Codeforces handle
find_your_name_selenium(2051, "khaledkammoun")



def inspectControllerFunction() : 
    # function fetchParticipants(pageNumber) {
    #     const url = `https://codeforces.com/contestRegistrants/2051/page/${pageNumber}`; // Replace with the correct URL and contest ID

    #     // Fetch the page using Fetch API
    #     fetch(url)
    #         .then(response => response.text())
    #         .then(html => {
    #             const parser = new DOMParser();
    #             const doc = parser.parseFromString(html, 'text/html');
    #             const registrantsTable = doc.getElementsByClassName("registrants")[0];

    #             if (!registrantsTable) {
    #                 console.log("No registrants table found on this page.");
    #                 return;
    #             }

    #             const rows = registrantsTable.getElementsByTagName("tr");

    #             // Skip the header row and process participant rows
    #             const participants = [];
    #             for (let i = 1; i < rows.length; i++) {
    #                 const cells = rows[i].getElementsByTagName("td");

    #                 if (cells.length > 0) {
    #                     const name = cells[1].innerText.trim(); // Assuming the second column is the name
    #                     const rating = cells[2].innerText.trim(); // Assuming the third column is the rating
    #                     const status = cells[4].innerText.trim(); // Assuming the fifth column is the status

    #                     participants.push({ name, rating, status });

    #                     // Check if the name includes the substring "khaledkammoun" (case-insensitive)
    #                     if (name.toLowerCase().includes("00karim00".toLowerCase())) {
    #                         console.log(`Found participant: ${name}`);
    #                         console.log(`Rating: ${rating}`);
    #                         console.log(`Status: ${status}`);
    #                         return; // Stop further processing after finding the participant
    #                     }
    #                 }
    #             }

    #             // Log the participants of the current page
    #             console.log(`Page ${pageNumber} participants:`);
    #             // console.log(participants);

    #             // Check if there's another page to load
    #             const nextPageButton = doc.querySelector('li a.arrow');
    #             if (nextPageButton) {
    #                 fetchParticipants(pageNumber + 1);
    #             } else {
    #                 console.log("No more pages.");
    #             }
    #         })
    #         .catch(error => {
    #             console.error('Error fetching the page:', error);
    #         });
    # }

    # // Start fetching data from page 1
    # fetchParticipants(30);

    pass