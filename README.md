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

| Dataset | Type | Domain | Anotation | Data time | Number of samples |
| --- | --- | --- | --- | --- | --- |
| [Fake.br](https://sites.icmc.usp.br/taspardo/PROPOR2018-MonteiroEtAl.pdf) | Claim | News | Annotated | 01/2016 - 01/2018 | 7.200 |
| [FakeRecogna](https://dl.acm.org/doi/10.1145/3428658.3430965) | Source | News | Agency | 03/2017  - 05/2020 | 11.773 |
| [Central de Fatos](https://sol.sbc.org.br/index.php/dsw/article/view/17421/17257) | Source | News | Agency | 01/2013 - 05/2021 | 10.461 |
| [Fact-check_tweet (pt split)](https://ceur-ws.org/Vol-3199/) | Claim-source pair | Tweets-Notícias | Auto-Agency | 2019 - 2021 | 656 - 656 |
| [FakeNewsSet](https://dl.acm.org/doi/10.1145/3428658.3430965) | Claim-source pair | Tweets-Notícias | Auto-Agencys |  | 26.970 - 598 |

## Usage 🤗

```python
from datasets import load_dataset

data = load_dataset("fake-news-UFG/FactChecksbr")
```
We addionally upload raw versions from [Fake.br](https://huggingface.co/datasets/fake-news-UFG/fakebr), [FakeRecogna](https://huggingface.co/datasets/fake-news-UFG/FakeRecogna), [Central de Fatos](https://huggingface.co/datasets/fake-news-UFG/central_de_fatos), and [FakeNewsSet](fake-news-UFG/FakeNewsSet).

Review urls were tagged using review id.

## Scripts

- Notebook generation script and EDA is located at [process.ipynb](process.ipynb).
- Builder scripts for Dataset Hub are located at [builders/](builders/).

## Data Analysis

#### Agencies per dataset
![image](https://github.com/fake-news-UFG/FactChecks.br/assets/28462295/9f0cb6ce-451d-45a4-ad37-bc930dc043c6)


### Duplication
There are 23,467 sources in total, of which there are 20,028 unique sources. The biggest overlap is between "FakeRecogna" and "Central de Fatos".
There is no source in common between all datasets. 

From 3303 duplicated sources,  we excluded 130 contradictory examples, in which one dataset indicates that source alledges “fake” while not alledges as "not fake".

![image](https://github.com/fake-news-UFG/FactChecks.br/assets/28462295/72e9e78f-4913-4d54-9403-8090edb97631)

### Samples per class
![image](https://github.com/fake-news-UFG/FactChecks.br/assets/28462295/40de40a7-d331-4ac5-8bca-68795110d719)

## Evaluation
If you evaluated any dataset, please feel free to pull a request. :smile:

| Dataset          | Model                          | Accuracy | Precision | Recall | macro-F1 | URL                                                                                                        |
| ---------------- | ------------------------------- | -------- | -------- | -------- | -------- | ----------------------------------------------------------------------------------------------------------- |
| Fake.br          | Bertimbau                       | 99,22%   | \-       | \-       | \-       | [repo](https://github.com/Talendar/br_fake_news_detection)                                           |
| Fake.Br          | GloVe 100-600D - HAN            | 97%      | \-       | \-       | \-       | [paper](https://link.springer.com/chapter/10.1007/978-3-030-41505-1_14)                                    |
| Fake.br          | Bertimbau + Regressão Logística | 96,14%   | 96,40%   | 95,49%   | 96,13%   | [paper](https://repositorio.unifesp.br/bitstream/handle/11600/63501/TCC2_FINAL.pdf?sequence=1&isAllowed=y) |
| Fake.Br          | BoW                             | 96%      | \-       | \-       | \-       | [paper](https://sites.icmc.usp.br/taspardo/PROPOR2018-MonteiroEtAl.pdf)                                    |
| Fake.br          | GloVe 100D + BiLSTM             | 93.56%   | \-       | \-       | \-       | [repo](https://github.com/Talendar/br_fake_news_detection)                                           |
| Fake.br          | TfidfVectorizer                 | 92,85%   | 92,19%   | 93,36%   | \-       | [repo](https://github.com/brauliotegui/FAKE)                                                         |
| Fake.BR          | BoW                             | 89%      | 89%      | 89%      | 89%      | [paper](https://sites.icmc.usp.br/taspardo/PROPOR2018-MonteiroEtAl.pdf)                                    |
| Fake.br          | BoW + MLP                       | 88,65%   | \-       | \-       | \-       | [repo](https://github.com/Talendar/br_fake_news_detection)                                           |
| FakeNewsSetGen   | Detective                       | 97,93%   | 97,93%   | \-       | \-       | [repo](https://github.com/kamplus/FakeNewsSetGen)                                                    |
| Fact-check_tweet | XLM-R                           | 84,08%   | \-       | \-       | 83,63%   | [paper](https://arxiv.org/pdf/2202.07094.pdf)                                                              |
| FakeRecogna    | MLP + BoW                       | 93,1%    | 93,1%    | 93,1%    | 93,0%    | [repo](https://github.com/Gabriel-Lino-Garcia/FakeRecogna)   

## Citing
```bibtex
@misc{FactChecksbr,
author = {R. S. Gomes, Juliana},
title = {FactChecks.br},
url = {https://github.com/fake-news-UFG/FactChecks.br},
doi = { 10.57967/hf/1016 },
}
```

## Acknowledgments

