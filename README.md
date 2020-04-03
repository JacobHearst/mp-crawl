# Mountain Project Database Builder
This project is a web crawler built using [Scrapy](https://scrapy.org/) that aims to pull important metadata about both areas and routes from [Mountain Project](https://mountainproject.com) into a MySQL database to serve as the backbone for a 3rd party
API. The ultimate goal with this project is to allow 3rd party developers to provide supplementary services for Mountain Project users.

## Prerequisites
As it stands now, this code is expecting there to be a MySQL (or MariaDB) server with the correct schema. Seeing as I would
like this to be easy for others to take advantage of, hopefully this will change. For now, the scheme will be documented in
SCHEMA.md, and create code will be documented in db_setup.sql

## Installation
  1. Clone the repository
  2. Navigate to your cloned repository
  3. Run `pip install -r requirements.txt`

## Usage
Before running the spider, ensure that you've entered your database credentials:
  1. Edit the file named `db_config_template.json` and enter in your connection details
  2. Rename `db_config_template.json` to `db_config.json`

Once you've done that, run the spider with: `scrapy crawl mp`

## Contributing
If you've somehow stumbled across this project and want to help, I try to open issues for things that I want changed. At the
time of writing this, I don't expect anybody to be contributing other than me for a long time (maybe ever). However, if you do
want to contribute and an issue doesn't have enough information, leave a comment and I can give you a better idea of what I
was thinking.
