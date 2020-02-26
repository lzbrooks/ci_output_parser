import pytest

from ci_output_parser import regex_ci_parser


def test_parser_init_with_valid_values(valued_parser, valid_regex):
    assert valued_parser.start_regex == valid_regex.get("start_regex")
    assert valued_parser.stop_regex == valid_regex.get("stop_regex")
    assert valued_parser.parse_regex == valid_regex.get("parse_regex")
    assert valued_parser.start_of_lines is False
    assert valued_parser.end_of_lines is False


def test_parser_init_with_invalid_start_value(valid_regex, invalid_regex):
    with pytest.raises(ValueError):
        regex_ci_parser.RegexCIParser(start_regex=invalid_regex, stop_regex=valid_regex.get(
            "stop_regex"), parse_regex=valid_regex.get("parse_regex"))


def test_parser_init_with_invalid_stop_value(valid_regex, invalid_regex):
    with pytest.raises(ValueError):
        regex_ci_parser.RegexCIParser(start_regex=valid_regex.get(
            "start_regex"), stop_regex=invalid_regex, parse_regex=valid_regex.get("parse_regex"))


def test_parser_init_with_invalid_parse_value(valid_regex, invalid_regex):
    with pytest.raises(ValueError):
        regex_ci_parser.RegexCIParser(start_regex=valid_regex.get(
            "start_regex"), stop_regex=valid_regex.get("stop_regex"), parse_regex=invalid_regex)


def test_parser_init_with_empty_values(valid_regex):
    default_parser = regex_ci_parser.RegexCIParser()
    assert default_parser.start_regex is None
    assert default_parser.stop_regex is None
    assert valid_regex.get("default_regex") == default_parser.parse_regex


def test_is_parser_start_with_valid_start_line(valued_parser, valid_log_lines):
    valued_parser.is_parser_start(valid_log_lines.get("start_line"))
    assert valued_parser.start_of_lines is True


def test_is_parser_start_with_invalid_start_line(valued_parser, invalid_log_lines):
    valued_parser.is_parser_start(invalid_log_lines.get("start_line"))
    assert valued_parser.start_of_lines is False


def test_is_parser_start_with_empty_start_line(valued_parser):
    valued_parser.is_parser_start("")
    assert valued_parser.start_of_lines is False


def test_is_parser_start_with_no_start_regex(valued_parser):
    valued_parser.start_regex = None
    valued_parser.is_parser_start("")
    assert valued_parser.start_of_lines is True


def test_is_parser_stop_with_valid_stop_line(valued_parser, valid_log_lines):
    valued_parser.start_of_lines = True
    valued_parser.end_of_lines = False
    valued_parser.is_parser_stop(valid_log_lines.get("stop_line"))
    assert valued_parser.end_of_lines is True


def test_is_parser_stop_with_valid_stop_line_and_start_of_lines_false(valued_parser, valid_log_lines):
    valued_parser.start_of_lines = False
    valued_parser.end_of_lines = False
    valued_parser.is_parser_stop(valid_log_lines.get("stop_line"))
    assert valued_parser.end_of_lines is False


def test_is_parser_stop_with_invalid_stop_line(valued_parser, invalid_log_lines):
    valued_parser.end_of_lines = False
    valued_parser.is_parser_stop(invalid_log_lines.get("stop_line"))
    assert valued_parser.end_of_lines is False


def test_is_parser_stop_with_empty_stop_line(valued_parser):
    valued_parser.end_of_lines = False
    valued_parser.is_parser_stop("")
    assert valued_parser.end_of_lines is False


def test_is_parser_stop_with_no_stop_parse(valid_regex, valid_log_lines):
    valued_parser = regex_ci_parser.RegexCIParser(
        start_regex=valid_regex.get("start_regex"), stop_regex=None)
    valued_parser.end_of_lines = False
    valued_parser.is_parser_stop(valid_log_lines.get("stop_line"))
    assert valued_parser.end_of_lines is False


def test_parse_line_regex_with_valid_line(valued_parser, valid_log_lines):
    valued_parser.start_of_lines = True
    match = valued_parser.parse_line_regex(
        valid_log_lines.get("parse_lines")[0])
    assert match.group(0) == "warning"


def test_parse_line_regex_with_invalid_line(valued_parser, valid_log_lines):
    valued_parser.start_of_lines = True
    match = valued_parser.parse_line_regex(valid_log_lines.get("stop_line"))
    assert match is None


def test_parse_line_regex_with_empty_line(valued_parser):
    valued_parser.start_of_lines = True
    match = valued_parser.parse_line_regex("")
    assert match is None


