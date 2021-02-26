## Machine Learning model END-to-END API

END-to-END machine learning model built on iris dataset

- api will be up on url `http://localhost:8000/`
- to get predition `POST` data point(single) to `http://localhost:8000/predict` in the format `{'data': [int,...]}`
- curl example: `curl -d '{"body":[1,2,3,4]}' -H 'Content-Type: application/json' http://localhost:8000/predict`

To run the application
- clone the repo
- run `python api.py`