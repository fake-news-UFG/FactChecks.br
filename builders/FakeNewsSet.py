# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""FakeNewsSet"""


import csv
import os

import datasets


_CITATION = """\
@inproceedings{10.1145/3428658.3430965,
  author = {da Silva, Fl\'{a}vio Roberto Matias and Freire, Paulo M\'{a}rcio Souza and de Souza, Marcelo Pereira and de A. B. Plenamente, Gustavo and Goldschmidt, Ronaldo Ribeiro},
  title = {FakeNewsSetGen: A Process to Build Datasets That Support Comparison Among Fake News Detection Methods},
  year = {2020},
  isbn = {9781450381963},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  url = {https://doi.org/10.1145/3428658.3430965},
  doi = {10.1145/3428658.3430965},
  abstract = {Due to easy access and low cost, social media online news consumption has increased significantly for the last decade. Despite their benefits, some social media allow anyone to post news with intense spreading power, which amplifies an old problem: the dissemination of Fake News. In the face of this scenario, several machine learning-based methods to automatically detect Fake News (MLFN) have been proposed. All of them require datasets to train and evaluate their detection models. Although recent MLFN were designed to consider data regarding the news propagation on social media, most of the few available datasets do not contain this kind of data. Hence, comparing the performances amid those recent MLFN and the others is restricted to a very limited number of datasets. Moreover, all existing datasets with propagation data do not contain news in Portuguese, which impairs the evaluation of the MLFN in this language. Thus, this work proposes FakeNewsSetGen, a process that builds Fake News datasets that contain news propagation data and support comparison amid the state-of-the-art MLFN. FakeNewsSetGen's software engineering process was guided to include all kind of data required by the existing MLFN. In order to illustrate FakeNewsSetGen's viability and adequacy, a case study was carried out. It encompassed the implementation of a FakeNewsSetGen prototype and the application of this prototype to create a dataset called FakeNewsSet, with news in Portuguese. Five MLFN with different kind of data requirements (two of them demanding news propagation data) were applied to FakeNewsSet and compared, demonstrating the potential use of both the proposed process and the created dataset.},
  booktitle = {Proceedings of the Brazilian Symposium on Multimedia and the Web},
  pages = {241–248},
  numpages = {8},
  keywords = {Fake News detection, Dataset building process, social media},
  location = {S\~{a}o Lu\'{\i}s, Brazil},
  series = {WebMedia '20}
}
"""

# TODO: Add description of the dataset here
_DESCRIPTION = """\
"""

# TODO: Add a link to an official homepage for the dataset here
_HOMEPAGE = ""


_LICENSE = "https://raw.githubusercontent.com/kamplus/FakeNewsSetGen/master/LICENSE"

_URLS = {
    "fake": "https://github.com/kamplus/FakeNewsSetGen/raw/master/Dataset/News_fake.csv",
    "notFake": "https://github.com/kamplus/FakeNewsSetGen/raw/master/Dataset/News_notFake.csv",
}


class FakeNewsSet(datasets.GeneratorBasedBuilder):
    """TODO: Short description of my dataset."""

    VERSION = datasets.Version("1.0.0")

    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name="default",
            version=VERSION,
        ),
    ]

    DEFAULT_CONFIG_NAME = "default"

    def _info(self):
        features = datasets.Features(
            {
                "id": datasets.Value("string"),
                "news_url": datasets.Value("string"),
                "title": datasets.Value("string"),
                "tweet_ids": datasets.Sequence(
                    feature=datasets.Value(dtype="string", id=None)
                ),
                "label": datasets.ClassLabel(num_classes=2, names=["fake", "notFake"]),
            }
        )

        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        urls = _URLS
        filepaths = {key: dl_manager.download(urls[key]) for key in urls}
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    "filepaths": filepaths,
                },
            ),
        ]

    def _generate_examples(self, filepaths):
        for label, filepath in filepaths.items():
            with open(filepath, encoding="utf-8") as f:
                names = next(csv.reader(f))
                names[0] = "id"
                for row in csv.reader(f):
                    row_data = dict(zip(names, row))

                    key = row_data["id"]
                    row_data["label"] = label
                    row_data["tweet_ids"] = row_data["tweet_ids"].split("\t")

                    yield key, row_data
