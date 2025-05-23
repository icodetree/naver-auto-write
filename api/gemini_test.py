import google.generativeai as genai

API_KEY = '구글 gemini api key'

# Gemini API 키 설정
genai.configure(api_key=API_KEY)

# 모델명 지정
gemini_model = 'gemini-2.0-flash'

# 프롬프트 예시
prompt = '안녕하세요, Gemini! 간단한 자기소개를 해주세요.'

def main():
  try:
    model = genai.GenerativeModel(gemini_model)
    response = model.generate_content(prompt)
    print('Gemini 응답:')
    print(response.text)
  except Exception as e:
    print('에러 발생:', e)

if __name__ == '__main__':
  main() 