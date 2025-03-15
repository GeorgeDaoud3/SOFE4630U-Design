FROM pytorch/pytorch:2.4.0-cuda12.4-cudnn9-devel
RUN pip install google-cloud-pubsub
COPY *.json .
COPY *.pkl .
ADD main.py .
CMD ["python","-u", "./main.py"] 
