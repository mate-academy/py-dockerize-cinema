# Сheck Your Code Against the Following Points

## Make sure you don't push the media directory and images

## Code Efficiency

Don't use `serializers.CharField` while adding an image.

Good example:

```python
movie_image = serializers.ImageField(...)
```

Bad example:

```python
movie_image = serializers.CharField(...)
```

## Code Style
1. Make sure you've added a blank line at the end to all your files.

2. Group imports using `()` if needed.

Good example:

```python
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin, 
    PermissionRequiredMixin,
)
```

Bad example:

```python
from django.contrib.auth.mixins import LoginRequiredMixin, \
    UserPassesTestMixin, PermissionRequiredMixin
```

Another bad example:

```python
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin, PermissionRequiredMixin,
)
```

## Clean Code
Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
