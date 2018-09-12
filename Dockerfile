FROM i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7:latest

RUN pip3 install kau3-tian2_iong7-ji7
WORKDIR /opt
COPY . .
RUN python3 twisas_trs.py

CMD cat twisas-HL-kaldi-pun.json
 
