import pytest

from ci_output_parser.log_file_parsers.junit_log_file_parser import JUnitAndroidDebugLogFileParser, \
    JUnitAndroidReleaseLogFileParser


def test_junit_android_log_file_parser_init_with_default_values(default_junit_android_log_file_parser,
                                                                junit_android_log_file_parser_parameters):
    assert default_junit_android_log_file_parser.parser_name == \
           junit_android_log_file_parser_parameters.get("parser_name")
    regex_parser = default_junit_android_log_file_parser.lint_parser
    log_line_parser_parameters = junit_android_log_file_parser_parameters.get("log_line_parser")
    assert regex_parser.start_regex == log_line_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == log_line_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == log_line_parser_parameters.get("parse_regex")
    regex_parser = default_junit_android_log_file_parser.lint_error_parser
    lint_error_parser_parameters = junit_android_log_file_parser_parameters.get("lint_error_parser")
    assert regex_parser.start_regex == lint_error_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == lint_error_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == lint_error_parser_parameters.get("parse_regex")


def test_junit_android_debug_log_file_parser_init_with_valid_values(junit_valid_file_path,
                                                                    junit_android_debug_log_file_parser_parameters):
    log_parser = JUnitAndroidDebugLogFileParser(junit_valid_file_path.get("junit_lint_valid_path"))
    file_parser_parameters = junit_android_debug_log_file_parser_parameters.get("file_parser")
    assert log_parser.log_file_parser.start_regex == file_parser_parameters.get("start_regex")
    assert log_parser.log_file_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert log_parser.log_file_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_junit_android_debug_log_file_parser_with_valid_file(junit_valid_file_path, valid_lint_lines,
                                                             mock_file_write_functions):
    log_parser = JUnitAndroidDebugLogFileParser(junit_valid_file_path.get("junit_lint_valid_path"))
    log_parser.log_parser()
    assert len(log_parser.formatted_lines) == 15
    assert valid_lint_lines.get("junit_android_lint")[1] in log_parser.formatted_lines


def test_junit_android_debug_log_file_parser_with_clean_file(junit_valid_file_path,
                                                             mock_file_write_functions):
    log_parser = JUnitAndroidDebugLogFileParser(junit_valid_file_path.get("junit_lint_clean_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_junit_android_debug_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = JUnitAndroidDebugLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_junit_android_debug_log_file_parser_with_empty_file(empty_file_path,
                                                             mock_file_write_functions):
    log_parser = JUnitAndroidDebugLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_junit_android_release_log_file_parser_init_with_valid_values(junit_valid_file_path,
                                                                      junit_android_release_log_file_parser_parameters):
    log_parser = JUnitAndroidReleaseLogFileParser(junit_valid_file_path.get("junit_lint_valid_path"))
    file_parser_parameters = junit_android_release_log_file_parser_parameters.get("file_parser")
    assert log_parser.log_file_parser.start_regex == file_parser_parameters.get("start_regex")
    assert log_parser.log_file_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert log_parser.log_file_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_junit_android_release_log_file_parser_with_clean_file(junit_valid_file_path,
                                                               mock_file_write_functions):
    log_parser = JUnitAndroidReleaseLogFileParser(junit_valid_file_path.get("junit_lint_clean_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_junit_android_release_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = JUnitAndroidReleaseLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_junit_android_release_log_file_parser_with_empty_file(empty_file_path,
                                                               mock_file_write_functions):
    log_parser = JUnitAndroidReleaseLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines
