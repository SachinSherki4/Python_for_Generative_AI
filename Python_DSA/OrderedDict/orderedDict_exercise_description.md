
## OrderedDict in Python Collections

1. It is special dictionary subclass in collections 
2. It remember the order in which key inserted. It give exact control 
3. dict.move_to_end(key, last=True) : move key to end
4. dict.popitem(last=True) : remove last item, if(last=False) : it will remove first (FIFO)
5. dict.reversed() : support reverse

## In real-world AI/ML/GenAI systems, order often matters

(Situation)	               (Why Order Matters)	                           (How OrderedDict Helps)
1. Preprocessing steps	=> Certain cleaning must happen before others	=> Store ordered steps
2. Feature Engineering Pipelines  =>  Need to apply features in specific order	=>  Track transformations
3. Tokenization in NLP	=> Tokens must match original order	 => Build ordered vocab/token maps
4. Storing Model Evaluation Results	=> For plotting and comparing metrics in order	=> Maintain metric sequence
5. Handling Configurations	=> Settings may depend on earlier settings	=> Ordered configs


## Use Cases
1. AI/ML — Feature Transform Pipeline :Applying scaling, encoding, normalization in correct sequence.
2. GenAI — Vocabulary Building in Tokenizer : When assigning unique IDs to tokens, order matters.
3. Data Science — Metric Tracking for Models : Keep track of metric evaluation during experiments in order.

[Solutions](orderDict_exercise.py)


## Mini-Project : Preprocessing pipeline for ML Datasets
1. Problem Statement :
   1. You are working on ML project where you have raw tabular data(CSV like) with various issues :
      1. missing data
      2. Catagorical Columns
      3. Numerical scalling required
      4. New feature creation
   2. You required to clean and transformed data in a specific controlled sequence.
   3. You want to define transacformation steps clearlly, dynamically and ordered.
   4. Use OrderedDict to store processing steps in a right ordered and apply them one by one to dataset


[Mini-Project-Solution](mini_project_preprocessing_pipeline_for_ML_datasets.py)