# Coccoc Tokenizer Simple Rest Api


Use python to warap coccoc_tokenizer and serve as service

```
http://localhost:1880/tokenize?text=Ông Hun Sen: Một số quốc gia từng mắc sai lầm khi ủng hộ Khmer Đỏ
```



## Usage

- Clone this repo
- Run `docker compose up -d` 
- Test 

```
curl http://localhost:1880/tokenize?text=%C3%94ng%20Hun%20Sen:%20M%E1%BB%99t%20s%E1%BB%91%20qu%E1%BB%91c%20gia%20t%E1%BB%ABng%20m%E1%BA%AFc%20sai%20l%E1%BA%A7m%20khi%20%E1%BB%A7ng%20h%E1%BB%99%20Khmer%20%C4%90%E1%BB%8F
```