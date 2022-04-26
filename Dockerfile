
FROM python
WORKDIR /app 
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . . 
EXPOSE 5001
EXPOSE 5432
CMD ["python", "hello.py"] 
