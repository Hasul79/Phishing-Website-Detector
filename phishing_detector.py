import requests
from bs4 import BeautifulSoup

def check_phishing(url):
    try:
        # Получаем содержимое веб-страницы
        response = requests.get(url)
        response.raise_for_status()

        # Анализируем содержимое с помощью BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Пример: Проверяем наличие ключевого слова "фишинг" в заголовке
        phishing_keyword = 'фишинг'
        if phishing_keyword.lower() in soup.title.text.lower():
            print(f"Предупреждение: Заголовок веб-страницы содержит '{phishing_keyword}'. Это может быть фишинговый сайт.")
        else:
            print("Веб-страница кажется безопасной.")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    # Запросите пользователя ввести URL для проверки
    user_url = input("Введите URL для проверки на фишинг: ")
    check_phishing(user_url)

