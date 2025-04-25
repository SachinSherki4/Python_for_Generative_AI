## filter() in Tendorflow and Hugging Face
1. In real AI project: massive datasets(images, text, audio), 
2. Noisy/unwanted data, need to clean/ high--quality sample
3. Instead of looping manually through thousands of samples, filter() is a clean and memory-efficient 
4. way to apply conditions to include/exclude data

## Tools and libraries we need 
1. Tool/Library	  =>       Purpose
2. transformers	  =>   Hugging Face models (GPT, BERT, etc.) [ pip install transformers datasets ]
3. datasets	      =>   Load & filter large AI datasets  
4. tensorflow	   =>    Deep learning and model training [ pip install tensorflow ]
5. torch (PyTorch)	=>    Alternative to TensorFlow, very popular  [ pip install torch torchvision torchaudio ]
6. scikit-learn	    =>   Classical ML (for preprocessing, training, etc.)
7. pandas	       =>     Data analysis and processing [ pip install pandas numpy scikit-learn matplotlib ]
8. numpy	      =>     Math operations (used under the hood in ML)Tool/Library	Purpose

## Usa cases
1. Hugging Face datasets library
   => super popular to handle and deal with large-massive datasets like wikipedia, Common Crawl
2. 