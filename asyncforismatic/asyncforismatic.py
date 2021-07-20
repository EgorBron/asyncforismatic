"""
# Forismatic

## An unoficall library for getting quotes from the Forismatic API. Supports asynchronous syntax.

## Неофицальная библиотека для получения цитат из Forismatic API. Поддерживает асинхронный синтаксис.

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
    return await asyncforismatic.async_quote()
print(asyncio.run(example()))
```

## Methods || Методы

### Getting a quote (async) || Получение цитаты (асинхронно)

***corotinue*** `async_quote(lang='en', *, as_dict=False)`

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
"""
from typing import Union
import aiohttp, requests

class LangIsNotSupported(Exception):
	pass
async def async_quote(lang = 'en', *, as_dict = False) -> Union[str, dict]:
	"""
	corotinue `async_quote(lang='en', *, as_dict=False)`\n
	### Getting a quote (async) || Получение цитаты (асинхронно)\n\n
		Returns an quote from Forismatic API\n
		Возвращает цитату из Forismatic API
		#### Parameters || Параметры
		as_dict: `bool`\n
			```If True, quote returns as JSON-like object (dict)```\n
			```Если True, возвращает результат в JSON'о подобном формате (dict, словарь)```\n
		#### Raises exceptions || Поднимает исключения
		`TypeError`\n
				The language is not passed as 'str'\n
				Язык передан не как 'str'\n\n
		`LangIsNotSupported`\n
				The language is not supported\n
				Язык не поддерживается\n\n
		Returns `Union[str, dict]`\n
		Возвращает `Union[str, dict]`
	"""
	if not isinstance(lang, str):
		raise TypeError(f'You must use language as \'str\', not as {type(lang)}')
	if lang not in ['en', 'ru']:
		raise LangIsNotSupported('This language not in supported (english - en and russian - ru).')
	async with aiohttp.ClientSession() as requester:
		async with requester.get(url = f"http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang={lang}") as response:
			quote = await response.json()
			if as_dict: return quote
			author = '©'+quote["quoteAuthor"] if quote["quoteAuthor"] else ''
			return f'{quote["quoteText"]}{author}'
def quote(lang = 'en', *, as_dict = False) -> Union[str, dict]:
	"""
def `quote(lang='en', *, as_dict=False)`\n
	### Getting a quote || Получение цитаты
		Returns an quote from Forismatic API\n
		Возвращает цитату из Forismatic API
		#### Parameters || Параметры
		as_dict: `bool`\n
			```If True, quote returns as JSON-like object (dict)```\n
			```Если True, возвращает результат в JSON'о подобном формате (dict, словарь)```\n
		#### Raises exceptions || Поднимает исключения
		`TypeError`\n
				The language is not passed as 'str'\n
				Язык передан не как 'str'\n\n
		`LangIsNotSupported`\n
				The language is not supported\n
				Язык не поддерживается\n\n
		Returns `Union[str, dict]`\n
		Возвращает `Union[str, dict]`
	"""
	if not isinstance(lang, str):
		raise TypeError(f'You must use language as \'str\', not as {type(lang)}')
	if lang not in ['en', 'ru']:
		raise LangIsNotSupported('This language not in supported (english and russian).')
	quote = requests.post(url = f"http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang={lang}").json()
	if as_dict: return quote
	author = '©'+quote["quoteAuthor"] if quote["quoteAuthor"] else ''
	return f'{quote["quoteText"]}{author}'
