# Wykorzystaj oficjalny obraz Pythona jako bazowy
FROM python:3.9-slim

# Ustaw zmienne środowiskowe, aby Python nie buforował wyjścia
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj pliki aplikacji do katalogu roboczego
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Udostępnij port, na którym aplikacja będzie działać
EXPOSE 5000

# Uruchom aplikację
CMD ["python", "adwcr_app.py"]
