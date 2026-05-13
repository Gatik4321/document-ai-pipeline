## Research work (1).pdf - Page 1

Answers to the questions of Safire team
Q1 find the major Diff between the 2 OCR model compare them in their 
repose time how much resources they use which is a better choice for PROD.
Ans  Chandra (by Datalab):
Document intelligence model designed for basically high accuracy results.
Best for the production where layout matters.
Excellent in maintaining the relationship in complex tables
multilaguage support(over 90) also support handwritten text.
Speed 2 page/sec
         
       DeepSeek-OCR
it is a LLM centric model but this model trades off in accuracy
it is best for training the large scale ai.
Highly optimized with a speed of 2500 tokens/sec i.e 5 page/sec.
Used for feading the data to large language models.
Feature Chandra DeepSeek-OCR 
Best Use Case Forms, Tables, 
Handwriting Speed, Large Datasets, 
General Images 
Hindi Support Very Strong (90+ 
languages) Good (General 
Multilingual) 
Speed High (2 pages/sec on 
H100) Extremely High (2500 
tokens/sec) 
Chocie for production completely depends on your need if you want 
accuracy,g invoices, technical manuals, or textbooks  where losing a single 
table cell or formula would break your downstream AI logic then go with 
chandra but i u want speed and accuracy does not matters like user uploads a 
photo and u need response under a second user deepseek-OCR.
Chandra is more costly and has more memory requirements as compared to 
the deepseek OCR.

## Research work (1).pdf - Page 2

Q2 The test OpenDataLoader PDF is is worth our time with that check the 
PageIndex How to work with it if we want to do a system with document 
indexing?
Ans  opentdataloader, chandra and deepseek these all work together 
OpenDataLoader as the project Manager while Deepseek-OCR and Chandra 
as Specialist Workers.
What open dataloader does it took the pdf and handles the complex readings 
breaking the page into sections and then called the ocr model for futhur work.
Two stack designed for work:
1. Accuracy stack:
framwork : opendataloader
 Engine : Chandra 2
 result: You get the safety/citation features of the tool combined with the best-
in-class table and structure accuracy of Chandra. 
2. Velocity stack:
   Framework : OpenDataLoader
   Enginee: DeepSeek-OCR
   result : You process pages 2-3x faster. You might lose some table formatting,  
but you'll index millions of documents at a fraction of the cost. 
PageIndex is a repository for building Vectorless RAG
designed to solve major problem in traditional ai called chunking and then 
finding the similarity but fails for long and complex documents.
Page Index creates a semantic tree and convert a 100 page pdf into 
hierarchical table of contents where every node has a summnary used in RAG 
for higher accuracy (98.7%) Because it navigates a tree, it can tell you exactly 
why it chose a specific section, providing a clear "reasoning path" with page 
and section references. 
Inegrating the opendataloader and pageIndex is highly effective for the 
production grade especially if your goal is high-accuracy retrievl for complex 
technical or professional documents.

## Research work (1).pdf - Page 3

How the openDataLoader and PageIndex work together Work together?
Extraction OpenDataLoader Converts the raw PDF into clean, structured 
Markdown or JSON. It handles the "Garbage In" problem by preserving 
tables and reading order. 
Indexing PageIndex Takes that clean text and builds a Semantic Tree  (a 
"Smart Table of Contents"). It summarizes every section so the AI knows 
"what is where" without reading every word. 
Retrieval Reasoning LLM When a user asks a question, the AI "walks" the 
tree to find the exact section, then zooms in to extract the answer. 
Q3Link Portal is tool worth looking Check that is it actually help use to save 
money on tokens.
Ans Yes it can absolutely save you money on tokens
1. Eliminating “Context Bloat”:
The Open Session tools (like KARIMO and OpenClaw) use "smart routing" 
to only show the AI the specific tools it needs for the current task, which can 
save 10–15 KB of tokens per turn . 
2. Structured Plan Mode:
A cheap model handle routine formatting and planning expensive reasoning 
model is called for heavy lifting if there is not need it will be not called which 
autmatically saves tokens.