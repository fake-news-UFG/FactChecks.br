<br />
<div align="center">
    <h2 align="center">FactChecks.br</h2>
    <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/28462295/262658173-2c1c5913-62ad-4ad3-945e-6574f5240d60.png" alt="https://www.flaticon.com/free-icon/detective_695826" width="250">
    <br />
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/fake-news-UFG/FactChecks.br">
  <img alt="GitHub" src="https://img.shields.io/github/license/fake-news-UFG/FactChecks.br">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/fake-news-UFG/FactChecks.br?style=social">
  <p align="center">
  <b>
    Collection of Portuguese Fact-Checking Benchmarks.
  </b>
  </p>
</div>

## Getting Started

| Nome | Tipo | Veículo | Anotado | Ano dos dados | Tamanho pós-processamento |
| --- | --- | --- | --- | --- | --- |
| [Fake.br](https://sites.icmc.usp.br/taspardo/PROPOR2018-MonteiroEtAl.pdf) | Alegação | Notícias | Manual | 01/2016 - 01/2018 | 7.200 |
| [FakeRecogna](https://dl.acm.org/doi/10.1145/3428658.3430965) | Fonte | Notícias | Agências | 03/2017  - 05/2020 | 11.902 |
| [Central de Fatos](https://sol.sbc.org.br/index.php/dsw/article/view/17421/17257) | Fonte | Notícias | Agências | 01/2013 - 05/2021 | 10.551 |
| [Fact-check_tweet (pt split)](https://ceur-ws.org/Vol-3199/) | Par | Tweets-Notícias | Auto-Agências | 2019 - 2021 | 803 - 803 |
| [FakeNewsSet](https://dl.acm.org/doi/10.1145/3428658.3430965) | Par | Tweets-Notícias | Auto-Agências |  | 27.059 - 600 |

## Usage 🤗

```python
from datasets import load_dataset

data = load_dataset("fake-news-UFG/FactChecks.br")
```

## Scripts

- Notebook generation script and EDA is located at [process.ipynb](process.ipynb).
- Builder scripts for Dataset Hub are located at [builders/](builders/).

## Data Analysis
![image](https://github.com/fake-news-UFG/FactChecks.br/assets/28462295/d3dc1ed5-aae9-488c-9564-adfa460554c0)


## Citing

## Acknowledgments

