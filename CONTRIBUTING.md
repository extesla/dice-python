# How to contribute

This document outlines how to contribute to the repository.

Contributing to the project should be as easy as possible for you, we don't
want to create unnecessary bureaucracy around the process of making changes.
However, there are a few ground rules and things to consider when
contributing. The following guidelines should be followed for developing and
submitting pull requests:

## Preparing for development

* You need a [GitHub account](https://github.com/signup/free) and you need to be
  included on one of the teams with access to this repository.
* Submit an [issue ticket](https://github.com/extesla/dice-python/issues) for your
  issue if there isn't one already created.
    * Describe the issue and include steps to reproduce when it's a bug.
    * Ensure to mention the earliest version that you know is affected.
    * If you plan on submitting a bug report, please submit detailed logs
      (preferably at DEBUG or lower).
* Fork the repository on GitHub (if you have not already done so previously)

## Making changes

* In your forked repository, create a topic branch for your upcoming patch.
  **NB:** Usually this is based on the `master` or `development` branches
  depending on what you are working on.
```
$ git checkout master
$ git checkout -b my-topic-branch
```
* Please avoid working directly on the `master` branch.
* Make commits of logical units and describe them properly. Avoid big,
  multi-purpose, commits.
* Check for unnecessary whitespace with `git diff --check` before committing.
* If possible, submit tests for your patch / new feature so it can be tested
  easily.
* Assure nothing is breaks by running all the tests.

## Submit Changes

* Push your changes to a topic branch in your fork of the repository.
* Open a pull request to the original repository and choose the right original
  branch you want to patch.
* If not done in commit messages (which you really should do) please reference
  and update your issue with the code changes.
* Even if you have write access to the repository, _do not_ directly push or
  merge pull-requests. Let another team member review your pull request and
  approve.

# Additional Resources

* [General GitHub documentation](http://help.github.com/)
* [GitHub pull request documentation](http://help.github.com/send-pull-requests/)
