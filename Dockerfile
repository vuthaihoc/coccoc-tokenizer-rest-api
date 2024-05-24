FROM python:3-alpine

WORKDIR /app

RUN apk update && apk add --no-cache gcc libc-dev make git cmake build-base pkgconfig

RUN pip install Cython flask

RUN git clone https://github.com/duydo/coccoc-tokenizer.git
RUN cd coccoc-tokenizer && mkdir build && cd build && cmake .. -DBUILD_PYTHON=1 && make install
RUN mkdir /usr/share/tokenizer && cp -r /usr/local/share/tokenizer/dicts /usr/share/tokenizer/dicts

WORKDIR /app
COPY ./app.py /app/app.py

EXPOSE 8000

ENTRYPOINT ["python"]
CMD ["/app/app.py"]