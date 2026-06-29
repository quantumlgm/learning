"""
Lesson 05: Structural Typing and Variance

Short Description:
A media content module demonstrating structural typing via Protocols and
the practical behavior of covariance and invariance using Collections ABC.

Detailed Description:
This module explores advanced type system behaviors in Python 3.12+:
- 'Publication' acts as a structural Protocol, allowing independent classes
  like 'Article' and 'Video' to match the type implicitly without inheritance.
- 'analytics' leverages 'Iterable', an immutable type that is naturally covariant,
  safely accepting collections of subtypes for read-only operations.
- 'moderation' highlights invariance when shifted to mutable containers like 'list',
  preventing type contamination and enforcing strict type safety at the IDE level.
"""

from typing import Protocol, Iterable
from dataclasses import dataclass


class Publication(Protocol):
    views: int

    def play(self) -> None: ...


@dataclass
class Article:
    views: int

    def play(self) -> None:
        print("Read the article")


@dataclass
class Video:
    views: int

    def play(self) -> None:
        print("Watch the wideo")


def analytics(publications: Iterable[Publication]) -> int:
    return sum(p.views for p in publications)


def moderation(publications: Iterable[Publication]):
    collection: dict[str, list[Publication]] = {"Article": [], "Video": []}

    for p in publications:
        if isinstance(p, Article):
            collection["Article"].append(p)
        elif isinstance(p, Video):
            collection["Video"].append(p)

    return collection


if __name__ == "__main__":
    article = Article(100)
    article.play()  # Read the article

    video = Video(200)
    video.play()  # Wathc the wideo

    print(analytics([article, video]))  # 300

    zoo_video = Video(1000)
    sea_article = Article(300)
    print(moderation([article, sea_article, video, zoo_video]))
    # {'Article': [Article(views=100), Article(views=300)], 'Video': [Video(views=200), Video(views=1000)]}
