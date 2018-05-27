# store
Sample project, using django and django rest framework
### Install
1. Create virtualenv ``python3 -m venv {name}``
2. Start your env ``source bin activate``
3. Install requirements ``pip install -r requirements.txt``
4. Run migrates ``python manage.py migrate``
5. Start app ``python manage.py runserver``
## End Points

### Login

```
curl -X POST \
  http://127.0.0.1:8000/api-token-auth/ \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: 423bed3d-1c03-41bb-8ea3-272d4882f97c' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F username=admin \
  -F 'password =admin123123'
```

### Items

```
curl -X GET \
  http://127.0.0.1:8000/api/items/ \
  -H 'Authorization: Bearer 3960649ff9574ddb470c062c25ef6734085f183d' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: ed5dc877-7d4c-4272-9d71-929aa1fcb81b'
```

### Cart

```
curl -X GET \
  http://127.0.0.1:8000/api/cart/ \
  -H 'Authorization: Token b4ad79d96f88c0a8eb1d594a5844113a59daeb4a' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: 434079c1-74b0-442b-bea9-1e689d83b1ae'
```
```
curl -X POST \
  http://127.0.0.1:8000/api/add/item/ \
  -H 'Authorization: Token b4ad79d96f88c0a8eb1d594a5844113a59daeb4a' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: e704c3c1-e9dc-482d-bc3c-70482606514b' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F item=7
```
```
curl -X POST \
  http://127.0.0.1:8000/api/remove/item/ \
  -H 'Authorization: Token b4ad79d96f88c0a8eb1d594a5844113a59daeb4a' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: 95053863-4cea-43f4-9918-fea01ca511fc' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F item=1
```

### Order

```
curl -X GET \
  http://127.0.0.1:8000/api/order/ \
  -H 'Authorization: Token b4ad79d96f88c0a8eb1d594a5844113a59daeb4a' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: d1f11c7b-0094-419f-84f1-62d2c784caf6' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F item=1
```
```
curl -X POST \
  http://127.0.0.1:8000/api/create/order/ \
  -H 'Authorization: Token b4ad79d96f88c0a8eb1d594a5844113a59daeb4a' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: ed7e77e7-eb35-496b-b978-c50806728bf0'
```