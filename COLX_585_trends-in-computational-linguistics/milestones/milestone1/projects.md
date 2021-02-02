# COLX-585 projects

### General guidelines about using other people's code
Feel free to use other people's code, but you ``M U S T``:
* Credit other people, and provide documentation/references/links to their repos
* Understand how the code works
* Have some other type of contribution(s). In other words, it is not sufficient for your project to just run someone else's code on the data and submit your results. Your other contribution(s) could be doing analysis of your results, comparisons of different methods, critique of the methods, deriving useful insights and interpretations of project outcome, etc. Please reade milestone 1 *very carefully* for more information.
* If you are not sure or have questions, please feel free to the instructor and/or TAs during their office hours. 

---
# COVID-19 PROJECTS
This is a cluser of projects around the theme of COVID-19. You could pick one of these, or perhaps they will inspire a new project idea you may like to propose for a project. For the following, we will provide a somewhat detailed description for the first two projects, as a way to walk you through what could be done. The same lines of thought, procedures, etc. could be extended to the rest of the projects within the COVID-19 Projects Cluster. 

## COVID-19 Sentiment Analysis
* Sentiment Analysis of COVID-19 social media data within (1) a certain location and/or (2) about certain topics.
The ``location``, for example, can involve North American, European, and Asian countries or cities. The ``topics``, for example, could include health, family, politics, school, etc.
* For this project, you could collect Twitter data from one or more countries or cities. Some people use hashtags to do that, or put a bounding box around a certain city or country for a given period of time. 
* The project could involve: (1) building a deep learning sentiment analysis system using some of the data (if you decide to annotate some of it) or using already labeled and available sentiment analysis data and (2) running the system on the collected Twitter data to perform some analysis. 
* The project could provide some insights. For example, what are people's sentiments toward politicians within certain locations? How do people feel about basic services, supply (e.g., grocery), health care system? There will be many such questions the project can explore.

