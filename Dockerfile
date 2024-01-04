FROM python:3.9.18-bookworm
WORKDIR /CVEfixes
COPY . .
RUN pip install -r requirements.txt
CMD ["sh", "./Code/create_CVEfixes_from_scratch.sh"]