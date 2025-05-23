import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import random
from selenium.webdriver.common.action_chains import ActionChains

# 네이버 계정 정보
NAVER_ID = 'master8407'
NAVER_PW = 'qusghdud0311#$'

# 크롬 드라이버 경로 (환경에 맞게 수정)
CHROME_DRIVER_PATH = '/usr/local/bin/chromedriver'

# 셀레니움 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--start-maximized')

# 드라이버 실행 (자동 경로)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

try:
  # 1. 네이버 로그인 페이지 접속
  driver.get('https://nid.naver.com/nidlogin.login')

  # 2. 영문 입력기로 전환 (Mac: Command + Space)
  pyautogui.hotkey('command', 'space')
  time.sleep(0.2)

  # 3. 아이디 입력
  id_input = wait.until(EC.presence_of_element_located((By.ID, 'id')))
  id_input.click()
  time.sleep(0.5)
  pyperclip.copy(NAVER_ID)
  pyautogui.hotkey('command', 'v')
  time.sleep(0.5)

  # 4. 비밀번호 입력
  pw_input = wait.until(EC.presence_of_element_located((By.ID, 'pw')))
  pw_input.click()
  time.sleep(0.5)
  pyperclip.copy(NAVER_PW)
  pyautogui.hotkey('command', 'v')
  time.sleep(0.5)

  # 5. 로그인 버튼 클릭
  login_btn = wait.until(EC.element_to_be_clickable((By.ID, 'log.login')))
  login_btn.click()
  time.sleep(2)

  # 6. 블로그 글쓰기 페이지로 이동
  driver.get('https://blog.naver.com/GoBlogWrite.naver')
  time.sleep(2)

  # 1. #mainFrame iframe 전환
  try:
    main_frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainFrame')))
    driver.switch_to.frame(main_frame)
    time.sleep(1)
  except Exception as e:
    print('mainFrame 전환 실패:', e)
    raise

  actions = ActionChains(driver)

  # 2. .se-popup-button-cancel 셀렉터가 존재하면 클릭
  try:
    cancel_btn = driver.find_element(By.CSS_SELECTOR, '.se-popup-button-cancel')
    cancel_btn.click()
    time.sleep(0.5)
  except:
    pass

  # 3. .se-help-panel-close-button 셀렉터가 존재하면 클릭
  try:
    help_close_btn = driver.find_element(By.CSS_SELECTOR, '.se-help-panel-close-button')
    help_close_btn.click()
    time.sleep(0.5)
  except:
    pass

  # 4. .se-section-documentTitle 클릭 후 "제목 테스트" 입력 (ActionChains, 랜덤 딜레이)
  title_elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.se-section-documentTitle')))
  title_elem.click()
  time.sleep(0.3)
  title_text = '제목 테스트'
  for ch in title_text:
    actions.send_keys(ch).perform()
    time.sleep(random.uniform(0.01, 0.10))

  # 5. .se-section-text 클릭 후 본문 입력 (5줄, ActionChains, 랜덤 딜레이)
  body_elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.se-section-text')))
  body_elem.click()
  time.sleep(0.3)
  body_line = '안녕하세요 내용을 입력하고 있어요'
  for _ in range(5):
    for ch in body_line:
      actions.send_keys(ch).perform()
      time.sleep(random.uniform(0.01, 0.10))
    actions.send_keys('\n').perform()
    time.sleep(0.1)

  # 6. .save_btn__bzc5B 클릭 (저장)
  save_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.save_btn__bzc5B')))
  save_btn.click()
  time.sleep(2)

  input('엔터를 누르면 브라우저가 종료됩니다...')

except Exception as e:
  print('오류 발생:', e)
finally:
  # 필요시 driver.quit() 호출 (테스트 시 주석처리)
  pass 