FROM python:3.9 
RUN pip install google-cloud-pubsub
RUN apt-get update && apt-get upgrade -y && apt-get install -y git 
RUN git clone https://github.com/apple/ml-depth-pro.git 
RUN pip install -e ml-depth-pro/.
RUN . ml-depth-pro/get_pretrained_models.sh
COPY *.json .
COPY *.png .
ADD main.py . 
CMD ["python","-u", "./main.py"] 