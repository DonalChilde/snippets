# Project Dev Reference

## Sphinx

### intersphinx

[Code Refinery Sphinx lesson](https://coderefinery.github.io/sphinx-lesson/intersphinx/)
[Intersphinx with ReadTheDocs](https://docs.readthedocs.io/en/stable/guides/intersphinx.html)

#### RST

```rst
# Restructured Text
The :py:class:`list` class :py:meth:`sort <list.sort>` method.
```

#### Markdown

```markdown
# MyST markdown
The {py:class}`list` class {py:meth}`sort <list.sort>` method.
```

#### Python

- `:py:mod:`: modules, e.g. {py:mod}`multiprocessing`
- `:py:func:`: modules, e.g. {py:func}`itertools.combinations`
- `:py:class:`: modules, e.g. {py:class}`list`
- `:py:meth:`: modules, e.g. {py:meth}`list.sort`
- `:py:attr:`: modules, e.g. {py:attr}`re.Pattern.groups`
- `:py:data:`: modules, e.g. {py:data}`datetime.MINYEAR`
