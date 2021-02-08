# DSCI 572 Supervised Learning II

An introduction to deep learning, with a focus on NLP problems and applications. Covers a number of deep learning methods.

Upon completion of this course students will be able to:


* *identify* the core principles of training and designing artificial neural networks
* *identify* the inherent ambiguity in natural language, and appreciate challenges
associated with teaching machines to understand and generate it
* *become* aware of the major deep learning methods developed for solving
NLP problems 
* *apply* deep learning methods to NLP problems in critical, creative, and novel ways

---
# Class Meetings

This course occurs during Block 4 in the 2020/21 school year.

Lectures: Tuesdays and Thursdays, 10:30-12:00 PT, [@Zoom](https://ubc.zoom.us/j/62467194367?pwd=VEgveVZBNENncXo1R0lhUG03RHBUUT09) (pwd: 4242)

Labs: Thursdays, 2-4 PT, Zoom

---
# Assessments

This is an *assignment-based course*. You'll be evaluated as follows:

| Assesment | Weight   | Due Date |  Location          | 
|------   | ------- |--------------------------| ----- |
| Lab Assignment 1	| 15%	| Jan 16, 6pm PT	| Submit to Github |
| Lab Assignment 2	| 15%	| Jan 23, 6pm PT	| Submit to Github |
| Quiz 1	| 20%	| TBA |	TBA |
| Lab Assignment 3	| 15%	| Jan 30, 6pm PT	| Submit to Github |
| Lab Assignment 4	| 15%	| Feb 6, 6pm PT	| Submit to Github |
| Quiz 2	| 20%	| TBA	| TBA |

---
## Teaching Team

| Position           | Name    | Slack Handle | GHE Handle |
| :----------------: | :-----: | :----------: | :--------: |
| Main Instructor | Muhammad Abdul Mageed |    `@Muhammad Mageed`       | `@amuham01`        |
| Teaching Assistant | Peter Sullivan |    `@prsull`       | `@prsull`        |
| Lab Instructor | Ganesh Jawahar | `@ganeshjw` | `@ganeshjw` |
| Graduate Assistant | Chiyu Zhang | `@Chiyu Zhang` | `@chiyuzh` |

---
## Office Hours: 

| Name           | Time    | Location |
| :----------------: | :----------: | :--------: |
| Muhammad Abdul Mageed |    Wed. 12:00-14:00 PT       | [@Zoom](https://ubc.zoom.us/j/62467194367?pwd=VEgveVZBNENncXo1R0lhUG03RHBUUT09)        |
| Peter Sullivan |   Fri. 11:00-12:00 PT |  Slack        |
| Ganesh Jawahar | Thurs. 18:00-19:00 PT | [@Zoom](https://ubc.zoom.us/j/67010634869?pwd=RFVZVWxpU3lsZGtmMU9vWXUwWHBBdz09) |

---
# Weekly Content

| Lecture | Topic   | Readings                 | Lecture |  Tutorials |  Assignment |
|------   | ------- |--------------------------| -------- | -------- | -------- |
| 1   | PyTorch I | [PyTorch_Tutorials](https://pytorch.org/tutorials/) | [slides](lectures/Lecture-1-DSCI572-dl_intro.pdf) | ```PyTorch I``` [[Notebook](tutorials/week1/pytorch_tutorial.ipynb)]; [[video](https://youtu.be/X2ljS5aXnq0)] | ```HW01```  [[video](https://www.youtube.com/watch?v=Zuga-YxJJ2Y&feature=youtu.be)] |
| 2   | Feedforward Networks I |  [GBC-CH06](https://www.deeplearningbook.org/contents/mlp.html) (optional)|  [slides](lectures/Lecture-2-DSCI572-ffw.pdf) | ```TorchText``` [[Notebook](tutorials/week1/torchtext_tutorial.ipynb)]; [[video](https://youtu.be/umNsmMrm0bI)]  | NA |
| 3   |   Feedforward Networks II |  [GBC-CH06](http://www.deeplearningbook.org/contents/mlp.html) [GBC-CH10](http://www.deeplearningbook.org/contents/rnn.html)  |  [slides](lectures/Lecture-3_4-DSCI572-rnn.pdf);  | ```Feedforward neural networks``` [[Notebook](tutorials/week2/feedforward_neuralnets.ipynb)]; [[video](https://youtu.be/f7rXC23JWoM)] ```Word2vec``` [[Notebook](tutorials/week2/feedforward_neuralnets.ipynb)]; [[video](https://youtu.be/IZ6AcylOwpY)]  | ```HW02``` [[L2T2](https://youtu.be/l_UXDv341WY)]; [[L2Q1](https://youtu.be/aa8PUpHLWDg)];[[L2Q2](https://youtu.be/KHXCP3-o-Fc)];[[L2Q3](https://youtu.be/HqCUbKoZvH4)];[[L2Q4](https://youtu.be/Mlfr3yAfDro)] |
| 4   |  Recurrent Neural Networks  |  [GBC-CH10](http://www.deeplearningbook.org/contents/rnn.html)  |  [slides](lectures/Lecture-3_4-DSCI572-rnn.pdf)   | ```PyTorch debugging (optional)``` [[Notebook](tutorials/week1/pytorch_debugging.ipynb)] | [[L3T3](https://youtu.be/6OJVF_Li8qs)] [[L3Q1](https://youtu.be/qEipJfA73EQ)] [[L3Q2](https://youtu.be/lO-7QBecAxI)]|
| 5   |  Long-Short Term Memory Networks  |   [ChungEtAl_2014](https://arxiv.org/pdf/1412.3555.pdf) ```(optional)``` | [slides](lectures/Lecture-5-DSCI572-lstm.pdf)  | ```RNN GRU LSTM``` [[Notebook](tutorials/week3/rnn_tutorial.ipynb)]; [[video](https://youtu.be/ewxq2iCRCNE)] | -------- |
| 6   |  Regularization in Deep Learning  |  [GBC-CH07](http://www.deeplearningbook.org/contents/regularization.html)  |  [slides](lectures/Lecture-6-DSCI572-regularizarion.pdf)   | -------- | NA |
| 7   |  Gradient-Based Optimization   |  [GBC-CH08](http://www.deeplearningbook.org/contents/optimization.html)  |  [slides](lectures/Lecture-7-DSCI572-optimization.pdf) | ```Regularization and Optimization``` [[Notebook](tutorials/week4/Regularization_Optimization.ipynb)]; [[video](https://youtu.be/5JHSBjW5K5s)] | [[L4Q1](https://youtu.be/w5DiBhD2ll4)]; [[L4Q2](https://youtu.be/uYxhA5fQMJM)] |
| 8   | Backpropagation  | [GBC-CH08](http://www.deeplearningbook.org/contents/optimization.html)   |  [slides](lectures/Lecture-8-DSCI572-backpropagation.pdf)   | -------- | NA |

# Resources
1. [Goodfellow, Bengio and Courville. Deep learning Book](http://www.deeplearningbook.org) 

---
### Where to find good papers:
* [[ACL Anthology](https://www.aclweb.org/anthology/)]
* [[NeurIPS 2020](https://papers.nips.cc/paper/2020)]; [[NeurIPS 2019](https://nips.cc/Conferences/2019/AcceptedPapersInitial)]; [[NeurIPS 2018](http://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018)]
* [[ICLR 2020](https://iclr.cc/virtual_2020/papers.html?filter=keywords)]; [[ICLR 2019](https://iclr.cc/Conferences/2019/Schedule?type=Poster)]; [[ICLR 2018](https://dblp.org/db/conf/iclr/iclr2018)]
* [[AAAI Digital Library](https://www.aaai.org/Library/conferences-library.php)]

# Policies

Please see the general [MDS policies](https://ubc-mds.github.io/policies/).
