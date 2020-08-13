# 🕷 Scrapy Starter Project 🕷

Empty starter Scrapy project. Just enough to get you up and running quickly.


## Get Started

```
# install virtualenv to isolate the project dependencies
pip3 install virtualenv

# init the virtualenv
virtualenv venv

# activate the virtualenv
. ./venv/bin/activate

# install the project dependencies
pip install -r requirements.txt
```

# Usage

To run a spider (replace `myspider` with the spider's name):

`scrapy crawl myspider -o output.json`
