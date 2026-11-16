# ReCaSR

## Dataset Preparation

### MM-IMDb

Download the dataset from [MM-IMDb](https://archive.org/download/mmimdb/mmimdb.tar.gz).

After extraction, organize the files as follows:

- Images: `dataset/mmimdb/image/`
- JSON metadata: `dataset/mmimdb/meta_data/`

### Hateful Memes

Download the dataset from [Facebook Hateful Meme Dataset](https://www.kaggle.com/datasets/parthplc/facebook-hateful-meme-dataset).

Organize the files as follows:

- Images: `dataset/hatememes/image/`
- JSON metadata: `dataset/hatememes/metadata/`

For evaluation, obtain the labeled `test_seen.json` from [Hateful Memes](https://www.kaggle.com/datasets/williamberrios/hateful-memes) and use it to replace `dataset/hatememes/metadata/test.json`, saving it under the name `test.json`. The test metadata from the first download does not contain the labels required for evaluation.

Only replace the test metadata file; keep the training and validation files unchanged. Ensure that the images referenced by the replacement file are available in the image directory.

### Food101 (UPMC Food-101)

Download the multimodal dataset from [UPMC-Food101](https://www.kaggle.com/datasets/gianmarco96/upmcfood101).

Organize the files as follows:

- Images: `dataset/food101/image/`
- CSV metadata: `dataset/food101/meta_data/`

For the three datasets above, place image files directly in their respective `image/` directories and preserve their original filenames. The expected path format is:

```text
dataset/<dataset_name>/image/<filename>.jpg
dataset/<dataset_name>/image/<filename>.png
dataset/<dataset_name>/image/<filename>.jpeg
```

### MIRFlickr25K

Download `mirflickr25k.zip` and `mirflickr25k_annotations_v080.zip` from the [official download page](https://press.liacs.nl/mirflickr/mirdownload.html). These archives provide the images, associated tags, and class annotations.

Prepare the cleaned subset using the [preprocessing repository](https://github.com/iTomxy/data/tree/master/flickr25k) and its [cleaning guide](https://blog.csdn.net/HackerTom/article/details/98477506). The procedure excludes samples with empty processed tag vectors or no class labels, retaining **20,015 samples**.

Use the retained sample indices to select the corresponding images, tags, and labels, keeping them aligned throughout preprocessing. In the cleaning guide, these indices are saved as `clean_id.npy` and are **zero-based**: index `i` corresponds to the original image ID `i + 1`, whose filename is `im<i+1>.jpg`.
