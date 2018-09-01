# EU_Legislation_NLP
Natural language processing of EU legislation references using IBM's Watson Cloud platform  

The program accepts EU legislation as an URL (e.g. "<https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:31995L0046>")
and returns a list of all Regulations and Directives referenced in the legislation text, decomposed into relevant components:
Legislation Type, Number, Year, Article, Paragraph, Point.  


The project consists of three phases:
1. Accept URL input and extract legislation text using BeautifulSoup (in progress)
2. Identify and isolate whole references (e.g. "point 25 of Article 2 of Directive 2009/73/EC") from legislation by training
a custom Natural Language Understanding (NLU) model for Watson Cloud (completed)
3. Decompose references into components (e.g. "POINT": "point 25", "ARTICLE": "Article 2) by training
a second custom Natural Language Understanding (NLU) model for Watson Cloud (completed)
