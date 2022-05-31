FROM continuumio/anaconda3:latest

WORKDIR /coloryt-exercise

COPY reqiurements.txt reqiurements.txt
RUN pip install -r reqiurements.txt

COPY . .

EXPOSE 8889

ENTRYPOINT ["jupyter", \
            "notebook", \
            "--notebook-dir=/coloryt-exercise", \
            "--ip=0.0.0.0", \
            "--port=8889",\
            "--no-browser",\
             "--allow-root"]