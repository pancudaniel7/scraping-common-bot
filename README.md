# Scraping Common Bot

### Build

```sh
tox -e build
```

Or for local build:

```sh
pip install -e .
pipenv install -e .
```



### Push

```sh
tox -e publish
tox -e publish -- --repository pypi
tox -av
```

More info [here](https://github.com/pyscaffold/pyscaffold)
