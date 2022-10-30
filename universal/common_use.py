def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

whitelist = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}

espn_cookies = {"swid": "{11F62244-D8C5-462F-BA6C-F2393EF28D6E}",
                "espn_s2": "AECy1%2FYwRZXQGhDYs%2BdlWOH%2FXtfsiEj%2Fl48YgQU61VjeBcVjNBakLk49WOW309ptiG%2BQBpYWDypR8ZY09H%2FUCpKeXfmc0e4K1biE0IoPPJQsRaq4PVmZiECEw%2Fv9Vw8bsOt1WZipnhzc20mlYtGZGD15mf7fUB9ShLkGi9LgTQg5LtdzgdN7l8UBZikcv49Uc3VYLlLaATYxul2ZTT20d1TS7ImzzezCeJSTCgDp1uruqHCyNe07yquk9AYxUB856knCXJWNhoGdtQ5CDYhpYEF%2F"}

