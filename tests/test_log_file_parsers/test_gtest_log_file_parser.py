import pytest

from ci_output_parser.log_file_parsers.gtest_log_file_parser import GTestLogFileParser


def test_gtest_log_file_parser_init_with_default_values(default_gtest_log_file_parser,
                                                        gtest_log_file_parser_parameters):
    assert default_gtest_log_file_parser.parser_name == gtest_log_file_parser_parameters.get("parser_name")
    regex_parser = default_gtest_log_file_parser.log_file_parser
    file_parser_parameters = gtest_log_file_parser_parameters.get("file_parser")
    assert regex_parser.start_regex == file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == file_parser_parameters.get("parse_regex")
    regex_parser = default_gtest_log_file_parser.lint_error_parser
    lint_error_parser_parameters = gtest_log_file_parser_parameters.get("lint_error_parser")
    assert regex_parser.start_regex == lint_error_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == lint_error_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == lint_error_parser_parameters.get("parse_regex")


def test_gtest_log_file_parser_with_valid_file(gtest_valid_file_path, valid_lint_lines,
                                               mock_file_write_functions):
    log_parser = GTestLogFileParser(gtest_valid_file_path.get("gtest_lint_valid_path"))
    log_parser.log_parser()
    assert len(log_parser.formatted_lines) == 39
    assert valid_lint_lines.get("gtest_lint")[1] in log_parser.formatted_lines
    assert valid_lint_lines.get("gtest_lint")[2] in log_parser.formatted_lines


def test_gtest_log_file_parser_with_clean_file(gtest_valid_file_path, valid_lint_lines,
                                               mock_file_write_functions):
    log_parser = GTestLogFileParser(gtest_valid_file_path.get("gtest_lint_clean_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_gtest_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = GTestLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_gtest_log_file_parser_with_empty_file(empty_file_path, valid_lint_lines,
                                               mock_file_write_functions):
    log_parser = GTestLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_clean_lint_error_lines_with_valid_lint_line(default_gtest_log_file_parser, valid_lint_lines):
    default_gtest_log_file_parser.lint_lines = [valid_lint_lines.get("gtest_lint")[0]]
    default_gtest_log_file_parser.lint_errors = [valid_lint_lines.get("gtest_lint")[1]]
    default_gtest_log_file_parser.clean_lint_error_lines()
    assert valid_lint_lines.get("gtest_lint")[0] in default_gtest_log_file_parser.lint_errors


def test_clean_lint_error_lines_with_invalid_line(default_gtest_log_file_parser, invalid_lint_lines):
    default_gtest_log_file_parser.lint_lines = [invalid_lint_lines.get("gtest_lint")]
    default_gtest_log_file_parser.clean_lint_error_lines()
    assert not default_gtest_log_file_parser.lint_errors


def test_clean_lint_error_lines_with_empty_lines(default_gtest_log_file_parser):
    default_gtest_log_file_parser.clean_lint_error_lines()
    assert not default_gtest_log_file_parser.lint_errors
