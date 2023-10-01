# just-eat-api

## How to run

Clone this repo and run:
```shell
pip install requirements.txt # (requests lib needed)
```

- Change POSTAL_CODE and run file

Or

- Use Python console:
```python
>>> from just_eat_client import JustEatClient
>>> client = JustEatClient()
>>> restaurants = client.get_restaurants_by_postalcode("{POSTAL_CODE}")
>>> print(restaurants)
```
