FROM python:3.8
RUN apt-get update
RUN apt-get install texlive-latex-base -y && apt-get install graphviz -y
RUN mkdir artifacts/
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install -i https://test.pypi.org/simple/ buildast-new==1.0.0
COPY main.py main.py
CMD [ "python3", "main.py"]