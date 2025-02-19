FROM python:3.10-alpine
ADD server.py .
RUN ls -l
#installazione flask
RUN pip install flask
#creazione file l'html e della cartella templates 
RUN mkdir templates
ADD ./templates/index.html ./templates
ADD ./templates/index2.html ./templates
#manca mapping tra le porte

CMD ["python","./server.py"]