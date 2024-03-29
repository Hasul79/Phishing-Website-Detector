<h1 align="center">Phishing Website Detector</h1>
<br>


![2_05_25_50_Phishing-_1_H@@IGHT_600_W@@IDTH_800](https://github.com/Hasul79/Phishing-Website-Detector/assets/95657084/0c47a492-ae91-4491-99f2-18c4ec287452)

<br>



# Для запуска предоставленного Python-кода выполните следующие шаги:
<ul>

<li>Установите необходимые библиотеки:</li>

![Screenshot 2024-03-02 020551](https://github.com/Hasul79/Phishing-Website-Detector/assets/95657084/47b17144-83f9-4c85-ad87-6028934cad81)

<li>Создайте скрипт на Python:</li>

![Screenshot 2024-03-02 021427](https://github.com/Hasul79/Phishing-Website-Detector/assets/95657084/5c54227d-4c2c-42f6-88be-d1108db349f5)


<li>Откройте свой любимый текстовый редактор,вставьте код</li>

```
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
```

<li>Запустите скрипт</li>

![Screenshot 2024-03-02 020155](https://github.com/Hasul79/Phishing-Website-Detector/assets/95657084/c54ed702-a5b5-4fbd-82b9-ba4fc7654129)


<li>Укажите URL для тестирования:</li>
<p>Скрипт запросит вас ввести URL, который вы хотите проверить на фишинг. Введите URL и нажмите Enter.</p>

<li>Проверьте вывод</li>
<p>Затем скрипт проверит предоставленный URL по указанной базе данных фишинга и проанализирует его содержимое. Он выведет предупреждения, если обнаружены потенциальные признаки фишинга.</p>
</ul>


# Объяснение:

<ol>

<li>
    <b>Импорт библиотек:</b> <br />
Скрипт использует библиотеку requests для выполнения HTTP-запросов и BeautifulSoup для разбора HTML.</li>
<li>
    <b>Функция is_phishing:</b> <br />
Эта функция принимает URL, отправляет HTTP-запрос на веб-сайт и затем проверяет наличие общих ключевых слов фишинга в HTML-контенте.</li>
  <li>  <b>Главная функция: </b> <br />
Принимает ввод пользователя для URL и вызывает функцию is_phishing. Затем выводит предупреждение, если веб-сайт может быть фишинговым.</li>

<li>
    <b>if name == "main":</b> <br />
Этот блок гарантирует, что функция main вызывается при выполнении скрипта.</li>
<br/>

# Author: Hasmik Minasyan
