FROM ultralytics/ultralytics:latest
RUN pip install google-cloud-pubsub opencv-python
RUN apt-get install wget 
RUN wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt
COPY *.json .
COPY *.png .
ADD main.py .
CMD ["python","-u", "./main.py"] 