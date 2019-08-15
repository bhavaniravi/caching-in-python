# Caching In Python

Caching is the method of storing the frequently used elements in a fast and easily accesible memory location. [This blog]() covers th basics of caching in detail.

Python supports caching with the help of various libraries

## Repo

This repo is split into packages with a `base` library commonly used by other packages. Each package is a flask application, which uses one of the caches.

## APIs

Each flask application delivers two sets of APIs

1. User
    - List User
    - Get User
    - List events attended by user

2. Events
    - List events
    - Get Events