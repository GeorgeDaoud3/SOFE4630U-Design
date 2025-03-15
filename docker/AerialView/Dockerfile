FROM python:3.9 
RUN pip install google-cloud-pubsub opencv-python numpy matplotlib
RUN apt update && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1
COPY *.json .
COPY *.png .
ADD main.py . 
CMD ["python","-u", "./main.py"] 
