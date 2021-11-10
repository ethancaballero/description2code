# Description2Code dataset and (very messy) scrapers

Description2Code is dataset of ~7764 programming challenges scraped from CodeChef, Codeforces, & Hackerearth in 2016.

Link to download dataset:
https://www.dropbox.com/s/zwj6u4caehf54s0/description2code_current.zip

Story of dataset creation:
https://github.com/openai/requests-for-research/pull/5

Very messy code that was used for scraping Codechef, Codeforces, Hackerearth, & Topcoder in 2016 is located in `description2code/scrapers` folder. I don't remember why Topcoder isn't included in the dataset.

## License
I don't "own" the data scraped. CodeChef and CodeForces and HackerEarth or their users or something technically own it (or maybe they don't; idk). I don't know what the legal_rights/data_licenses of CodeChef and CodeForces and HackerEarth and their users are. I'm fine with you using this dataset and scraping code however you want.

## Citation
**⚠️ If you find this dataset (or scrapers) useful please cite us in your work ⚠️; BibTex to use:**
```
```

# Notes about dataset that download link contains

## CodeChef
* Contains curriculum of problems increasing as easy < medium < hard < harder < hardest
* External folder contains 2070 problems of varying difficulty
* does not contain samples and annotations for now
* 3201 total

## CodeForces
* Problem's difficulty relative to other problems in individual competition is indicated by suffix letter on end of folder ( A < B < C < D < E < F < G < I < J ); individual competition is signified by prefix number at start of folder
* '_tags.txt' contains list of which types of algorithmic techniques are needed to solve each problem; could be used to benchmark which types of problems your model is/isn't capable of solving or possibly as a supervision signal.
* 2128 total

## HackerEarth
* descriptions in 'problem_normal' are written slightly better than in 'problem_college'.
* '_tags.txt' contains list of the difficulty of and which types of algorithmic techniques are needed to solve each problem; could be used to benchmark which types of problems your model is/isn't capable of solving or possibly as a supervision signal.
* 2435 total

## General Usage
* description folder contains input for model; solutions_* (c++ or python depending on what you want to train on) contains target output for model.
* Use Example Input(s)/Output(s) near bottom of 'description.txt' to test whether generated code is correct.
* Train on multiple solutions provided for each problem to help your model generalize.
* 'Samples' folders contain several input/output samples that could be used to reward model when it generates code that correctly processes sample input into sample output. Several input/output examples are contained in each samples folder to prevent model from overfitting to generated code that could only correctly process a single sample input to sample output.  
* 'description_annotated.txt' is version of description that annotates tokens (with dagger (U+2020) and double_dagger (U+2021) at beginning and end of token(s) respectively) that are meant to be program variables.
* Use several sample input/output from samples folder to reward model for generating code that passes all possible test cases.
* versions of collected solution source codes are Python 2 and C++ 4.3.2
* 7764 total
