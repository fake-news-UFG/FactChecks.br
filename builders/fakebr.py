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
"""Fake.br dataset"""


import os
from pprint import pprint

import datasets


_CITATION = """\
@article{silva:20,
  title = "Towards automatically filtering fake news in Portuguese",
  journal = "Expert Systems with Applications",
  volume = "146",
  pages = "113199",
  year = "2020",
  issn = "0957-4174",
  doi = "https://doi.org/10.1016/j.eswa.2020.113199",
  url = "http://www.sciencedirect.com/science/article/pii/S0957417420300257",
  author = "Renato M. Silva and Roney L.S. Santos and Tiago A. Almeida and Thiago A.S. Pardo",
}
"""


_DESCRIPTION = """\
Fake.Br Corpus is composed of aligned true and fake news written in Brazilian Portuguese.
"""

_HOMEPAGE = "https://github.com/roneysco/Fake.br-Corpus"

# TODO: Add the licence for the dataset here if you can find it
_LICENSE = ""


_URL = "https://github.com/roneysco/Fake.br-Corpus/archive/refs/heads/master.zip"

# column names in metadata texts
_METADATA_COLS = [
    "author",
    "link",
    "category",
    "date of publication",
    "number of tokens",
    "number of words without punctuation",
    "number of types",
    "number of links inside the news",
    "number of words in upper case",
    "number of verbs",
    "number of subjuntive and imperative verbs",
    "number of nouns",
    "number of adjectives",
    "number of adverbs",
    "number of modal verbs (mainly auxiliary verbs)",
    "number of singular first and second personal pronouns",
    "number of plural first personal pronouns",
    "number of pronouns",
    "pausality",
    "number of characters",
    "average sentence length",
    "average word length",
    "percentage of news with speeling errors",
    "emotiveness",
    "diversity",
]


class Fakebr(datasets.GeneratorBasedBuilder):
    """Fake.Br Corpus is composed of aligned true and fake news written in Brazilian Portuguese."""

    VERSION = datasets.Version("1.0.0")

    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name="full_texts",
            version=VERSION,
            description="full texts, as collected from their websites",
        ),
        datasets.BuilderConfig(
            name="size_normalized_texts",
            version=VERSION,
            description="in each fake-true pair, the longer text is truncated (in number of words) to the size of the shorter text",
        ),
    ]

    DEFAULT_CONFIG_NAME = "full_texts"

    def _info(self):
        if self.config.name == "full_texts":
            features = datasets.Features(
                {
                    "text": datasets.Value("string"),
                    "label": datasets.ClassLabel(num_classes=2, names=["fake", "true"]),
                    "author": datasets.Value("string"),
                    "link": datasets.Value("string"),
                    "category": datasets.Value("string"),
                    "date of publication": datasets.Value("string"),
                    "number of tokens": datasets.Value("int32"),
                    "number of words without punctuation": datasets.Value("int32"),
                    "number of types": datasets.Value("int32"),
                    "number of links inside the news": datasets.Value("int32"),
                    "number of words in upper case": datasets.Value("int32"),
                    "number of verbs": datasets.Value("int32"),
                    "number of subjuntive and imperative verbs": datasets.Value(
                        "int32"
                    ),
                    "number of nouns": datasets.Value("int32"),
                    "number of adjectives": datasets.Value("int32"),
                    "number of adverbs": datasets.Value("int32"),
                    "number of modal verbs (mainly auxiliary verbs)": datasets.Value(
                        "int32"
                    ),
                    "number of singular first and second personal pronouns": datasets.Value(
                        "int32"
                    ),
                    "number of plural first personal pronouns": datasets.Value("int32"),
                    "number of pronouns": datasets.Value("int32"),
                    "pausality": datasets.Value("float"),
                    "number of characters": datasets.Value("int32"),
                    "average sentence length": datasets.Value("float"),
                    "average word length": datasets.Value("float"),
                    "percentage of news with speeling errors": datasets.Value("float"),
                    "emotiveness": datasets.Value("float"),
                    "diversity": datasets.Value("float"),
                }
            )
        elif self.config.name == "size_normalized_texts":
            features = datasets.Features(
                {
                    "text": datasets.Value("string"),
                    "label": datasets.ClassLabel(num_classes=2, names=["fake", "true"]),
                }
            )
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            supervised_keys=("text", "label"),
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        urls = _URL
        data_dir = dl_manager.download_and_extract(urls)
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    "data_dir": os.path.join(data_dir, "Fake.br-Corpus-master"),
                },
            ),
        ]

    def _generate_examples(self, data_dir):
        config_dir = os.path.join(data_dir, self.config.name)

        for label in ["fake", "true"]:
            label_dir = os.path.join(config_dir, label)

            for example in os.listdir(label_dir):
                key = label + "_" + example.replace(".txt", "")
                example_path = os.path.join(label_dir, example)

                with open(example_path, "r") as f:
                    text = f.read()

                row = {"text": text, "label": label}

                if self.config.name == "full_texts":
                    metadata_path = os.path.join(
                        config_dir,
                        f"{label}-meta-information",
                        example.replace(".txt", "-meta.txt"),
                    )

                    with open(metadata_path, "r") as f:
                        metadata = f.read().split("\n")

                    metadata = dict(zip(_METADATA_COLS, metadata))

                    if metadata["author"] == "None":
                        metadata["author"] = ""

                    if metadata["number of links inside the news"] == "None":
                        metadata["number of links inside the news"] = "0"

                    row.update(metadata)

                yield key, row
