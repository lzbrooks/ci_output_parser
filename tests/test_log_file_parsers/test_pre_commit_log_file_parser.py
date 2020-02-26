import pytest

from ci_output_parser.log_file_parsers.pre_commit_log_file_parser import PreCommitLogLogFileParser, \
    PreCommitDockerLogFileParser


def test_pre_commit_log_file_parser_init_with_default_values(default_pre_commit_log_file_parser,
                                                             valid_log_file_parser_fields,
                                                             default_regex_log_file_parser_parameters):
    assert default_pre_commit_log_file_parser.log_file_path == valid_log_file_parser_fields.get("log_file_path")
    assert default_pre_commit_log_file_parser.parser_name == valid_log_file_parser_fields.get("parser_name")
    assert not default_pre_commit_log_file_parser.formatted_lines
    assert default_pre_commit_log_file_parser.text_output_file_name == valid_log_file_parser_fields.get(
        "text_output_file_name")
    assert default_pre_commit_log_file_parser.json_output_file_name == valid_log_file_parser_fields.get(
        "json_output_file_name")
    assert not default_pre_commit_log_file_parser.log_lines
    assert not default_pre_commit_log_file_parser.lint_lines
    assert not default_pre_commit_log_file_parser.lint_errors
    regex_parser = default_pre_commit_log_file_parser.log_file_parser
    assert regex_parser.start_regex == default_regex_log_file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == default_regex_log_file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == default_regex_log_file_parser_parameters.get("parse_regex")
    regex_parser = default_pre_commit_log_file_parser.lint_parser
    assert regex_parser.start_regex == default_regex_log_file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == default_regex_log_file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == default_regex_log_file_parser_parameters.get("parse_regex")
    regex_parser = default_pre_commit_log_file_parser.lint_error_parser
    assert regex_parser.start_regex == default_regex_log_file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == default_regex_log_file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == default_regex_log_file_parser_parameters.get("parse_regex")
    regex_parser = default_pre_commit_log_file_parser.clean_lint_error_parser
    assert regex_parser.start_regex == default_regex_log_file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == default_regex_log_file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == default_regex_log_file_parser_parameters.get("parse_regex")


def test_get_lint_error_lines_with_valid_line(default_pre_commit_log_file_parser, valid_lint_lines):
    default_pre_commit_log_file_parser.lint_lines = [valid_lint_lines.get("pre_commit_lint")]
    default_pre_commit_log_file_parser.get_lint_error_lines()
    assert valid_lint_lines.get("pre_commit_lint") == default_pre_commit_log_file_parser.lint_errors[0]


def test_get_lint_error_lines_with_invalid_line_first_group(default_pre_commit_log_file_parser, invalid_lint_lines):
    default_pre_commit_log_file_parser.lint_lines = [invalid_lint_lines.get("pre_commit_lint")[0]]
    default_pre_commit_log_file_parser.get_lint_error_lines()
    assert not default_pre_commit_log_file_parser.lint_errors


def test_get_lint_error_lines_with_invalid_line_second_group(default_pre_commit_log_file_parser, invalid_lint_lines):
    default_pre_commit_log_file_parser.lint_lines = [invalid_lint_lines.get("pre_commit_lint")[1]]
    default_pre_commit_log_file_parser.get_lint_error_lines()
    assert not default_pre_commit_log_file_parser.lint_errors


def test_get_lint_error_lines_with_empty_lines(default_pre_commit_log_file_parser):
    default_pre_commit_log_file_parser.get_lint_error_lines()
    assert not default_pre_commit_log_file_parser.lint_errors


def test_clean_lint_error_lines_with_valid_line(default_pre_commit_log_file_parser, valid_lint_lines):
    default_pre_commit_log_file_parser.lint_errors = [valid_lint_lines.get("pre_commit_lint")]
    default_pre_commit_log_file_parser.clean_lint_error_lines()
    assert valid_lint_lines.get("pre_commit_lint") == default_pre_commit_log_file_parser.lint_errors[0]


def test_clean_lint_error_lines_with_invalid_line(default_pre_commit_log_file_parser, invalid_lint_lines):
    default_pre_commit_log_file_parser.lint_errors = [invalid_lint_lines.get("pre_commit_lint")[2]]
    default_pre_commit_log_file_parser.clean_lint_error_lines()
    assert not default_pre_commit_log_file_parser.lint_errors


