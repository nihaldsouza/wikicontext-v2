## WikiContext [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/nihaldsouza/wikicontext-v2/main)

Wikipedia articles are hardly lucid. There is always some kind of jargon which floats around, which is difficult to understand in layman's term. This is an attempt to simplify the understanding of any Wikipedia article by providing a summary of some of the key concepts of the said article.
We provide the context, hence the name WikiContext.

![Streamlit UI Animation](https://raw.githubusercontent.com/nihaldsouza/wikicontext-v2/master/streamlit-ui.gif "Making-of Animation")

### Beneath the hood

WikiContext makes use of extractive text summarization, using [TextRank](https://www.aclweb.org/anthology/W04-3252). First step is to define a keyword list based on the hyperlinks present in the article. Once this is done, based on [keyword ranking](http://ceur-ws.org/Vol-706/poster13.pdf), we identify the most relevent keywords in the article. Then the data is fetched and the summarization is performed.

### What's next?

Add the [BERT extractive text summarizer](https://pypi.org/project/bert-extractive-summarizer/) as an additional algorithm.


### Contributing
We are doing some active development on this now, because there is a provision to host the app using streamlit! 

Link 1:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/nihaldsouza/wikicontext-v2/main)

Link 2:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/avinashbhat/wikicontext-v2/main)

