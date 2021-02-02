# COLX 585 Trends in Computational Linguistics

## Introduction                        

This goal of this course is two-fold. First, the course aims at introducing ``recent deep learning of NLP methods``. Second, the course will function as a context for ``further enhancing student knowledge of deep learing software engineering`` in a project-based fashion where students work on a problem of their choice for the whole course. 

__Slack Channel__: cl-585_trends


## Learning Outcomes
Upon completion of this course students will be able to:

* *identify, motivate, and propose* a research plan for an important, meaningful, and possibly socially relevant problem
* *become* aware of the major engineering and research efforts related to the chosen project and major approaches to solve it
* *apply* deep learning of NLP methods to provide solutions on the problem of choice
* *present*, clearly, their proposed solution in the form of an oral presentation, a written report, and code
* *develop* effective strategies for teamwork

---
# Class Meetings

This course occurs during Block 6 in the 2019/20 school year.

### Lectures: 

* Some lectures will be recorded, with links to recordings provided in syllabus below before each lecture.
* Lectures will be delivered online real-time on Mondays and Tuesdays, 9:00 – 10:30 via Zoom.
* Zoom Link for real-time lectures: [here](https://ubc.zoom.us/j/806676863)
* Any exceptions as to how lecture is delivered will be announced beforehand.

### Labs: 
* Labs will be delivered online real-time on Tuesday, 2:00 – 4:00 pm via Zoom.
* Zoom Link for real-time lectures: [here](https://ubc.zoom.us/j/408820308).

---
## Project deadlines

This is an __project-based course__. You will work in assigned groups of three or four. You'll be evaluated as follows:

| Assessment       | Weight  | Deadline        | Location |
|------------------|---------|------------------|----------|
| Milestone 1: Project Proposal | 10%     | April 4, 6pm | On Github |
| Milestone 2: Progress Report 1 | 15%     |  April 11, 6pm | On Github |
| Milestone 3: Progress Report 2 | 15%     | April 18, 6pm | On Github |
| Milestone 4_a: Project Presentation | 5%   | April 22, 9:00am    | On [Zoom](https://ubc.zoom.us/j/806676863) |
| Milestone 4_b: Final Project | 25%   | April 26, 6pm    | On Github |
| Teamwork |  30% | April 28, 6pm  | On Github |

Note that for all but Teamwork, all students in the same group will receive the same grade. Students who get a failing grade on teamwork can get no better than a C in the course.

---
## Teaching Team

| Position           | Name    | Slack Handle | GHE Handle |
| :----------------: | :-----: | :----------: | :--------: |
| Main Instructor | Muhammad Abdul Mageed |    `@Muhammad Mageed`       | `@amuham01`        |
| Teaching Assistant | Peter Sullivan |    `@prsull`       | `@prsull`        |
| Lab Instructor | Chiyu Zhang | `@Chiyu Zhang` | `@chiyuzh` |
| Lab Instructor | Ganesh Jawahar | `@ganeshjw` | `@ganeshjw` |

---
## Office Hours: 
**Muhammad:** Mon. 12:00-14:00 via [Zoom](https://ubc.zoom.us/j/216120302) *(I can also handle inquiries via Zoom, by appointment.)*

**Peter:** Fri. 13:45-14:45 

**Chiyu:** Thurs. 14:00-15:00 on Slack

**Ganesh:**  Fri. 12:00-13:00

---
# Lecture Details (Tentative)

| Lecture       | Topic                 | Resources        | Zoom |
|---------------|-----------------------|------------------|------|
|1              |   Course Overview     |       Delivered Real-Time              | [Zoom](https://ubc.zoom.us/j/806676863) |
|2              |   ConvNets     |   [Video: CNN](https://www.youtube.com/watch?v=CwNIFfi67rE); [DLB-CH09](https://www.deeplearningbook.org/contents/convnets.html)   | [Zoom](https://ubc.zoom.us/j/806676863) |
|3              |   Self-Supervised Learning I   |     [Video: ELMo](https://www.youtube.com/watch?v=3qhriESuX9Y&t=2497s); [ELMo-slides](https://github.ubc.ca/MDS-CL-2019-20/COLX_585_trends_students/blob/master/Lectures/Lecture-3-COLX585_Trends-ELMo-2020.pdf); [ELMo-annot-slides](https://github.ubc.ca/MDS-CL-2019-20/COLX_585_trends_students/blob/master/Lectures/Lecture-3-COLX585_Trends-ELMo-annotated-2020.pdf); [ELMo](https://www.cs.ubc.ca/~amuham01/LING530/papers/petersELMo2018.pdf)|
|4              |   Self-Supervised Learning II    |  [Video: BERT](https://www.youtube.com/watch?v=4PAzTvFL4p4&t=1592s); [BERT](https://arxiv.org/pdf/1810.04805.pdf); [SentencePiece](https://arxiv.org/pdf/1808.06226.pdf)              | [Zoom](https://ubc.zoom.us/j/806676863)              |
|5              |    Holiday    |         No Class         | -- |
|6              |    Generative Deep Learning    |    [Video: GPT-2](xxx);    [GPT-2](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)          | [Zoom](https://ubc.zoom.us/j/806676863) |
|7              |    Multiple Methods  & Revision  |                  | [Zoom](https://ubc.zoom.us/j/806676863) |
|8              |     Project Presentations   |                  | [Zoom](https://ubc.zoom.us/j/806676863) |

---

# Papers & Resources

## Week 1
[DLB-CH09](https://www.deeplearningbook.org/contents/convnets.html)

## Week 2
#### Various Language Models
* [Semi-supervised sequence tagging with bidirectional language models](https://www.aclweb.org/anthology/P17-1161.pdf)
* [ELMo](https://www.cs.ubc.ca/~amuham01/LING530/papers/petersELMo2018.pdf)
* [BERT](https://arxiv.org/pdf/1810.04805.pdf)
* [Roberta](https://arxiv.org/pdf/1907.11692.pdf)
* [ALBERT](https://arxiv.org/pdf/1909.11942.pdf)
* [SpanBERT](https://www.mitpressjournals.org/doi/full/10.1162/tacl_a_00300)
* [MASS](https://arxiv.org/pdf/1905.02450.pdf)

#### Sub-Word Representations (Byte-pair Encoding)
* [Neural Machine Translation of Rare Words with Subword Units](https://www.aclweb.org/anthology/P16-1162.pdf)
* [Subword Regularization: Improving Neural Network Translation Models with Multiple Subword Candidates](https://arxiv.org/pdf/1804.10959.pdf)
* [SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing](https://arxiv.org/pdf/1808.06226.pdf)
* [A New Algorithm for Data Compression](https://www.derczynski.com/papers/archive/BPE_Gage.pdf)

#### Python Tools
* [Transformers](https://huggingface.co/transformers/)
* [Sentencepiece](https://github.com/google/sentencepiece)
* [BERT tokenizer](https://github.com/google-research/bert/blob/master/tokenization.py)


## Week 3
* [Improving Language Understanding by Generative Pre-Training(GPT-1)](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)
* [Language Models are Unsupervised Multitask Learners(GPT-2)](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
* [Neural Text Degeneration with Unlikelihood Training](https://arxiv.org/pdf/1908.04319.pdf)
* [Defending Against Neural Fake News(GROVER)](https://arxiv.org/pdf/1905.12616.pdf)
* [CTRL: A Conditional Transformer Language Model for Controllable Generation](https://arxiv.org/pdf/1909.05858.pdf)
* [Plug and Play Language Models: A Simple Approach to Controlled Text Generation(PPLM)](https://arxiv.org/pdf/1912.02164.pdf)
* [The Curious Case of Neural Text Degeneration(nucleus samples)](https://arxiv.org/pdf/1904.09751.pdf)

## Week 4


---
# Video Resources:
* [CNNs](https://www.youtube.com/watch?v=CwNIFfi67rE)
* [ELMo](https://www.youtube.com/watch?v=3qhriESuX9Y&t=2497s)
* [BERT](https://www.youtube.com/watch?v=4PAzTvFL4p4&t=1592s)
* [GPT-2](xxx)


## Previous Video Resources
* [Seq2seq Setup 1: Skeleton](https://www.youtube.com/watch?v=aial99njwdo)
* [Seq2seq Setup 2: Encoder Side](https://www.youtube.com/watch?v=k5NK2x5IUzY)
* [Seq2seq Setup 3: Encoder Side Code](https://www.youtube.com/watch?v=K7vj-eevn78)

* [Transformer 1](https://www.youtube.com/watch?v=IoXR8z-nfYI)
* [Transformer 2](https://www.youtube.com/watch?v=4Z5gkkCptHI)


# Further Resources

## Style Transfer: 
* [Multiple-Attribute Text Style Transfer](https://arxiv.org/pdf/1811.00552.pdf)
* [Dear sir or madam, may i introduce the gyafc dataset: Corpus, benchmarks and metrics for formality style transfer](https://arxiv.org/pdf/1803.06535.pdf)
* [Controllable Unsupervised Text Attribute Transfer via Editing Entangled Latent Representation Comprehension](https://papers.nips.cc/paper/9284-controllable-unsupervised-text-attribute-transfer-via-editing-entangled-latent-representation.pdf)

---
### Where to find good papers:
* [[ACL Anthology](https://www.aclweb.org/anthology/)]
* [[NeurIPS 2019 papers](https://nips.cc/Conferences/2019/AcceptedPapersInitial)]; [[NeurIPS 2018 proceedings](http://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018)]
* [[ICLR 2019](https://iclr.cc/Conferences/2019/Schedule?type=Poster)]; [[ICLR 2018](https://dblp.org/db/conf/iclr/iclr2018)]
* [[AAAI Digital Library](https://www.aaai.org/Library/conferences-library.php)]

# Policies

* Please see the general [MDS policies](https://ubc-mds.github.io/policies/).
* Note: 5% of an assignment will be lost for each 24 hour period up to the maximum of total assignment weight.
* Assignments submitted by 12/noon the next day of due date will not be penalized. Delay after 12/noon of the next day of due date will be penalized by 5% for that day. That is, automatic externsion does not apply after 12/noon of the next day of assignment due date.   