def test_clean_lint_error_lines_with_empty_lines(default_pre_commit_log_file_parser):
    default_pre_commit_log_file_parser.clean_lint_error_lines()
    assert not default_pre_commit_log_file_parser.lint_errors


def test_pre_commit_log_log_file_parser_init_with_valid_values(pre_commit_valid_file_path,
                                                               pre_commit_log_log_file_parser_parameters):
    log_parser = PreCommitLogLogFileParser(pre_commit_valid_file_path.get("pre_commit_lint_valid_path"))
    log_parser_parameters = pre_commit_log_log_file_parser_parameters.get("log_line_parser")
    assert log_parser.lint_parser.start_regex == log_parser_parameters.get("start_regex")
    assert log_parser.lint_parser.stop_regex == log_parser_parameters.get("stop_regex")
    assert log_parser.lint_parser.parse_regex == log_parser_parameters.get("parse_regex")


def test_pre_commit_log_log_file_parser_with_valid_file(pre_commit_valid_file_path, valid_lint_lines,
                                                        mock_file_write_functions):
    log_parser = PreCommitLogLogFileParser(pre_commit_valid_file_path.get("pre_commit_lint_valid_path"))
    log_parser.log_parser()
    assert len(log_parser.formatted_lines) == 15
    assert valid_lint_lines.get("pre_commit_lint") in log_parser.formatted_lines


def test_pre_commit_log_log_file_parser_with_clean_file(pre_commit_valid_file_path, valid_lint_lines,
                                                        mock_file_write_functions):
    log_parser = PreCommitLogLogFileParser(pre_commit_valid_file_path.get("pre_commit_lint_clean_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_pre_commit_log_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = PreCommitLogLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_pre_commit_log_log_file_parser_with_empty_file(empty_file_path, valid_lint_lines,
                                                        mock_file_write_functions):
    log_parser = PreCommitLogLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_pre_commit_docker_log_file_parser_init_with_valid_values(pre_commit_valid_file_path,
                                                                  pre_commit_docker_log_file_parser_parameters):
    log_parser = PreCommitDockerLogFileParser(pre_commit_valid_file_path.get("pre_commit_lint_valid_path"))
    file_parser_parameters = pre_commit_docker_log_file_parser_parameters.get("file_parser")
    assert log_parser.log_file_parser.start_regex == file_parser_parameters.get("start_regex")
    assert log_parser.log_file_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert log_parser.log_file_parser.parse_regex == file_parser_parameters.get("parse_regex")
    log_parser_parameters = pre_commit_docker_log_file_parser_parameters.get("log_line_parser")
    assert log_parser.lint_parser.start_regex == log_parser_parameters.get("start_regex")
    assert log_parser.lint_parser.stop_regex == log_parser_parameters.get("stop_regex")
    assert log_parser.lint_parser.parse_regex == log_parser_parameters.get("parse_regex")


def test_pre_commit_docker_log_file_parser_with_valid_file(docker_valid_file_path, valid_lint_lines,
                                                           mock_file_write_functions):
    log_parser = PreCommitDockerLogFileParser(docker_valid_file_path.get("docker_valid_path"))
    log_parser.log_parser()
    assert len(log_parser.formatted_lines) == 26
    assert valid_lint_lines.get("pre_commit_lint") in log_parser.formatted_lines


def test_pre_commit_docker_log_file_parser_with_clean_log_file(pre_commit_valid_file_path, valid_lint_lines,
                                                               mock_file_write_functions):
    log_parser = PreCommitDockerLogFileParser(pre_commit_valid_file_path.get("pre_commit_lint_clean_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_pre_commit_docker_log_file_parser_with_invalid_file(invalid_file_path):
    with pytest.raises(FileNotFoundError):
        log_parser = PreCommitDockerLogFileParser(invalid_file_path)
        log_parser.log_parser()


def test_pre_commit_docker_log_file_parser_with_empty_file(empty_file_path, valid_lint_lines,
                                                           mock_file_write_functions):
    log_parser = PreCommitDockerLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines
