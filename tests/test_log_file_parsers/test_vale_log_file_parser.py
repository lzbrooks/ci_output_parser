import pytest

from ci_output_parser.log_file_parsers.vale_log_file_parser import ValeDockerLogFileParser, ValeLogFileParser


def test_vale_log_file_parser_init_with_default_values(default_vale_log_file_parser,
                                                       vale_log_file_parser_parameters):
    assert default_vale_log_file_parser.parser_name == vale_log_file_parser_parameters.get("parser_name")


def test_get_lint_lines_with_valid_line(default_vale_log_file_parser, valid_lint_lines):
    default_vale_log_file_parser.log_lines = [valid_lint_lines.get("vale_lint")[1]]
    default_vale_log_file_parser.get_lint_lines()
    assert valid_lint_lines.get("vale_lint")[1] in default_vale_log_file_parser.lint_lines


def test_get_lint_lines_invalid_line_first_group(default_vale_log_file_parser, invalid_lint_lines):
    default_vale_log_file_parser.log_lines = [invalid_lint_lines.get("vale_lint")[0]]
    default_vale_log_file_parser.get_lint_lines()
    assert not default_vale_log_file_parser.lint_lines


def test_get_lint_lines_with_invalid_line_second_group(default_vale_log_file_parser, invalid_lint_lines):
    default_vale_log_file_parser.log_lines = [invalid_lint_lines.get("vale_lint")[1]]
    default_vale_log_file_parser.get_lint_lines()
    assert not default_vale_log_file_parser.lint_lines


def test_get_lint_lines_with_invalid_line_third_group(default_vale_log_file_parser, invalid_lint_lines):
    default_vale_log_file_parser.log_lines = [invalid_lint_lines.get("vale_lint")[2]]
    default_vale_log_file_parser.get_lint_lines()
    assert not default_vale_log_file_parser.lint_lines


def test_get_lint_lines_with_empty_lines(default_vale_log_file_parser):
    default_vale_log_file_parser.get_lint_lines()
    assert not default_vale_log_file_parser.lint_lines


def test_vale_log_file_parser_with_valid_file(vale_valid_file_path, valid_lint_lines, mock_file_write_functions):
    log_parser = ValeLogFileParser(vale_valid_file_path.get("vale_lint_valid_path"))
    log_parser.log_parser()
    assert len(log_parser.formatted_lines) == 12
    assert valid_lint_lines.get("vale_lint")[0] in log_parser.formatted_lines


def test_vale_log_file_parser_with_clean_file(vale_valid_file_path, mock_file_write_functions):
    log_parser = ValeLogFileParser(vale_valid_file_path.get("vale_lint_clean_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_vale_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = ValeLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_vale_log_file_parser_with_empty_file(empty_file_path, mock_file_write_functions):
    log_parser = ValeLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_vale_docker_log_file_parser_init_with_valid_values(docker_valid_file_path,
                                                            vale_docker_log_file_parser_parameters):
    log_parser = ValeDockerLogFileParser(docker_valid_file_path.get("docker_valid_path"))
    file_parser_parameters = vale_docker_log_file_parser_parameters.get("file_parser")
    assert log_parser.log_file_parser.start_regex == file_parser_parameters.get("start_regex")
    assert log_parser.log_file_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert log_parser.log_file_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_vale_docker_log_file_parser_with_valid_file(docker_valid_file_path, valid_lint_lines,
                                                     mock_file_write_functions):
    log_parser = ValeDockerLogFileParser(docker_valid_file_path.get("docker_valid_path"))
    log_parser.log_parser()
    assert len(log_parser.formatted_lines) == 11
    assert valid_lint_lines.get("vale_lint")[0] in log_parser.formatted_lines


def test_vale_docker_log_file_parser_with_clean_file(docker_valid_file_path, valid_lint_lines,
                                                     mock_file_write_functions):
    log_parser = ValeDockerLogFileParser(docker_valid_file_path.get("docker_clean_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_vale_docker_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = ValeDockerLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_vale_docker_log_file_parser_with_empty_file(empty_file_path, mock_file_write_functions):
    log_parser = ValeDockerLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines
