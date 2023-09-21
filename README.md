# FlaskAndFastAPI

Курс по Фреймворкам Flask и FastAPI

## Урок 1. Знакомство с Flask.

**Задание 1**
Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние
шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы «Одежда», «Обувь» и «Куртка»,
используя базовый шаблон.
[Решение](lesson_1)

## Урок 2. Погружение во Flask

**Задание 1**
Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан
cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия, где будет
отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными
пользователя и произведено перенаправление на страницу ввода имени и электронной почты. [Решение](lesson_2)

## Урок 3. Погружение во Flask

**Задание 1**
Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и
кнопку "Зарегистрироваться". При отправке формы данные должны сохраняться в базе данных, а пароль должен быть
зашифрован. [Решение](lesson_3)

## Урок 4. Введение в многозадачность

**Задание 1**
Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение
должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения
программы. [Решение](lesson_4)

# Урок 5. Знакомство с FastAPI

**Задание 1**

- Создать API для добавления нового пользователя в базу данных. Приложение должно иметь возможность принимать POST
  запросы с данными нового пользователя и сохранять их в базу данных.
- Создайте модуль приложения и настройте сервер и маршрутизацию.
- Создайте класс User с полями id, name, email и password.
- Создайте список users для хранения пользователей.
- Создайте маршрут для добавления нового пользователя (метод POST).
- Реализуйте валидацию данных запроса и ответа. [Решение](lesson_5)

**Задание 2**

- Создать API для обновления информации о пользователе в базе данных. Приложение должно иметь возможность принимать PUT
  запросы с данными пользователей и обновлять их в базе данных.
- Создайте модуль приложения и настройте сервер и маршрутизацию.
- Создайте класс User с полями id, name, email и password.
- Создайте список users для хранения пользователей.
- Создайте маршрут для обновления информации о пользователе (метод PUT).
- Реализуйте валидацию данных запроса и ответа. [Решение](lesson_5)

**Задание 3**

- Создать API для удаления информации о пользователе из базы данных. Приложение должно иметь возможность принимать
  DELETE
  запросы и удалять информацию о пользователе из базы данных.
- Создайте модуль приложения и настройте сервер и маршрутизацию.
- Создайте класс User с полями id, name, email и password.
- Создайте список users для хранения пользователей.
- Создайте маршрут для удаления информации о пользователе (метод DELETE).
- Реализуйте проверку наличия пользователя в списке и удаление его из списка. [Решение](lesson_5)

**Задание 4**

- Создать веб-страницу для отображения списка пользователей. Приложение должно использовать шаблонизатор Jinja для
  динамического формирования HTML страницы.
- Создайте модуль приложения и настройте сервер и маршрутизацию.
- Создайте класс User с полями id, name, email и password.
- Создайте список users для хранения пользователей.
- Создайте HTML шаблон для отображения списка пользователей. Шаблон должен содержать заголовок страницы, таблицу со
  списком пользователей и кнопку для добавления нового пользователя.
- Создайте маршрут для отображения списка пользователей (метод GET).
- Реализуйте вывод списка пользователей через шаблонизатор Jinja. [Решение](lesson_5)

## Урок 6. Дополнительные возможности FastAPI

**Задание**

Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и
пользователи.

- Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
- Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
- Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
- Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и
  пароль.
- Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN
  KEY), дата заказа и статус заказа.
- Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
- Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
  Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.

 