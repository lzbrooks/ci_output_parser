Contributing to CILogParser
======================

Contents:

 * [Getting Started](CONTRIBUTING.md#getting-started)
 * [Running Tests](CONTRIBUTING.md#running-tests)
 * [Running the Project](CONTRIBUTING.md#running-the-project)
 * [Style Guide](CONTRIBUTING.md#style-guide)
 * [Code of Conduct](CONTRIBUTING.md#code-of-conduct)
 * [Development Cycle](CONTRIBUTING.md#development-cycle)
 * [Github Checks](CONTRIBUTING.md#github-checks)
 * [Documentation](CONTRIBUTING.md#documentation)


Getting Started
---------------

Project development dependencies:

### Version Control

[Git][git_download]

### IDE

[PyCharm][pycharm]\
[Python 3][python]

### Codebase

Clone the [repository][repo]


Running Tests
-----------------

Tests are written with [pytest][pytest].

### Running tests locally in IDE

Start PyCharm

Select the `tests` folder and click `Run pytest in tests`

### Running tests locally through commandline

Open git bash or similar

Install dependencies

```
pip install --user -r requirements.txt
```

Run tests with coverage

```
coverage run --source ci_output_parser -m pytest
coverage report -m
```


Running the Project
-------------------

### From source for debug

```
python -m ci_output_parser <<your_log_file>>.txt [...]
```

### From local install

```
python setup.py install
ci_output_parser <<your_log_file>>.txt [...]
```

### From release for production

Download the wheel release asset from the [github release][github_release] you want

Open git bash or similar in the directory you downloaded the release

```
pip install CIOutputParser-<<your release tag>>.whl
```

Then run as usual:

```
ci_output_parser <<your_log_file>>.txt [...]
```


Style Guide
-----------

Use the [Google style guide][style].


Code of Conduct
---------------

Please read and follow our [Code of Conduct][conduct].


Development Cycle
-----------------

[Github flow][flow] model:

 * [Create an issue (feature or bug)](CONTRIBUTING.md#issues)
 * [Create a branch](CONTRIBUTING.md#branches)
 * [Open a pull request](CONTRIBUTING.md#pull-requests)
 * [Commit code](CONTRIBUTING.md#commit-messages)
 * [Test locally](CONTRIBUTING.md#running-tests)
 * [Document changes](CONTRIBUTING.md#documentation)
 * [Get a code review](CONTRIBUTING.md#code-review)
 * [Merge the branch](CONTRIBUTING.md#merges)

### Issues

[Create an issue][issue_creation] in the project indicating what you want to work on, if no issue exitsts for it already. [Assign it to yourself][issue_layout] and [add it to the Software Beamforming project][issue_to_project]. If addressing an existing milestone, [add that milestone][issue_layout].

Issues follow our [commit title](CONTRIBUTING.md#commit-messages) naming scheme.

### Branches

All additions to the master branch must be done through [feature branches][branch_flow]. These feature branches are named after the issue they are addressing.

For example, issue #162 named `Document CI pipeline changes` would have a branch named `document_ci_pipeline_changes_162`.

### Pull Requests

When beginning work on a branch make a [draft pull request][draft_pr] named after the issue the pull request fixes. [Add the pull request to the Software Beamforming project][issue_to_project] and [assign yourself][issue_layout] to the pull request.

The pull request body follows this pull request template:

```
<!--- Provide a general summary of your changes in the Title above -->

## Description
<!--- Describe your changes in detail -->

## Related Issue
<!--- This project only accepts pull requests related to open issues -->
<!--- If suggesting a new feature or change, please discuss it in an issue first -->
<!--- If fixing a bug, there should be an issue describing it with steps to reproduce -->
<!--- Please write the issue number here: -->
Close: #1
<!--- Please link to the issue here: -->
See: https://github.com/lzbrooks/CIOutputParser/issues/1

## Motivation and Context
<!--- Why is this change required? What problem does it solve? -->

## How Has This Been Tested?
<!--- Please describe in detail how you tested your changes. -->
<!--- Include details of your testing environment, and the tests you ran to -->
<!--- see how your change affects other areas of the code, etc. -->

## Screenshots (if appropriate):

## Types of changes
<!--- What types of changes does your code introduce? Put an `x` in all the boxes that apply: -->
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)

## Checklist:
<!--- Go over all the following points, and put an `x` in all the boxes that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're here to help! -->
- [ ] My code follows the code style of this project.
- [ ] My change requires a change to the documentation.
- [ ] I have updated the documentation accordingly.
- [ ] I have added tests to cover my changes.
- [ ] All new and existing tests passed.
```

### Commit Messages

[Commit your work][basic_git] to your feature branch and [push to Github][basic_git] often.

Follow [commit message hygiene][hygiene] to make reviews easier and to make
the VCS/git logs more valuable. [Add a commit message template][commit_templating] to your local repository for more consistent commit message formatting.

Commit messages follow this template:

```
Add your title here

# See links to relevant web pages, issue trackers, blog articles, etc.
See: https://example.com/
See: [Example Page](https://example.com/)

# List all co-authors, so version control systems can connect teams.
Co-authored-by: Name <name@example.com>
Co-authored-by: Name <name@example.com>

# Why is this change happening, e.g. goals, use cases, stories, etc.?
Why: 

# How is this change happening, e.g. implementations, algorithms, etc.?
How: 

# Tags suitable for searching, such as hashtags, keywords, etc.
Tags:
```

#### Commit title

Use 50 characters maximum\
Do not use a sentence-ending period\
Use the _imperative voice_: "Fix bug" rather than "Fixed bug" or "Fixes bug."

#### Commit body text

Use as many lines as you like\
Use 72 characters maximum per line for typical word wrap text

#### Allowed commit title starters

Add = Create a capability, for example: feature, test, dependency\
Drop = Delete a capability, for example: feature, test, dependency\
Fix = Fix an issue, for example: bug, typo, accident, misstatement\
Bump = Increase the version of something, for example: a dependency\
Make = Change the build process, or tools, or infrastructure\
Start = Begin doing something, for example: enable a toggle, feature flag, etc.\
Stop = End doing something, for example: disable a toggle, feature flag, etc.\
Optimize = A change that MUST be just about performance, for example: speed up code\
Document = A change that MUST be only in the documentation, for example: help files\
Refactor = A change that MUST be just refactoring\
Reformat = A change that MUST be just format, for example: indent line, trim space, etc.\
Rephrase = A change that MUST be just textual, for example: edit a comment, doc, etc.

### Code Review

Every pull request to master requires at least one code reviewer approval before merge.
Change your pull request from draft status and[request a reviewer][review_request]
when you are ready to merge the pull request.

When [reviewing a pull request][pr_review], keep these points in mind:

 * Is the code easy to _understand_?
 * Is the code written following the _coding standards/guidelines_?
 * Is the same code _duplicated_ more than twice?
 * Is the code easy to _unit test / debug_ to find the root cause?
 * Is this function or class _too big_? If yes, does the function or class have too many responsibilities?

For a more indepth guide, see this [code review checklist][review_checklist].

### Merges

Once all [checks](CONTRIBUTING.md#github-checks) and [code reviews](CONTRIBUTING.md#code-review) are resolved and pass, [merge your feature branch][git_merge] into the master branch. The branch will automatically be deleted and the addressed issue closed.

### Releases

Every pull request merge into master creates a [github release][github_release]. This release is made with [semantic-release][semantic_release].

Releases contain the current version of the docs as well as the tar and wheel of the project.


Github Checks
-------------

All required [Github checks][github_checks] must pass before you can merge a pull request.

Most build errors are reported as comments in the pull request after the checks run.

#### Pre-commit Lint

[cpplint][cpplint]: google c++ and CUDA style checker\
[cppcheck][cppcheck]: c++ and CUDA code linter\
[flake8][flake8]: python PEP8 style checker\
[check-json][pre_commit_hook_hooks]: json code linter\
[pretty-format-json][pre_commit_hook_hooks]: json style checker\
[check-merge-conflict][pre_commit_hook_hooks]: merge conflict string checker\
[check-symlinks][pre_commit_hook_hooks]: broken symlink checker\
[check-xml][pre_commit_hook_hooks]: xml style checker\
[check-yaml][pre_commit_hook_hooks]: yaml style checker\
[end-of-file-fixer][pre_commit_hook_hooks]: empty line at end of file checker\
[gitlint][gitlint]: git linter\
[yamllint][yamllint]: yaml code linter\
[cmake-format][cmake-format]: cmake list file code linter\
[dockerfilelint][dockerfilelint]: dockerfile code linter\
[bashate][bashate]: bash script style checker\
[shell-lint][shell_lint]: shell script code linter\
[circleci-config-validate][circleci_cofig_validate]: circleci config file code linter\
[detect-private-key][pre_commit_hook_hooks]: private key checker

#### Vale Lint

[vale][vale]: google prose style checker

#### Code Coverage

[CodeCov][codecov]: code coverage compiler

#### CircleCI

[CircleCI][circleci]: automatic build and test runner


Documentation
-------------

This project uses python [Google-style][google_style_docstring] [docstrings][python_docstring] code comments and [pdoc][pdoc] to generate and view the html documentation pages.

### View Documentation

#### To view the docs from source

```
pip install --user -r requirements.txt
pdoc --html ci_output_parser
```

In `html/ci_output_parser` open `index.html` with your preferred web browser

#### To view docs from release

Download Docs asset from the [github release][github_release] you want

Unzip docs folder

Open git bash or similar in the unzipped folder

In `ci_output_parser` open `index.html` with your preferred web browser

### Add Code Comments

Python Google-style docstrings are used for each function, class, and module:

#### Basic format

Brief description:

```
"""A brief description."""
```

Brief and more detailed description:

```
"""A brief description.

A longer and more detailed description
that may take more than one line.
"""
```

#### Functions

For smaller helper functions brief descriptions are fine.  For more important functions use a properly structured docstring:

```
def a_function(self, a_parameter):
	"""A brief description.

	A longer and more detailed description
	that may take more than one line.

	Args:
		a_parameter (string): Description of  the parameter.

	Returns:
		int: Description of return value.
	"""
```

#### Classes

Brief and more detailed descriptions for each class:

```
class AClass:
    """A brief description.
    
    A longer and more detailed description
	that may take more than one line.
	
	Attributes:
		a_class_attribute (int): Desciption of the class attribute.
	"""
	
	def __init__(self, a_class_attribute):
```

#### Modules

Brief and more detailed description at the top of each file:

```
"""A brief description.

A longer and more detailed description
that may take more than one line.
"""
```

#### Edit Documentation Pages

The handwritten docs pages are in `docs`. These follow [vale][vale] Google style enforcement. All documentation files are written in [Github compatible markdown][github_markdown].


[git_download]: http://git-scm.com/
[pycharm]: https://www.jetbrains.com/pycharm/
[python]: https://www.python.org/downloads/
[repo]: https://github.com/lzbrooks/CIOutputParser.git

[pytest]: https://docs.pytest.org/en/latest/

[conduct]: CODE_OF_CONDUCT.md

[style]: https://google.github.io/styleguide/cppguide.html

[flow]: https://guides.github.com/introduction/flow/

[issue_creation]: https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue
[issue_layout]: https://guides.github.com/features/issues/
[issue_to_project]: https://help.github.com/en/github/managing-your-work-on-github/adding-issues-and-pull-requests-to-a-project-board#adding-issues-and-pull-requests-to-a-project-board-from-the-sidebar

[branch_flow]: https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow

[draft_pr]: https://github.blog/2019-02-14-introducing-draft-pull-requests/

[github_checks]: https://help.github.com/en/github/administering-a-repository/about-required-status-checks
[cpplint]: https://github.com/cpplint/cpplint
[cppcheck]: http://cppcheck.sourceforge.net/
[flake8]: http://flake8.pycqa.org/en/latest/
[pre_commit_hook_hooks]: https://github.com/pre-commit/pre-commit-hooks
[gitlint]: https://github.com/jorisroovers/gitlint
[yamllint]: https://github.com/adrienverge/yamllint
[cmake-format]: https://pypi.org/project/cmake-format/
[dockerfilelint]: https://github.com/replicatedhq/dockerfilelint
[bashate]: https://github.com/openstack/bashate
[shell_lint]: https://github.com/koalaman/shellcheck
[circleci_cofig_validate]: https://github.com/syntaqx/git-hooks
[doxygen]: http://www.doxygen.nl/index.html
[doxybook]: https://github.com/matusnovak/doxybook
[mkdocs]: https://www.mkdocs.org
[vale]: https://github.com/errata-ai/vale
[cmake]: https://cmake.org/
[codecov]: https://codecov.io/
[circleci]: https://circleci.com/

[basic_git]: https://guides.github.com/introduction/git-handbook/#basic-git
[hygiene]: https://github.com/joelparkerhenderson/git_commit_message
[commit_templating]: Git_Commit_Templating.md

[review_request]: https://help.github.com/en/articles/requesting-a-pull-request-review
[pr_review]: https://help.github.com/en/articles/reviewing-proposed-changes-in-a-pull-request
[review_checklist]: https://www.evoketechnologies.com/blog/code-review-checklist-perform-effective-code-reviews/

[git_merge]: https://www.atlassian.com/git/tutorials/using-branches/git-merge

[github_release]: https://help.github.com/en/github/administering-a-repository/about-releases
[semantic_release]: https://semantic-release.gitbook.io/semantic-release/

[google_style_docstring]: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
[python_docstring]: https://www.python.org/dev/peps/pep-0257/
[pdoc]: https://pdoc3.github.io/pdoc/
[github_markdown]: https://guides.github.com/features/mastering-markdown/
