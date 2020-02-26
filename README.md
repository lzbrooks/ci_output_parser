# CIOutputParser

A python-based parser for collating and formatting log reports


## Installation

Download the latest release wheel and run:

```
pip install --user ci_output_parser-*-py3-none-any.whl
```

If this doesn't work, check that you have at least python 3.7, and that the `setuptools` and `wheel` python packages are up to date


## Usage

### Options

The options for the parser are:

```
ci_output_parser file_path [ android_lint [api_version] | junit_android_lint [api_version] | pre_commit_lint | vale_lint | gtest_lint firebase_lint | firebase_test_lint [device_name] ]

The default value of the first parser parameter is 'Target'
```

### Input

The parser takes in a single log file path

### Output

The base names of the output files (which are txt and json) are:

```
android_lint:       "android_api_<< api_version >>_app_lint"
                    "android_api_<< api_version >>_models_lint"
					"android_api_<< api_version >>_build_lint"
                    "android_api_<< api_version >>_kotlin_lint"
					"android_api_<< api_version >>_debug_javac_lint"
					"android_api_<< api_version >>_release_javac_lint"

junit_android_lint: "android_api_<< api_version >>_debug_unit_tests"
                    "android_api_<< api_version >>_release_unit_tests"

pre_commit_lint:    "pre_commit_lint"

vale_lint:          "vale_lint"

gtest_lint:         "gtest_tests"
firebase_lint:      "firebase_bucket_path"
                    "firebase_device_folders"
firebase_test_lint: "firebase_<< device_name >>_tests"
```

### Use Cases

In a CircleCI worflow these can be used in a few ways: []


## Log Parser Logic

### LogFileParser

LogFileParser is the base class of the parser project. Every other parser is built on this class

LogFileParser does these steps in order:
 - Get log lines from file
 - Get lint lines
 - Get lint error lines
 - Clean lint error lines
 - Format lint errors
 - Write lines to file

### RegexLogFileParser

All regex calls are confined to the RegexLogFileParser, which builds on LogFileParser

RegexLogFileParser takes regex parameters, which are converted to regex parsers, which then are used to parse the log file given

To get log lines from log file:
`file_parser_parameters -> log_file_parser`
`log_file_path -> log_file_parser -> log_lines`

To get lint lines from log lines:
`log_line_parser_parameters -> lint_parser`
`log_lines -> lint_parser -> lint_lines`

To get lint errors from lint lines:
`lint_error_parser_parameters -> lint_error_parser`
`lint_lines -> lint_error_parser -> lint_errors`

To get clean lint error lines from lint errors:
`clean_lint_error_parser_parameters -> clean_lint_error_parser`
`lint_errors -> clean_lint_error_parser -> lint_errors`


## Getting Started

Read the [contribution guide][contributing_guide] to get started developing this project


## Help

If you need help with the project see the authors or make an [issue][issue_template] if there's something that needs fixing or adding to the project


## Authors

* Lizann Brooks

For all contributors see the [contributors list][contributors_list].

[contributing_guide]: CONTRIBUTING.md
[issue_template]: https://github.com/lzbrooks/CIOutputParser/issues/new/choose
[contributors_list]: https://github.com/lzbrooks/CIOutputParser/graphs/contributors
