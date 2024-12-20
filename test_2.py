
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from transformers import pipeline 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.get("https://dev.rejara.com/login")
time.sleep(5)
driver.find_element(By.ID,"email").send_keys("nqqv6j4tk3@bltiwd.com")
time.sleep(5)
driver.find_element(By.ID,"password").send_keys("Admin@123")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(5)
all_questions=[]
driver.get("https://dev.rejara.com/gather-assist")

stories=["https://dev.rejara.com/gather-assist/chat-screen/Personal/4575/Profile/ttttt%20yllllll","https://dev.rejara.com/gather-assist/chat-screen/Dependents/4569/Child/ccccccc","https://dev.rejara.com/gather-assist/chat-screen/Dependents/4570/Parent/pppcpcpcp"]




# Load a pre-trained question-answering pipeline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def get_relevant_answer(question, context="Provide relevant domain-specific context here"):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Example usage with fetched questions
for story in stories:
    driver.get(story)
    time.sleep(20)
    questions = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".justify-start.p-2.text-sm.rounded-md.bg-neutral-800.bg-opacity-10")
        ))
    # questions = driver.find_element(By.CSS_SELECTOR, "div[class='justify-start p-2 text-sm rounded-md bg-neutral-800 bg-opacity-10'] span")
    # for question in questions:
    question = questions.text
    print(question)
    answer = get_relevant_answer(question)
    print(f"Q: {question}\nA: {answer}")    
    time.sleep(20)