* Notes: 
- If you need some data to get started, please ask and we will make available some general, English language Twitter dataset from the past 2-3 months (~ 1 million tweets, with no specific location), but you may want to augment the data or collect your own.
- If you need a labeled sentiment analysis dataset to train on, please ask and we will provide some English Twitter data.
- It will probably make your work interesting if you apply on more than one language (2 may be enough, but it's your decision)

## COVID-19 Racism & Hate Speech
* As you are probably aware, there is a lot of racism and hate speech associated with COVID-19. This type of toxic language can trigger harmful real-world events, and so this project can seek to detect when such language is used on social media. The goal will be to help a platform to monitor and regulate their content (assume you are working in one of these tech companies and you are tasked to build such a system). 
* The project can also seek to quantify the scale of racist and hateful speech online as it associates with COVID-19. The developed system can be run on data from a given time stamp (say 1 specific month) to carry out such quantification. 
* Data: You could identify certain trigger words or hashtags associated with racist and hateful speech and use these as seeds to collect tweets, for example. You may need to manually verify on a subset of the data that the tweets actually express this type of language. 
* You could then build models to assign a tag from the set {``hateful``, ``racist``, ``not-related``} on the sentence/tweet level. ``Not-related`` here means neither hateful nor racist.
* You could further look at the profiles of people who express hate and/or racism and try to gain more insights about their backgrounds, political affiliations, etc. 


## COVID-19 Misinformation
* Collect a number of fake stories about COVID-19, crawl data related to these fake stories
* On a subset of the data, manually verify whether the sentence/story/tweet is ``fake`` or ``legitimate``. 
* Build a model that would take a sentence/story/tweet ans automatically assign it a tage from the set {``fake``, ``legitimate``}.

Another idea:

* Create synthetic data using the scientific literature (possibly from this source) by e.g., replacing names of ceryain chemicals causing certain problems, effects, etc. with other words.
* Build a system that identifies whether the data (at the sentence level) is fake or not

## COVID-19 Tweet Intent
* Given a tweet, what is it trying to achieve. Is it spam/marketing, question, sharing medical information, complaining about resources (groceries), etc.
* Here you will need to identify a set of tags (or what is usually referred to as a ``code-book``) to assign each tweet. Some tweets won't fit into any category and can just be called ``other``. 

---

# Several Projects

## Detecting human written text from text produced by the GPT-2 model
* Detect human written text (webtext) from GPT-2 generated text (xl-1542M model) 
* [Dataset](https://github.com/openai/gpt-2-output-dataset) (250K/250K train, 5K/5K valid, 5K/5K test)
* [Baseline classifier](https://github.com/openai/gpt-2-output-dataset/blob/master/baseline.py)
* [Analysis of baseline classifier](https://github.com/openai/gpt-2-output-dataset/blob/master/detection.md)
* Some ideas worth exploring:
  * Use advanced contextualized word representation model like [BERT](https://huggingface.co/transformers/)
  * Use simple bag of word embedding models like [fastText](https://fasttext.cc/)
  * Use other neural classification models from Supervised Learning II
* References
  * [GPT-2 original](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
  * [GPT-2 followup](https://arxiv.org/pdf/1908.09203.pdf)

## Machine translation for noisy Reddit text
* Build a neural machine translation model that translates noisy Reddit post (with typos, grammar errors, code switching and more) from French language to English language
* [Dataset](http://www.statmt.org/wmt19/robustness.html) (19161 train, 886 valid, 1022 test)
* Some ideas worth exploring:
  * Data augmentation using synthetic noise (take natural data and corrupt it); natural noise (Wikipedia errors?)
  * Backtranslation
  * Sub-word models like BPE, WordPiece
* References
  * [Dataset paper](https://www.aclweb.org/anthology/D18-1050.pdf)
  * [Related shared task](http://www.statmt.org/wmt19/robustness.html)
  * [Findings of the First Shared Task on Machine Translation Robustness](https://www.aclweb.org/anthology/W19-5303/)
  * [Improving Robustness of Machine Translation with Synthetic Noise](https://www.aclweb.org/anthology/N19-1190.pdf)

## Train a language model to generate social media data (e.g., tweets)
* Build a language model using a set of tweets (say) that can generate semantically sound tweets during test time
* Data can be diverse
* Model will most likely be better if it uses a lot of good quality data (e.g., 1M tweets)
* Might be computation intensive (so maybe Google Cloud TPUs, one month free)
* References
  * [Char-RNN blog](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

## Jigsaw Multilingual Toxic Comment Classification
* Identify toxic comments from benign or non-toxic comment
* [Data](https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification/data)
* Some ideas worth exploring:
  * Use advanced contextualized word representation model like [BERT](https://huggingface.co/transformers/)
  * Use simple bag of word embedding models like [fastText](https://fasttext.cc/)
  * Use other neural classification models from Supervised Learning II

## Inspect neurons of a machine translation model and write the analysis.
* Visualize important neurons in a machine translation model
* [Toolkit](https://github.com/fdalvi/NeuroX)
* Some ideas worth exploring
  * Identify linguistically interpretable neurons
  * Control translation to mitigate biases (e.g. gender bias)
* References
  * [Toolkit paper](https://arxiv.org/pdf/1812.09359.pdf)
  * [NMTViz](https://openreview.net/pdf?id=H1z-PsR5KX)
  * [ClassifierViz](http://www.aaai.org/Papers/AAAI/2019/AAAI-DalviF.5894.pdf)

## Compare and contrast several NLU/NLG architectures (e.g. BERT, GPT-2) via probing tasks and write the analysis
* Use existing or define new probing task to identify the linguistic features encoded by NLU/NLG models
* [Existing probing task](https://github.com/facebookresearch/SentEval/tree/master/data/probing)
* [NLU/NLG models](https://github.com/huggingface/transformers)
* Some ideas worth exploring
  * Analyzing state-of-the-art NLU model like BERT, XLNet and NLG model like GPT-2, CTRL
  * Contrast the performance with an untrained baseline model from the same family
  * Probe all the layers for each probing task and visualize using heatmap
* References
  * [What you can cram into a single $&!#* vector: Probing sentence embeddings for linguistic properties](https://www.aclweb.org/anthology/P18-1198.pdf)
  * [Linguistic Knowledge and Transferability of Contextual Representations](https://arxiv.org/abs/1903.08855)


