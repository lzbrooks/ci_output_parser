import pytest

from ci_output_parser import regex_ci_parser


@pytest.fixture
def valued_parser():
    valued_parser = regex_ci_parser.RegexCIParser(
        start_regex=r'doxygen Doxyfile',
        stop_regex=r'Removing intermediate container|non-zero code',
        parse_regex=r'warning')
    return valued_parser


@pytest.fixture
def valid_regex():
    valid_regex = {
        "start_regex": r'doxygen Doxyfile',
        "stop_regex": r'Removing intermediate container|non-zero code',
        "parse_regex": r'warning',
        "default_regex": r'.*'
    }
    return valid_regex


@pytest.fixture
def invalid_regex():
    return r'\u'


@pytest.fixture
def valid_log_lines():
    valid_log_lines = {
        "start_line": "Step 9/27 : RUN doxygen Doxyfile && doxybook -i temp/xml -o docs/api -t mkdocs &&     mkdocs "
                      "build\n",
        "stop_line": "Removing intermediate container 4c208e0c0ae7\n",
        "parse_lines": ["warning: ignoring unsupported tag `OUTPUT_TEXT_DIRECTION  =' at line 102, file Doxyfile\n",
                        "warning: ignoring unsupported tag `JAVADOC_BANNER         =' at line 208, file Doxyfile\n"],
        "parse_lines_with_escaped_characters": ["[91mwarning: ignoring unsupported tag `OUTPUT_TEXT_DIRECTION  =' at "
                                                "line 102, file Doxyfile\n",
                                                "[0mwarning: ignoring unsupported tag `JAVADOC_BANNER         =' at "
                                                "line 208, file Doxyfile\n",
                                                "[0m[91mwarning: ignoring unsupported tag `JAVADOC_BANNER         =' "
                                                "at line 208, file Doxyfile\n"]
    }
    return valid_log_lines


@pytest.fixture
def invalid_log_lines():
    invalid_log_lines = {"start_line": "Parsing: alpha_8cpp\n",
                         "stop_line": "Loading XML from: temp/xml/utils_8cpp.xml\n",
                         "parse_lines": [
                             "Searching for include files...\n",
                             "lookup cache used 132/65536 hits=599 misses=132\n"]}
    return invalid_log_lines


@pytest.fixture
def valid_lint_lines():
    valid_lint_lines = {
        "no_errors_report": "No errors to report\n",
        "pre_commit_lint": "Fix End of Files.........................................................Failed\n",
        "cmake_lint": ["make[1]: *** [CMakeFiles/blueberry_test.dir/all] Error 2\n",
                       "Scanning dependencies of target blueberry_cuda\n",
                       "CMake Generate step failed.  Build files cannot be regenerated correctly.\n"],
    }
    return valid_lint_lines


@pytest.fixture
def valid_lint_format():
    valid_lint_format = {
        "parser_name": "Doxygen Lint",
        "header_divider": "\n",
        "parser_name_formatted": "## Doxygen Lint\n",
        "no_parser_name_formatted": "## \n",
        "lint_comment_block": "```\n"
    }
    return valid_lint_format


@pytest.fixture
def parser_log_file_types():
    parser_log_file_types = {
        "android_lint": "android_lint",
        "junit_android_lint": "junit_android_lint",
        "pre_commit_lint": "pre_commit_lint",
        "vale_lint": "vale_lint",
        "gtest_lint": "gtest_lint",
        "firebase_lint": "firebase_lint",
        "firebase_test_lint": "firebase_test_lint",
        "api_version": "28",
        "device_name": "seoul-26-en-portrait",
        "no_parser_error": "ci_output_parser file_path [ docker_build | android_lint [api_version] | "
                           "junit_android_lint [api_version] | pre_commit_lint | vale_lint | gtest_lint | "
                           "firebase_lint | firebase_test_lint [device_name] ] \n The default value of the first "
                           "parser parameter is 'Target' "
    }
    return parser_log_file_types


@pytest.fixture
def parser_command_arguments(android_valid_file_path,
                             pre_commit_valid_file_path,
                             parser_log_file_types):
    program_name = "__main__.py"
    parser_command_arguments = {
        "program_name": [program_name],
        "android_lint_default": [program_name,
                                 android_valid_file_path.get("android_pass_lint_valid_path"),
                                 parser_log_file_types.get("android_lint")],
        "android_lint": [program_name,
                         android_valid_file_path.get("android_pass_lint_valid_path"),
                         parser_log_file_types.get("android_lint"),
                         parser_log_file_types.get("api_version")],
        "pre_commit_lint": [program_name,
                            pre_commit_valid_file_path.get("pre_commit_lint_valid_path"),
                            parser_log_file_types.get("pre_commit_lint")]
    }
    return parser_command_arguments
