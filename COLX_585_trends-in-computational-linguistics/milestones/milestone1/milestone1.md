
# COLX 585 - Trends in CL | Milestone 1
---

## Overall Project Goals

* *Strengthen* student overall enginerring skills 
* *Extend and enhance* student experience working with the PyTorch framework
* *Apply* advanced deep learning of NLP methods and architectures 
* *Develop an ability to apply* existing methods on novel problems, or possibly develop new methods for solving existing problems (although the latter is not required) 
* *Improve* teamwork skills

---

## Group Project

During this course you will work collaboratively [in assigned groups](https://github.ubc.ca/MDS-CL-2019-20/COLX_585_trends_instructors/blob/master/milestones/milestone1/colx_585_groups.md) to apply deep learning and NLP methods on a problem (see below).

---

## Choosing Your Project

* You can either (1) choose a project from the pool of project ideas we are providing [here](https://github.ubc.ca/MDS-CL-2019-20/COLX_585_trends_instructors/blob/master/milestones/milestone1/projects.md) or (2) propose ypur own project. Each of the projects in category 1 [here](https://github.ubc.ca/MDS-CL-2019-20/COLX_585_trends_instructors/blob/master/milestones/milestone1/projects.md) is introduced as a simple idea, with a high-level context setting the stage for the problem to be solved. 
* It is the student responsibility to define the scope of the project, the approbriate methods (so long as these methods involve deep learning of NLP), how to articulate different aspects of the project, the related engineering, etc.

---

## Important Parameters Around Project Nature: 
* You should pick a method or a set of methods that you have at least some familiarity with. Especially for methods we have not covered, it is your responsibility to identify/develop methods and code and start working with these. This is a good context to practice self-learning which builds on and extends what you have been trained on thus far. 
*  As example methods, projects could involve applications of RNNs and variations (e.g., LSTMs, GRUs), CNNs and variations, Seq2Seq models, Transformers, BERT, etc.
* The instructor and the teaching support team will be able to provide pointers and guidance related to the methods. However, it is the student responsibility to carry out the engineering related to their project. Note that you can use and modify code you have been provided as part of the tutorials in any of the courses in the program thus far. There will also be additional tutorials with code that students will be provided during the current course. This code can also be used and modified by the students.
* Students can use code available online or in other sources. Importantly, the sources must be credited. *Failing to credit the sources from which ideas and/or code is derived will be treated as plagiarism.*
* The project cannot and must not be copied in whole or in part from another source such as an online post or a book. Students are expected to develop *their own* project. The project is expected to carry some level of *originality*. Originality can be in (1) applying existing methods to a *new problem*, (2) developing a new method for an existing problem, or (3) a mixture of the two.
* Students can use non-deep learning methods (e.g., use of LDA for topic modeling) as part of your project.
However, the *core/main methods used must be deep learning of NLP*.

---

## Repo setup
rubric={mechanics:2}

* Credit: Some of the details related to this and the next sections are inspired by (and in some parts borrowed from) Julian Brooks.

- You will be working in groups, and for each assignment (with the exception of the teamwork evaluation), you will do your work in the appropriate milestone directory in your group's github. For weekly submissions, please ensure that your individual repo has a link to the group repository's milestone folder, you have committed all changes to the master branch, and that the instructional team has read access.
 
- For the group repository, please create a group repo in the UBC github (it will be in one of your own repos, not MDS-CL). All the members of your team should have write access, and the instructor and all teaching support team (Peter, Chiyu, and Ganesh) should be given read access (check the syllabus for our github handles). Please message Peter on slack with the path to your repo by Sun. April 5 at 12:00/noon.

- Create a branch for each member of your team, where each of you will do your individual work. You should never push directly to the master branch during this project, instead when you are ready to share your work you should create a pull request to master which should be reviewed by one other member of the team.

- You may generally choose how to organize your repo, but for each milestone you should have one folder in the main repo directory where you will put milestone-specific written documents (such as the proposal), along with a readme with information about where to find any required code (which should NOT be put in the milestone folder). Make sure everything is in the master branch before the deadline, we won't go looking in your individual branches. You should not modify the documents in this folder after the deadline, or late penalties will be applied, see below. For the individual submission (on github LMS), again you will just post a link to the specific milestone folder in your groups repository.

---
## Teamwork contract
rubric={reasoning:2, writing:2}

Please create a teamwork contract. This document will govern your working relationship and you are encouraged to design it to manage and resolve any issues that arise in group work. 

A teamwork contract communicates specifically how the core group of people who are working together and gives more detail about the logisitics of working together and the expectations you have for each other. Some aspects of the team work contract could be:

- How will work be distributed in a fair and equitable way?
- What are the expected work hours for the project?
- How often will group meetings occur ([here is a nice article on meetings](http://third-bit.com/2018/05/11/meetings.html))?
- How will you manage online meetings? What technology will you use? Please provide a description of your *online collaboration* plan. (*See last paragraph in this section*).
- Will you have meeting agendas and minutes?
- What will be the style of working?
- Will you use daily "stand-ups", or submit a written summaries of your contributions, or something else?
- What is the quality of work each team member expects from themselves and each other?
- When are team members not available (e.g., evenings and Sundays because of family obligations).
- Will you have someone who acts as the project manager (i.e. keeps things on track) for the entire project, or each milestone, or be entirely democratic throughout the project?
- Is there any behaviour you wish to highlight as being expected or unacceptable (i.e., what is the code of conduct for the group?)
- And any other similar things that govern your working relationships.

Use this opportunity to apply your prior knowledge/experience to improve your teamwork, communication, leadership, and organizational skills. For this and all other written work in this course, do pay attention to the basic mechanics of writing, including spelling and grammar (everyone in the team should read over all the documents looking for such errors). You should submit this and other pieces of writing in .md (markdown) format, please take advantage of things like headers, bullet points, italics, etc to make things clearer.

---
### Online Collaboration
* You could use Blackboard Collab Ultra (GCU) on course Canvas.If you need your own group ``room`` on GCU, please let Peter know and he will set you up with it.
* Alternatively, you could use Zoom, Skype, or Google Hangouts. 
* It is *important* for you to identify and agree on the media you will employ for your meetings.

---

## Project proposal
rubric={reasoning:5,writing:2}

Describe your proposed project. Your should include the following information and anything else you deem relevant:

### *Introduction:* 
- Where you introduce the task/problem you will work on. This answers the question: ``What is the nature of the task?`` (e.g., sentiment analysis, machine translation, language generation, style transfer, etc.?). Please explain ``what the task entails`` (e.g., taking in as input a sequence of text from a source language and turning it into a sequence of sufficiently equivalent meaning in target language). 
### *Motivation and Contributions/Originality:*
- ``What is the motivation for pursuing this project?`` In other words, ``why is the project important``. This could be because this is a ``(relatively) new problem`` where you are using an existing method on (e.g., translating tweets where the language is noisy and doesn't usually obey `standard` rules). This could also be because the problem is ``timely`` (e.g., carrying out ``sentiment analysis on COVID-19`` data, given the negative impact of the pandemic). Further, this could be because the problem is ``socially motivated`` and/or ``remains unsolved`` (e.g., ``toxic`` and/or ``racist`` comments on social media, given their pervasively harmful impact).  
- What do you hope your ``contribution`` will be? Here, you could aim at providing a ``better system`` than what exists (e.g., more robust MT), an application on new data (possibly within a new domain) (e.g., ``tweet intent and topic detection on COVID-19 data``), a system that delivers insights on a new topic (e.g., ``scale and sentiment in tweets in different location as to COVID-19``), etc. 
### *Data:*
- What kind of ``data`` will you be using? ``Describe the corpus``: genre, size, language, style, etc. Do you have the data? Will you acquire the data? How? Where will you ``store`` your data? 
### *Engineering:*
- What ``computing infrastructure`` will you use? Personal computers? Google Colab? Google Cloud TPUs?
- What ``deep learning of NLP (DL-NLP)`` methods will you employ? For example, will you do ``text classification with BERT?``, ``MT with attention-based BiLSTMs``, ``language generation with transformers``, etc.? 
- ``Framework`` you will use. Note: You *must* use PyTorch. Identify any ``existing codebase`` you can start off with. Provide links.
### *Previous Works (minimal):*
- Refer to one or more projects that people have carried out that may be somewhat relevant to your project. This will later be expanded to some form of ``literature review``. For the sake of the proposal, this can be very brief. You are encouraged to refer to previous work here as a way to alert you to benefiting from existing projects. Provide links to any such projects.
### *Evaluation:*
- How will you ``evaluate`` your system? For example, if you are going to do MT, you could evaluate in ``BLEU``. For text classification, you can use ``accuracy`` and ``macro F1`` score. If your projects involves some interpretability, you could use ``visualization`` as a vehicle of deriving insights (and possibly some form of ``accuracy`` as approbriate).
### *Conclusion (optional):*
- You can have a very brief conclusion just summarizing the goal of the proposal. (2-3 sentences max).

### Writing:
* Again, pay attention to writing mechanics and use .md format.

---
# correct date for submission.

## Prompt completion
rubric={raw:4}

You should finish everything discussed above by 6pm Saturday, April 4. You will get an automatic extension until Sunday, April 5 at 12/noon. (You don't need to ask for that extension. Please go ahead and use it if you need it). Submissions after Sunday, April 5 12/noon, will be penalized by 5% if receieved after 12/noon. Another 5% applies for each additional day, up to total assignment weight. 
