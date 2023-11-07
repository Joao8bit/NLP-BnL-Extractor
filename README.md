# NLP-BnL-Extractor

## What is this project about?
The following project was a bachelor semester project as a Computer Science student, with the main goal to study dated newspapers from the BnL (Bibliothéque Nationale du Luxembourg) using topic modelling.

The model being used for this project is Latent Dirichlet  Allocation (LDA). The objective will be to analyse how well can LDA identify key subjects in a sizable newspapers sample.

## How are the newspapers' data getting extracted?
The BnL provides a sample of newspapers in XML format, which allows for individual tag extraction. This is interesting because we will not need all tags' data for this study project.

The data is then extracted into CSV columns, where each row in a generated csv file represents a different newspaper article.

## Overall challenges
Some challenges faced during this project included some of the articles' provided data being of questionable quality, while others were of perfect quality. This could lead to misleading key subject information, non-relevant conclusions or even just pure chaos and confusion.
As an example, here is one of the least favourable article's description XML tag.
![Neg](https://github.com/Joao8bit/NLP-BnL-Extractor/blob/readmeUpdate/src/assets/NegativeLang.png)

Compared to a more accurate article, this one is more preferrable to be worked with.
![Pos](https://github.com/Joao8bit/NLP-BnL-Extractor/blob/readmeUpdate/src/assets/PositiveLang.png)