def test_parse_line_regex_with_start_of_lines_false(valued_parser, valid_log_lines):
    valued_parser.start_of_lines = False
    match = valued_parser.parse_line_regex(
        valid_log_lines.get("parse_lines")[0])
    assert match is None


def test_parse_line_with_valid_line(valued_parser, valid_log_lines):
    valued_parser.start_of_lines = True
    parsed_lines = valued_parser.parse_line(
        valid_log_lines.get("parse_lines")[0])
    assert parsed_lines[0] == valid_log_lines.get("parse_lines")[0]


def test_parse_line_with_invalid_line(valued_parser, invalid_log_lines):
    valued_parser.start_of_lines = True
    parsed_lines = valued_parser.parse_line(
        invalid_log_lines.get("parse_lines")[0])
    assert not parsed_lines


def test_parse_line_with_escaped_characters_first_group(valued_parser, valid_log_lines):
    valued_parser.start_of_lines = True
    parsed_lines = valued_parser.parse_line(
        valid_log_lines.get("parse_lines_with_escaped_characters")[1])
    assert parsed_lines[0] == valid_log_lines.get("parse_lines")[1]


def test_parse_line_with_escaped_characters_second_group(valued_parser, valid_log_lines):
    valued_parser.start_of_lines = True
    parsed_lines = valued_parser.parse_line(
        valid_log_lines.get("parse_lines_with_escaped_characters")[0])
    assert parsed_lines[0] == valid_log_lines.get("parse_lines")[0]


def test_parse_line_with_escaped_characters_both_groups(valued_parser, valid_log_lines):
    valued_parser.start_of_lines = True
    parsed_lines = valued_parser.parse_line(
        valid_log_lines.get("parse_lines_with_escaped_characters")[2])
    assert parsed_lines[0] == valid_log_lines.get("parse_lines")[1]


def test_parse_line_with_empty_line(valued_parser):
    valued_parser.start_of_lines = True
    parsed_lines = valued_parser.parse_line("")
    assert not parsed_lines


def test_parse_line_with_non_empty_parsed_lines(valued_parser, valid_log_lines):
    valued_parser.start_of_lines = True
    parsed_lines = valued_parser.parse_line(
        valid_log_lines.get("parse_lines")[0], ["warning"])
    assert parsed_lines[1] == valid_log_lines.get("parse_lines")[0]


def test_parse_line_list_with_valid_lines(valued_parser, valid_log_lines):
    valued_parser.start_of_lines = True
    parsed_lines = valued_parser.parse_line_list(
        valid_log_lines.get("parse_lines"))
    assert parsed_lines[0] == valid_log_lines.get("parse_lines")[0]
    assert parsed_lines[1] == valid_log_lines.get("parse_lines")[1]


def test_parse_line_list_with_invalid_lines(valued_parser, invalid_log_lines):
    valued_parser.start_of_lines = True
    parsed_lines = valued_parser.parse_line_list(
        invalid_log_lines.get("parse_lines"))
    assert not parsed_lines


def test_parse_line_list_with_empty_lines(valued_parser):
    line_list = ["", ""]
    valued_parser.start_of_lines = True
    parsed_lines = valued_parser.parse_line_list(line_list)
    assert not parsed_lines


def test_parse_line_list_with_valid_and_invalid_lines(valued_parser, valid_log_lines, invalid_log_lines):
    line_list = [invalid_log_lines.get("parse_lines")[1],
                 valid_log_lines.get("parse_lines")[1]]
    valued_parser.start_of_lines = True
    parsed_lines = valued_parser.parse_line_list(line_list)
    assert parsed_lines[0] == valid_log_lines.get("parse_lines")[1]


def test_parse_file_with_valid_file(valued_parser, docker_valid_file_path, valid_log_lines):
    parsed_lines = valued_parser.parse_file(
        docker_valid_file_path.get("docker_valid_path"))
    assert len(parsed_lines) == 22
    assert valid_log_lines.get("parse_lines")[0] in parsed_lines


def test_parse_file_with_invalid_file(valued_parser, invalid_file_path):
    with pytest.raises(FileNotFoundError):
        valued_parser.parse_file(invalid_file_path)


def test_parse_file_with_empty_file(valued_parser, empty_file_path):
    parsed_lines = valued_parser.parse_file(empty_file_path)
    assert not parsed_lines


def test_parse_file_with_empty_file_path(valued_parser):
    with pytest.raises(FileNotFoundError):
        valued_parser.parse_file("")
