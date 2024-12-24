from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

# Initialize the Selenium WebDriver and wait object
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

# Log in to the application
driver.get("https://dev.rejara.com/login")
driver.find_element(By.ID, "email").send_keys("nqqv6j4tk3@bltiwd.com")
driver.find_element(By.ID, "password").send_keys("Admin@123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(5)

# Stories to process
stories = [
    "https://dev.rejara.com/gather-assist/chat-screen/Personal/4575/Profile/ttttt%20yllllll",
    # "https://dev.rejara.com/gather-assist/chat-screen/Dependents/4569/Child/ccccccc",
    # "https://dev.rejara.com/gather-assist/chat-screen/Dependents/4570/Parent/pppcpcpcp"
]

# Function to fetch answers using the external API
def chatbot_answer_question(text):
    url = "https://human-impersonator.llama-shubham.workers.dev/"
    params = {
        "text": text
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        json_data = response.json()
        return json_data.get("response", "No response from API")
    except requests.exceptions.RequestException as e:
        return f"Error in API request: {e}"

# Process each story
for story in stories:
    driver.get(story)
    time.sleep(5)
    story_question=[]

    # Wait for the question element and get the text
    try:
        question_elements=wait.until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".justify-start.p-2.text-sm.rounded-md.bg-neutral-800.bg-opacity-10")
            )
        )
        for quest in question_elements:
            question =quest.text.strip()
            


            if not question:
                print("Question text is empty, skipping...")
                continue

            # Fetch the answer using the API
            print(f"Q: {question}")
            answer = chatbot_answer_question(question)
            ans=driver.find_element(By.CSS_SELECTOR,("#userInputId")).send_keys(answer)
            time.sleep(2)
            send=driver.find_element(By.CSS_SELECTOR,"img[alt='Send icon']").click()
            time.sleep(10)
            print(f"A: {answer}")
            story_question.append(question)
        for story in story_question:
             if story !=question:
                question =quest.text.strip()
            


                if not question:
                    print("Question text is empty, skipping...")
                    continue

            # Fetch the answer using the API
                print(f"Q: {question}")
                answer = chatbot_answer_question(question)
                ans=driver.find_element(By.CSS_SELECTOR,("#userInputId")).send_keys(answer)
                time.sleep(2)
                send=driver.find_element(By.CSS_SELECTOR,"img[alt='Send icon']").click()
                time.sleep(10)
                print(f"A: {answer}")    
        



    except Exception as e:
            print(f"Error while processing story {story}: {e}")
    time.sleep(10)
        
        

    
    

# Close the driver
driver.quit()
