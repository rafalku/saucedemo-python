# E2E Automation

Sample tests for https://www.saucedemo.com/ website.


## Prerequisites

* Python >= 3.9
* pip
* Chrome browser
* chromedriver (at location in PATH environment variable)

## Running

```
pip install -r requirements.txt
pytest --driver=Chrome --html=report.html --self-contained-html

```
Test report will be created in `report.html`

## Multi-browser testing

It is possible to specify different browser by passing its name as value of `--driver` argument in the above command 
(provided that respective driver is available at location in `PATH` variable).
It was tested with Firefox

## Tech Stack
* [pytest](https://docs.pytest.org/)
* [PyHamcrest](https://github.com/hamcrest/PyHamcrest) 
* [Selenium](https://www.selenium.dev/)
