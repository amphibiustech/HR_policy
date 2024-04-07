FROM python:3.12-bookworm
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV Name policy
EXPOSE 5000
CMD [ "streamlit","run","policy.py" ]