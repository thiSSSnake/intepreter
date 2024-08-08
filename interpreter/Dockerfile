FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /

# Копируем скрипт, который будет выполнять код
COPY execute_code.py /execute_code.py

# Copy requirements.txt
COPY ./requirements.txt ./

# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
RUN pip install -r requirements.txt

# Устанавливаем команду по умолчанию
CMD ["python", "/execute_code.py"]