<div id="top"></div>



<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<h3 align="center">Inventory Tracker</h3>

  <p align="center">
    Inventory tracker using Django, GraphQL, and Postgres
    <br />
    <a href="https://github.com/manlalaro1/ShopifyF22"><strong>Explore the repo »</strong></a>
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This inventory API is a Django application with a GraphiQL interface. 

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Django](https://www.djangoproject.com/)
* [GraphQL](https://graphql.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Graphene Django](https://docs.graphene-python.org/)
* [GraphiQL](https://github.com/graphql/graphiql)
* [Docker](https://www.docker.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Since this project is built to run in containers, `Docker` and `Docker-Compose` is required to run the project.

### Prerequisites

* [Docker](https://docs.docker.com/get-docker/)
* [Docker-compose](https://docs.docker.com/compose/install/)

### Installation

1. Get a free API Key at [https://openweathermap.org/](https://openweathermap.org/)
2. Clone the repo
   ```sh
   git clone https://github.com/manlalaro1/ShopifyF22.git
   ```
3. Enter your credentials in `docker-compose.yaml`
   ```python
   POSTGRES_NAME='ENTER YOUR DB NAME'
   POSTGRES_USER='ENTER YOUR DB USER'
   POSTGRES_PASSWORD='ENTER YOUR DB PASSWORD'
   API_KEY='ENTER YOUR API'
   ```
4. Start the docker containers:
   ```sh
   docker-compose up
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This project utilizes the GraphiQL interface to visualize an inventory API. If you'd like to try it out for yourself, there is a repl running without containers [here](https://shopifyf22-1.manlalaro1.repl.co/).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Patrick O'Donnell - odonnellp46@gmail.com

Project Link: [https://github.com/manlalaro1/ShopifyF22](https://github.com/manlalaro1/ShopifyF22)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/manlalaro1/ShopifyF22.svg?style=for-the-badge
[contributors-url]: https://github.com/manlalaro1/ShopifyF22/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/manlalaro1/ShopifyF22.svg?style=for-the-badge
[forks-url]: https://github.com/manlalaro1/ShopifyF22/network/members
[stars-shield]: https://img.shields.io/github/stars/manlalaro1/ShopifyF22.svg?style=for-the-badge
[stars-url]: https://github.com/manlalaro1/ShopifyF22/stargazers
[issues-shield]: https://img.shields.io/github/issues/manlalaro1/ShopifyF22.svg?style=for-the-badge
[issues-url]: https://github.com/manlalaro1/ShopifyF22/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/pvtrick-odonnell
