# Scraping and Analysing Job Positions from LinkedIn

This project was created with the intent of understanding what are the main requirements for Data Analysts and Data Scientists jobs. To do that we created a crawler to scrap job pages from LinkedIn and processed the text, in order to achieve a report with the most frequent skills that are asked for each position. 


## Authors/Contributors

**Carlos Madriz**  ([LinkedIn](https://www.linkedin.com/in/carlos-madriz/) | [Github](https://github.com/carlosmd14/))  
**Inês Garcia**  ([LinkedIn](https://www.linkedin.com/in/in%C3%AAs-garcia/) | [Github](https://github.com/Inrx))

# Table of contents
* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Acknowledgements](#acknowledgements)
* [Features](#features)

## Getting Started

To use the code from this project you should fork this repository and clone it locally.

## Prerequisites

To run the sraping code you will need to make sure you have the following python libraries installed:
1. [Selenium](https://pypi.org/project/selenium/)
2. [tqdm](https://pypi.org/project/tqdm/)
3. csv
4. math
5. time
6. os
7. numpy
8. pandas
9. random
10. re

As per the text processing you will need:
1. [nltk](https://www.nltk.org/)
2. [langdetect](https://pypi.org/project/langdetect/)

## Features

- Job search with your own credentials.
- Your account is protected from bot detection - it's only used to get the jobs links. To scrape each job, you don't need to be logged in.
- Searches by job title and by location (specified by you).
- Gets all the job position links for the specified parameters.
- Gets, cleans and analyses all the job information for each job position.


## Acknowledgements

* **David Craven** who wrote and [article](https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven/) on how to use Selenium to Scrap LinkedIn, that was very helpful.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


