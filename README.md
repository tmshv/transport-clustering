# Кластеризация изображений транспортных средств.

## ОПИСАНИЕ ЗАДАЧИ

Даны изображения транспортных средств различных типов и с разных ракурсов.
Для каждого изображения есть вектора признаков (дескрипторы), полученные с помощью разных глубоких моделей.

Задача состоит в том, чтобы, используя дескрипторы, разбить изображения на кластеры и проинтерпретировать каждый из них.
Для всех вариантов дескрипторов нужно применить несколько алгоритмов кластеризации и сравнить полученные результаты.
Сравнивать можно по метрикам и по тому, насколько кластера хорошо интерпретируются.

Дополнительным плюсом будет, если среди изображений будут выделены выбросы.
Это могут быть изображения плохого качества, изображения, на которых нет транспортных средств и т.д.

В качестве результата должен быть представлен jupyter notebook с ходом решения, анализом и интерпретацией,
а также csv файл с лучшей разбивкой на кластеры и выбросы.

## ЗАДАНИЯ

A. Для каждого типа дескрипторов необходимо:
1. Сделать кластеризацию, подобрав алгоритм и параметры кластеризации
(рекомендуется ориентироваться на внутренние метрики*, интерпретируемость и визуализацию).
2. Выделить выбросы (данные сильно отличающиеся от основной масссы данных).
2. Сделать визуализацию в 2d или 3d.
3. Проинтерпретировать полученные кластеры (пару предложений о том какие картинки попали в кластер)

B. Полученные кластеризации для каждого типа дескрипторов сравнить между собой (по метрикам, визуализации и по результатам интерпретации)

С. Попробовать другие дескрипторы или смесь дескрипторов.

* `calinski_harabasz_score`, `davies_bouldin_score`

## MODELS

- `efficientnet-b7` - модель классификации изображений Imagenet на 1000 классов, softmax loss, обучена на Imagenet, не видела датасет veriwild
- `type_model` - модель классификации транспортных средств по типу на 10 классов, softmax loss,  частично обучена на veriwild
- `color_model` - модель регрессии для определения цвета транспортных средств в формате RGB, mse loss, частично обучена на veriwild
- `osnet`- модель *reid людей, животных и машин, softmax loss, не видела датасет veriwild

## Установка и настройка

```sh
pip3 install -r requirements.txt
```

1. Put your data

Папка должна находиться на одном уровне с `create_dataset.py`. Внутри папки `raw_data/veriwild/veriwild/....`. Ее нужно скачать на [странице](https://www.notion.so/Intellivision-fd429538b10b4151aece69d16901095c)

2. Create dataset

```py
python3 create_dataset.py
```

на выходе должен получиться `transport_dataset.csv`.

Далее работаем с файлом `transport_clustering.ipynb`


## link to Notebooks

- https://www.kaggle.com/itslek/easy-start-with-fastai-sf-car-classification-v26
- https://www.kaggle.com/brunorazeramoretti1/eda-atividade-pr-tica
- https://www.kaggle.com/sohamtiwari/car-classfication
- https://www.kaggle.com/alexeybelomoykin/belomoykin-dst-18-keras-car-class
- https://www.kaggle.com/dmitry89/ford-vs-ferrari-dst-9-19-fullsuccess
- https://www.kaggle.com/sokolovaleks/sf-dst-10-car-classification-sokolov
- https://www.kaggle.com/romanianvarev/sf-dl-car-classificator-efficientnetb4

Цветовая классификация

https://www.kaggle.com/ashutoshvarma/image-classification-using-svm-92-accuracy

