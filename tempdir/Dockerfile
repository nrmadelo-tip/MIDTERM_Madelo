FROM python
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY midterm_app.py /home/myapp/
COPY requirements.txt /home/myapp/
RUN pip install -r /home/myapp/requirements.txt
EXPOSE 5000
CMD python3 /home/myapp/midterm_app.py
FROM python
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY midterm_app.py /home/myapp/
COPY requirements.txt /home/myapp/
RUN pip install -r /home/myapp/requirements.txt
EXPOSE 5000
CMD python3 /home/myapp/midterm_app.py
