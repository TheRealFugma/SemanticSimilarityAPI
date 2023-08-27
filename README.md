# Semantic Similarity API
An API that measures the semantic similarity between two texts.

Submit an HTTP POST request in JSON format like so:

```
{
  "text1": "hello fugma",
  "text2": "hello figma"
}
```

The API returns a JSON like so:

```
{
  "similarity": 0.5
}
```

It's always a score between 0 and 1.
