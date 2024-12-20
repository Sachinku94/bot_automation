from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from transformers import pipeline
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

# Log in to the application
driver.get("https://dev.rejara.com/login")
driver.find_element(By.ID, "email").send_keys("nqqv6j4tk3@bltiwd.com")
driver.find_element(By.ID, "password").send_keys("Admin@123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(5)

# Load pre-trained question-answering pipeline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Stories to process
stories = [
    "https://dev.rejara.com/gather-assist/chat-screen/Personal/4575/Profile/ttttt%20yllllll",
    "https://dev.rejara.com/gather-assist/chat-screen/Dependents/4569/Child/ccccccc",
    "https://dev.rejara.com/gather-assist/chat-screen/Dependents/4570/Parent/pppcpcpcp"
]

# Function to get answer
def get_relevant_answer(question, context="Provide relevant domain-specific context here"):
    if not question.strip():
        raise ValueError("Question cannot be empty.")
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Process each story
for story in stories:
    driver.get(story)
    time.sleep(5)

    # Wait for the element and get the text
    try:
        question_element = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".justify-start.p-2.text-sm.rounded-md.bg-neutral-800.bg-opacity-10")
            )
        )
        question = question_element.text.strip()
        if not question:
            print("Question text is empty, skipping...")
            continue

        print(f"Q: {question}")
        answer = get_relevant_answer(question)
        print(f"A: {answer}")
    except Exception as e:
        print(f"Error while processing story {story}: {e}")
