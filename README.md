# Flask API Docker

To repozytorium zawiera prostą aplikację Flask, która została skonteneryzowana za pomocą Docker.

## Jak uruchomić

1. Zbuduj obraz Dockera:
   ```bash
   docker build -t flask-api https://github.com/konchrab02/flask-api-docker-adwcr.git
2. Uruchom kontener:
   ```bash
   docker run -p 5005:5000 --name your-name flask-api 
