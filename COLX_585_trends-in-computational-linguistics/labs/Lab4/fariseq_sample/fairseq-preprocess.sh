DATASET=en-fr 
fairseq-preprocess --source-lang fr --target-lang en \
	--tokenizer nltk \
    --trainpref $DATASET/train --validpref $DATASET/val --testpref $DATASET/test_2016_flickr \
    --destdir ./preproccessed 