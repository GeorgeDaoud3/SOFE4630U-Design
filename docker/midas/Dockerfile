FROM pytorch/pytorch:1.13.0-cuda11.6-cudnn8-runtime
RUN pip install google-cloud-pubsub   opencv-python timm
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY *.json .
COPY *.png .
ADD main.py .
CMD ["python","-u", "./main.py"] 