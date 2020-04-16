# Mountain Project Database Builder
This project is a web crawler built using [Scrapy](https://scrapy.org/) that aims to pull important metadata about both areas and routes from [Mountain Project](https://mountainproject.com) into a database to serve as the backbone for a 3rd party
API. The ultimate goal of this project is to allow 3rd party developers to provide supplementary services for Mountain Project users.

## Prerequisites
- Python 3.x
- A MongoDB database

## Installation
  1. Clone the repository
  2. Navigate to your cloned repository
  3. Run `pip install -r requirements.txt`
  4. (Optional) Create a file called creds.py in the project root and enter the following with your details substituted
  
    URI="<YOUR_MONGO_URI>"
    DATABASE="<YOUR_MONGO_DATABASE_NAME>"

## Usage
The spider can be started with: `scrapy crawl mp`

Alternatively if you didn't perform step 4, use:

`scrapy crawl mp -s MONGO_URI=<YOUR_MONGO_URI> MONGO_DATABASE=<YOUR_MONGO_DATABASE_NAME>`

## What if I don't want to use MongoDB?
If MongoDB doesn't suit your needs, creating a new serialization pipeline is fairly trivial. I recommend looking at
[Scrapy's Item Pipeline docs](https://docs.scrapy.org/en/latest/topics/item-pipeline.html) as a starting place. All items coming
into the pipeline are defined in `mp_scraper/items.py`.

## Contributing
If you've somehow stumbled across this project and want to help, I try to open issues for things that I want changed. At the
time of writing this, I don't expect anybody to be contributing other than me for a long time (maybe ever). However, if you do
want to contribute and an issue doesn't have enough information, leave a comment and I can give you a better idea of what I
was thinking.
