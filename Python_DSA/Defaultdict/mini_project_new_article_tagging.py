
from collections import defaultdict
articles = [
    {'id': 1, 'title': 'New vaccine developed', 'tags': ['health', 'science']},
    {'id': 2, 'title': 'Elections coming soon', 'tags': ['politics']},
    {'id': 3, 'title': 'Tech giants release new AI', 'tags': ['technology', 'science']},
    {'id': 4, 'title': 'SpaceX launches rocket', 'tags': ['space', 'technology']},
    # Some articles are missing 'tags'
    {'id': 5, 'title': 'Climate change affects crops', 'tags': None},
]
tag_to_article=defaultdict(list)
article_count=defaultdict(int)
#iterate through each article
for article in articles:
    title=article['title'] # store each title
    tags=article['tags'] # store tags
    #count=article['count']

    if tags: # it tag present iterate
        for tag in tags: # iterate through each tags
            tag_to_article[tag].append(title) # assign title based on tag
            article_count[tag] += 1 # increase tag counter
#print(tag_to_article)
#print(article_count)

print("====each tag with assign articlies with it===")
for tag, article in tag_to_article.items():
    print(f"{tag} : {article}")
"""
====each tag with assign articlies with it===
health : ['New vaccine developed']
science : ['New vaccine developed', 'Tech giants release new AI']
politics : ['Elections coming soon']
technology : ['Tech giants release new AI', 'SpaceX launches rocket']
space : ['SpaceX launches rocket']
"""

