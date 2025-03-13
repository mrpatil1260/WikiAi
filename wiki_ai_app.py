!pip install wikipedia
!pip install transformers

import wikipedia
from transformers import pipeline

def summarize_wikipedia(url):
  """
  Summarizes a Wikipedia page given its URL.

  Args:
    url: The URL of the Wikipedia page.

  Returns:
    A summary of the Wikipedia page, or an error message if the URL is invalid or the page cannot be found.
  """
  try:
    title = url.split('/')[-1]  # Extract the page title from the URL
    page = wikipedia.page(title)
    content = page.content

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn") # You can change the model here
    summary = summarizer(content, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

  except wikipedia.exceptions.PageError:
    return "Error: Wikipedia page not found."
  except wikipedia.exceptions.DisambiguationError as e:
      return f"Error: Disambiguation error. Possible pages: {', '.join(e.options)}"
  except Exception as e:
    return f"An error occurred: {e}"

#Example Usage
wikipedia_url = input("Enter a Wikipedia page URL: ")
summary = summarize_wikipedia(wikipedia_url)
summary
