## WikiContext [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/nihaldsouza/wikicontext-v2/main)

Wikipedia articles are hardly lucid. There is always some sort of jargon which floats around, that is difficult to understand in layman's term. This project is an attempt to simplify the understanding of any Wikipedia article by providing a summary of some of the key concepts.
We provide the context, hence the name WikiContext.

![Streamlit UI Animation](https://raw.githubusercontent.com/nihaldsouza/wikicontext-v2/master/streamlit-ui.gif "Making-of Animation")

### Beneath the hood

WikiContext makes use of extractive text summarization, using [TextRank](https://www.aclweb.org/anthology/W04-3252). First step is to define a keyword list based on the hyperlinks present in the article. Once this is done, based on [keyword ranking](http://ceur-ws.org/Vol-706/poster13.pdf), we identify the most relevent keywords in the article. Then the data is fetched and the summarization is performed.

### What's next?

1. [Wikipedia2Vec](https://wikipedia2vec.github.io/wikipedia2vec/) to obtain the embeddings of a wikipedia subject and use them as prerequisite sub-topics.

2. [BERT extractive text summarizer](https://pypi.org/project/bert-extractive-summarizer/) as an additional algorithm for summarization. We are exploring the option of using [Serverless Framework](https://www.serverless.com/) to deploy this service.


### Contributing
We are doing some active development on this now, so feel free to raise a PR! You can contact me directly on Twitter for any further enquires.

Link 1:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/nihaldsouza/wikicontext-v2/main)

Link 2:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/avinashbhat/wikicontext-v2/main)

