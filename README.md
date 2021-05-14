# Welcome to News Label classification Using Bi-LSTM 👋
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000)
![Documentation](https://img.shields.io/badge/documentation-yes-brightgreen.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Twitter: Manikan31004419](https://img.shields.io/twitter/follow/Manikan09676833.svg?style=social)](https://twitter.com/Manikan09676833)

## Overview
**This is a nlp model that classify the news to their repective label**
eg. Tiger woods won the game -> label - sport

- We have trained the model on AG's News Topic Classification Dataset that contain 1 million article from 20 different news source.
## API ENDPOINT
- http://54.188.107.227/predict
- you can also test this api by provinding parameter like:
![](https://github.com/devil-cyber/asset/blob/main/Screenshot%20from%202021-05-14%2023-12-48.png)

## Bi-LSTM
`As in NLP , sometimes to understand a word we need not just to the previous word , but also to the coming word , like in this example`

![](https://miro.medium.com/max/609/1*wODEqmbZyAPH4lihCgpjdQ.gif)

`Here for the word “Teddy” , we can’t just say whether the next word is gonna be “Bears” or “Roosevelt”, it will depend on the context of the sentence.
Bi-lstm is general architecture that can use any RNN model`

![](https://miro.medium.com/max/609/1*c4yHwRQESwG5e0WsmW-zBw.gif)

`Here we apply forward propagation 2 times , one for the forward cells and one for the backward cells
Both activations(forward , backward) would be considered to calculate the output y^ at time t`

![](https://miro.medium.com/max/700/1*tboMWGjYt0kcA8vdhg2WeQ.jpeg)


## Install

```python

# To get started with this project run following command:
# create enivornment
pip install -r requirements.txt
python run.py

# You can change training parameter in config.py
```


## Run App

```sh
# Before running of app go to api folder and in main.py and remove host='0.0.0.0'
cd api
python main.py

```
## Demo
[![](http://img.youtube.com/vi/da973gTg-9A/0.jpg)](http://www.youtube.com/watch?v=da973gTg-9A "demo")

## Author

👤 **Manikant Kumar**

* Website: https://devil-cyber.github.io/CodingSpace/
* Twitter: [@Manikan31004419](https://twitter.com/Manikan09676833)
* Github: [@devil-cyber](https://github.com/devil-cyber)
* LinkedIn: [@manikant-kumar-550998192](https://linkedin.com/in/manikant-kumar-550998192)

## Show your support

Give a ⭐️ if this project helped you!


***


