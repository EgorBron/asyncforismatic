import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="asyncforismatic",
    version="0.0.1",
    author="EgorBron",
    author_email="bataikinegor@yandex.ru",
    description="A library for getting quotes from the Forismatic API. Supports asynchronous syntax. Библиотека для получения цитат из Forismatic API. Поддерживает асинхронный синтаксис.",
    long_description= """
    # *Forismatic* ![forismatic_logo](http://forismatic.com/favicon.ico)

## An unoficall library for getting quotes from the Forismatic API. Supports asynchronous syntax.

## Неофицальная библиотека для получения цитат из Forismatic API. Поддерживает асинхронный синтаксис\.

## Installing || Установка

```bash
pip3 install asyncforismatic
```

Requires aiohttp and requests

## Examples || Примеры

```py
import asyncforismatic
import asyncio

# getting sync quote on russian as dict
# синхронное получение цитаты на русском в виде словаря
print(asyncforismatic.quote(lang='ru', as_dict=True)) 

# getting async quote with default params (english language and formated quote)
# асинхронное получение цитаты со стандартными параметрами (английский язык и отформатированная цитата)
async def example():
    return await asyncforismatic.asyncforismatic()
print(asyncio.run(example()))
```

## Methods || Методы

### Getting a quote (async) || Получение цитаты (асинхронно)

***corotinue*** `asyncforismatic(lang='en', *, as_dict=False)`

* Returns an quote from Forismatic API
* Возвращает цитату из Forismatic API

#### Parameters || Параметры

*as_dict*: `bool`

* If True, quote returns as JSON-like object (dict)
* Если True, возвращает результат в JSON'о подобном формате (dict, словарь)

#### Raises exceptions || Поднимает исключения

`TypeError`

* The language is not passed as 'str'
* Язык передан не как 'str'

`LangIsNotSupported`

* The language is not supported
* Язык не поддерживается

**Returns** `Union[str, dict]`
**Возвращает**`Union[str, dict]`

### Getting a quote || Получение цитаты

***def*** `quote(lang='en', *, as_dict=False)`

* Returns an quote from Forismatic API
* Возвращает цитату из Forismatic API

#### Parameters || Параметры

*as_dict*: `bool`

* If True, quote returns as JSON-like object (dict)
* Если True, возвращает результат в JSON'о подобном формате (dict, словарь)

#### Raises exceptions || Поднимает исключения

`TypeError`

* The language is not passed as 'str'
* Язык передан не как 'str'

`LangIsNotSupported`

* The language is not supported
* Язык не поддерживается

**Returns** `Union[str, dict]`
**Возвращает** `Union[str, dict]`

## Exceptions || Исключения

`LangIsNotSupported`

* Raises when the language is not supported
* Возникает когда язык не поддерживается
    """,#long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EgorBron/asyncforismatic",
    project_urls={
        "Bug Tracker": "https://github.com/EgorBron/asyncforismatic/issues",
        'Creator YouTube channel': 'https://www.youtube.com/channel/UCWd7FjRN4EM6D7tiJUv6lWg'
    },
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    #package_dir={"": "asyncforismatic"},
    packages=setuptools.find_packages(where='.'),
    python_requires=">=3.9",
    install_requires = ['aiohttp', 'requests'],
    zip_save = False
)