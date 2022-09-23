# links and snippets

## github badges

[Badge examples](https://github.com/Naereen/badges)

rst badge

```text
.. .. image:: https://pyup.io/repos/github/audreyfeldroy/cookiecutter-pypackage/shield.svg
..     :target: https://pyup.io/repos/github/audreyfeldroy/cookiecutter-pypackage/
..     :alt: Updates
```

## rst

- [rst Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

### Heading Levels

Normally, there are no heading levels assigned to certain characters as the structure is determined from the succession of headings. However, it is better to stick to the same convention throughout a project. For instance:

```text
# with overline, for parts
* with overline, for chapters
=, for sections
-, for subsections
^, for subsubsections
“, for paragraphs
```

### Napolean for google style doc strings

- [Napolean](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)

## Markdown

- [MyST](https://myst-parser.readthedocs.io/en/latest/index.html)
- [CommonMark](https://spec.commonmark.org/)

## Linting

### pylint

[Pylint disable messages](https://pylint.pycqa.org/en/latest/user_guide/messages/message_control.html#messages-control)

Disable checking for a file

```python
# pylint: disable-all
# OR
# pylint: skip-file
```

Block or line level

```python
# pylint: disable=no-member
# pylint: enable=no-member
```

## Testing

## Python

### Loading package resources

[importlib.resources – Resources](https://docs.python.org/3.11/library/importlib.resources.html#module-importlib.resources)
