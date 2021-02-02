# COLX 585 Trends in Computational Linguistic
## Lab tutorial 4: Implementation of Fairseq

[Fairseq(-py)](https://github.com/pytorch/fairseq) is a sequence modeling toolkit that allows researchers and developers to train custom models for translation, summarization, language modeling and other text generation tasks.

You can use Fairseq to implement many state-of-the-art deep learning architectures such as BERT, wav2vec, and BART. Fairseq provides several [command-line tools](https://fairseq.readthedocs.io/en/latest/command_line_tools.html#fairseq-interactive) for training and evaluating models. 

You can install the Fairseq by 
```
pip install fairseq
```
We provide an example to train a Transformer model with the Fairseq tool in this tutorial.

In this tutorial, the dataset we'll be using is the [Multi30k](https://github.com/multi30k/dataset) dataset that includes ~30,000 parallel English, French and German sentences. The length of the sentence is around 12 words. You can find more information in [WMT18](http://www.statmt.org/wmt18/multimodal-task.html). This corpus was officially split to training (29,000 sentences), Validation (1,014 sentences), and multiple Test sets. We provide Test 2016 (1,000 sentences). 

You can find the dataset in the subdirectory `./fr-en/`. This subdirectory includes 6 files. The prefix indicates the type of dataset, like train, val, and test_2016_flickr. The suffix indicates the language, `fr` for French and `en` for English. 

We use the command-line tools to pre-process data and train our models. Hence, you should use your Terminal or Cygwin to run the following codes. 

#### Pre-process
First, we pre-process the datasets using [fairseq-preprocess](https://fairseq.readthedocs.io/en/latest/command_line_tools.html#fairseq-preprocess). 

The sample command is in `fairseq-preprocess.sh` file. We provide the suffix names of source and target languages, directory to the datasets, and the destination directory. You can investigate other optional arguments of `fairseq-preprocess` [here](https://fairseq.readthedocs.io/en/latest/command_line_tools.html#Preprocessing). 

#### Train
When you get pre-processed datasets, you can use [fairseq-train](https://fairseq.readthedocs.io/en/latest/command_line_tools.html#fairseq-train) to train your model from scratch. 

File `fairseq-train.sh` provides an example to train a big Transformer from scratch. We specify some arguments to control the hyper-parameters of the modeling. For example:
- `--arch` indicates the `Model Architecture`, you can find the possible choices [here](https://fairseq.readthedocs.io/en/latest/command_line_tools.html#Model%20configuration)
- `--optimizer` selects the type of optimizer.
- `--batch-size` sets the number of batch size.
- `--max-epoch` sets the number of epochs. 

Fairseq-train will create a subdirectory `checkpoint` and save checkpoint at the end of each epoch automatically. 

#### Use Pre-trained Models
Fairseq not only helps train a model from scratch but also offers many pre-trained models. You can find more information [here](https://fairseq.readthedocs.io/en/latest/getting_started.html). 

You can find more training and evaluating examples [here](https://github.com/pytorch/fairseq/tree/master/examples).

#### Google Cloud 
If you want to train a model with Fairseq, you can use [Google Cloud](https://cloud.google.com/) that offer a powerful compute infrastructure. You can also train [a Transformer with TPUs](https://cloud.google.com/tpu/docs/tutorials/transformer-pytorch) on Google Cloud. 

#### Reference:
- https://github.com/pytorch/fairseq
- https://cloud.google.com/
- https://cloud.google.com/tpu/docs/tutorials/transformer-pytorch
- https://www.youtube.com/watch?v=zEOtG-ChmZE