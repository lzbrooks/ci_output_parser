import pytest

from ci_output_parser import formatter


def test_format_lint_lines_with_valid_line(valid_lint_lines, valid_lint_format):
    lint_lines = formatter.format_lint_lines(valid_lint_format.get("parser_name"),
                                             [valid_lint_lines.get("doxygen_lint")],
                                             valid_lint_lines.get("cmake_lint"))
    assert len(lint_lines) == 9
    assert valid_lint_lines.get("cmake_lint")[0] == lint_lines[0]
    assert valid_lint_format.get("header_divider") == lint_lines[3]
    assert valid_lint_format.get("parser_name_formatted") == lint_lines[4]
    assert valid_lint_format.get("header_divider") == lint_lines[5]
    assert valid_lint_format.get("lint_comment_block") == lint_lines[6]
    assert valid_lint_lines.get("doxygen_lint") == lint_lines[7]
    assert valid_lint_format.get("lint_comment_block") == lint_lines[8]


def test_format_lint_lines_with_empty_lint_log_lines(valid_lint_lines, valid_lint_format):
    lint_lines = formatter.format_lint_lines(valid_lint_format.get("parser_name"),
                                             [valid_lint_lines.get("doxygen_lint")],
                                             [])
    assert len(lint_lines) == 6
    assert valid_lint_format.get("header_divider") == lint_lines[0]
    assert valid_lint_format.get("parser_name_formatted") == lint_lines[1]
    assert valid_lint_format.get("header_divider") == lint_lines[2]
    assert valid_lint_format.get("lint_comment_block") == lint_lines[3]
    assert valid_lint_lines.get("doxygen_lint") == lint_lines[4]
    assert valid_lint_format.get("lint_comment_block") == lint_lines[5]


def test_format_lint_lines_with_no_lint_log_lines(valid_lint_lines, valid_lint_format):
    lint_lines = formatter.format_lint_lines(valid_lint_format.get("parser_name"),
                                             [valid_lint_lines.get("doxygen_lint")])
    assert len(lint_lines) == 6
    assert valid_lint_format.get("header_divider") == lint_lines[0]
    assert valid_lint_format.get("parser_name_formatted") == lint_lines[1]
    assert valid_lint_format.get("header_divider") == lint_lines[2]
    assert valid_lint_format.get("lint_comment_block") == lint_lines[3]
    assert valid_lint_lines.get("doxygen_lint") == lint_lines[4]
    assert valid_lint_format.get("lint_comment_block") == lint_lines[5]


def test_format_lint_lines_with_no_parser_lint(valid_lint_lines, valid_lint_format):
    lint_lines = formatter.format_lint_lines(valid_lint_format.get("parser_name"),
                                             [],
                                             [])
    assert len(lint_lines) == 6
    assert valid_lint_format.get("header_divider") == lint_lines[0]
    assert valid_lint_format.get("parser_name_formatted") == lint_lines[1]
    assert valid_lint_format.get("header_divider") == lint_lines[2]
    assert valid_lint_format.get("lint_comment_block") == lint_lines[3]
    assert valid_lint_lines.get("no_errors_report") == lint_lines[4]
    assert valid_lint_format.get("lint_comment_block") == lint_lines[5]


def test_format_lint_lines_with_no_parser_name(valid_lint_lines, valid_lint_format):
    lint_lines = formatter.format_lint_lines("", [], [])
    assert len(lint_lines) == 6
    assert valid_lint_format.get("header_divider") == lint_lines[0]
    assert valid_lint_format.get("no_parser_name_formatted") == lint_lines[1]
    assert valid_lint_format.get("header_divider") == lint_lines[2]
    assert valid_lint_format.get("lint_comment_block") == lint_lines[3]
    assert valid_lint_lines.get("no_errors_report") == lint_lines[4]
    assert valid_lint_format.get("lint_comment_block") == lint_lines[5]


def test_format_lint_error_lines_with_valid_line(valid_lint_lines, valid_lint_format):
    lint_lines = formatter.format_lint_error_lines([valid_lint_lines.get("doxygen_lint")],
                                                   valid_lint_lines.get("cmake_lint"))
    assert len(lint_lines) == 6
    assert valid_lint_lines.get("cmake_lint")[0] == lint_lines[0]
    assert valid_lint_format.get("lint_comment_block") == lint_lines[3]
    assert valid_lint_lines.get("doxygen_lint") == lint_lines[4]
    assert valid_lint_format.get("lint_comment_block") == lint_lines[5]


def test_format_lint_error_lines_with_empty_lint_log_lines(valid_lint_lines, valid_lint_format):
    lint_lines = formatter.format_lint_error_lines([valid_lint_lines.get("doxygen_lint")], [])
    assert len(lint_lines) == 3
    assert valid_lint_format.get("lint_comment_block") == lint_lines[0]
    assert valid_lint_lines.get("doxygen_lint") == lint_lines[1]
    assert valid_lint_format.get("lint_comment_block") == lint_lines[2]


def test_format_lint_error_lines_with_no_lint_log_lines(valid_lint_lines, valid_lint_format):
    with pytest.raises(AttributeError):
        formatter.format_lint_error_lines([valid_lint_lines.get("doxygen_lint")], None)


def test_format_lint_error_lines_with_no_parser_lint(valid_lint_lines, valid_lint_format):
    lint_lines = formatter.format_lint_error_lines([], [])
    assert len(lint_lines) == 3
    assert valid_lint_format.get("lint_comment_block") == lint_lines[0]
    assert valid_lint_lines.get("no_errors_report") == lint_lines[1]
    assert valid_lint_format.get("lint_comment_block") == lint_lines[2]


def test_format_lint_title_with_valid_parser_name_and_log_lines(valid_lint_lines, valid_lint_format):
    lint_lines = formatter.format_lint_title(valid_lint_format.get("parser_name"),
                                             valid_lint_lines.get("cmake_lint"))
    assert len(lint_lines) == 6
    assert valid_lint_lines.get("cmake_lint")[0] == lint_lines[0]
    assert valid_lint_format.get("header_divider") == lint_lines[3]
    assert valid_lint_format.get("parser_name_formatted") == lint_lines[4]
    assert valid_lint_format.get("header_divider") == lint_lines[5]


def test_format_lint_title_with_empty_lint_log_lines(valid_lint_lines, valid_lint_format):
    lint_lines = formatter.format_lint_title(valid_lint_format.get("parser_name"), [])
    assert len(lint_lines) == 3
    assert valid_lint_format.get("header_divider") == lint_lines[0]
    assert valid_lint_format.get("parser_name_formatted") == lint_lines[1]
    assert valid_lint_format.get("header_divider") == lint_lines[2]


def test_format_lint_title_with_no_lint_log_lines(valid_lint_lines, valid_lint_format):
    with pytest.raises(AttributeError):
        formatter.format_lint_title(valid_lint_format.get("parser_name"), None)


def test_format_lint_title_with_no_parser_name(valid_lint_lines, valid_lint_format):
    lint_lines = formatter.format_lint_title("", [])
    assert len(lint_lines) == 3
    assert valid_lint_format.get("header_divider") == lint_lines[0]
    assert valid_lint_format.get("no_parser_name_formatted") == lint_lines[1]
    assert valid_lint_format.get("header_divider") == lint_lines[2]
