import pytest

from ci_output_parser.log_file_parsers.log_file_parser import LogFileParser


def test_log_file_parser_init_with_default_values(default_log_file_parser,
                                                  default_log_file_parser_fields,
                                                  valid_log_file_parser_fields):
    assert default_log_file_parser.log_file_path == valid_log_file_parser_fields.get("log_file_path")
    assert default_log_file_parser.parser_name == default_log_file_parser_fields.get("parser_name")
    assert not default_log_file_parser.formatted_lines
    assert default_log_file_parser.text_output_file_name == default_log_file_parser_fields.get("text_output_file_name")
    assert default_log_file_parser.json_output_file_name == default_log_file_parser_fields.get("json_output_file_name")
    assert not default_log_file_parser.log_lines
    assert not default_log_file_parser.lint_lines
    assert not default_log_file_parser.lint_errors


def test_log_file_parser_init_with_no_log_file_path():
    with pytest.raises(ValueError):
        LogFileParser()


def test_log_file_parser_init_with_log_file_path(default_log_file_parser, valid_log_file_parser_fields):
    assert default_log_file_parser.log_file_path == valid_log_file_parser_fields.get("log_file_path")


def test_log_file_parser_init_with_no_parser_name(default_log_file_parser, default_log_file_parser_fields):
    assert default_log_file_parser.parser_name == default_log_file_parser_fields.get("parser_name")


def test_log_file_parser_init_with_parser_name(valid_log_file_parser_fields):
    log_file_parser = LogFileParser(log_file_path=valid_log_file_parser_fields.get("log_file_path"),
                                    parser_name=valid_log_file_parser_fields.get("parser_name"))
    assert log_file_parser.parser_name == valid_log_file_parser_fields.get("parser_name")


def test_log_file_parser_init_with_no_output_file_name_nor_parser_name(default_log_file_parser,
                                                                       default_log_file_parser_fields):
    assert default_log_file_parser.text_output_file_name == default_log_file_parser_fields.get("text_output_file_name")
    assert default_log_file_parser.json_output_file_name == default_log_file_parser_fields.get("json_output_file_name")


def test_log_file_parser_init_with_output_file_name(valid_log_file_parser_fields):
    log_file_parser = LogFileParser(log_file_path=valid_log_file_parser_fields.get("log_file_path"),
                                    output_file_name=valid_log_file_parser_fields.get("output_file_name"))
    assert log_file_parser.text_output_file_name == valid_log_file_parser_fields.get("text_output_file_name")
    assert log_file_parser.json_output_file_name == valid_log_file_parser_fields.get("json_output_file_name")


def test_log_file_parser_init_with_parser_name_and_no_output_file_name(valid_log_file_parser_fields):
    log_file_parser = LogFileParser(log_file_path=valid_log_file_parser_fields.get("log_file_path"),
                                    parser_name=valid_log_file_parser_fields.get("parser_name"))
    assert log_file_parser.text_output_file_name == valid_log_file_parser_fields.get("text_output_file_name")
    assert log_file_parser.json_output_file_name == valid_log_file_parser_fields.get("json_output_file_name")


def test_log_parser_with_default_values(mocker, default_log_file_parser):
    mocked_get_log_lines_from_file = mocker.patch.object(LogFileParser, 'get_log_lines_from_file')
    mocked_get_lint_lines = mocker.patch.object(LogFileParser, 'get_lint_lines')
    mocked_get_lint_errors = mocker.patch.object(LogFileParser, 'get_lint_error_lines')
    mocked_clean_lint_error_lines = mocker.patch.object(LogFileParser, 'clean_lint_error_lines')
    mocked_write_formatted_lines_to_file = mocker.patch.object(LogFileParser, 'write_formatted_lines_to_file')

    default_log_file_parser.log_parser()

    mocked_get_log_lines_from_file.assert_called()
    mocked_get_lint_lines.assert_called()
    mocked_get_lint_errors.assert_called()
    mocked_clean_lint_error_lines.assert_called()
    mocked_write_formatted_lines_to_file.assert_not_called()

    assert not default_log_file_parser.formatted_lines


def test_log_parser_with_lint_errors(mocker, default_log_file_parser, valid_log_file_parser_fields,
                                     mock_file_write_functions):
    mocked_get_log_lines_from_file = mocker.patch.object(LogFileParser, 'get_log_lines_from_file')
    mocked_get_lint_lines = mocker.patch.object(LogFileParser, 'get_lint_lines')
    mocked_get_lint_errors = mocker.patch.object(LogFileParser, 'get_lint_error_lines')
    mocked_clean_lint_error_lines = mocker.patch.object(LogFileParser, 'clean_lint_error_lines')
    mocked_write_formatted_lines_to_file = mocker.patch.object(LogFileParser, 'write_formatted_lines_to_file')
    default_log_file_parser.lint_errors = valid_log_file_parser_fields.get("lint_errors")

    default_log_file_parser.log_parser()

    mocked_get_log_lines_from_file.assert_called()
    mocked_get_lint_lines.assert_called()
    mocked_get_lint_errors.assert_called()
    mocked_clean_lint_error_lines.assert_called()
    mocked_write_formatted_lines_to_file.assert_called()
    assert default_log_file_parser.formatted_lines == valid_log_file_parser_fields.get("formatted_lines")


def test_get_log_lines_from_file_with_no_implementation(default_log_file_parser):
    with pytest.raises(NotImplementedError):
        default_log_file_parser.get_log_lines_from_file()


def test_get_lint_lines_with_no_implementation(default_log_file_parser):
    with pytest.raises(NotImplementedError):
        default_log_file_parser.get_lint_lines()


def test_get_lint_error_lines_with_no_implementation(default_log_file_parser):
    with pytest.raises(NotImplementedError):
        default_log_file_parser.get_lint_error_lines()


def test_clean_lint_error_lines_with_no_implementation(default_log_file_parser):
    with pytest.raises(NotImplementedError):
        default_log_file_parser.clean_lint_error_lines()


def test_format_lint_errors_with_no_lint_errors(default_log_file_parser):
    default_log_file_parser.format_lint_errors()
    assert not default_log_file_parser.formatted_lines


def test_format_lint_errors_with_lint_errors(default_log_file_parser, valid_log_file_parser_fields):
    default_log_file_parser.lint_errors = valid_log_file_parser_fields.get("lint_errors")
    default_log_file_parser.format_lint_errors()
    assert default_log_file_parser.formatted_lines == valid_log_file_parser_fields.get("formatted_lines")


def test_write_lines_to_file_with_no_formatted_lines_to_write(default_log_file_parser, mock_file_write_functions):
    write_file_success = default_log_file_parser.write_lines_to_file()
    assert not write_file_success


def test_write_lines_to_file_with_formatted_lines_to_write(default_log_file_parser, valid_log_file_parser_fields,
                                                           mock_file_write_functions):
    default_log_file_parser.formatted_lines = valid_log_file_parser_fields.get("formatted_lines")
    write_file_success = default_log_file_parser.write_lines_to_file()
    assert write_file_success


def test_write_formatted_lines_to_file_with_no_formatted_lines_to_write(default_log_file_parser,
                                                                        mock_file_write_functions):
    write_file_success = default_log_file_parser.write_formatted_lines_to_file()
    assert write_file_success


def test_write_formatted_lines_to_file_with_formatted_lines_to_write(default_log_file_parser,
                                                                     valid_log_file_parser_fields,
                                                                     mock_file_write_functions):
    default_log_file_parser.formatted_lines = valid_log_file_parser_fields.get("formatted_lines")
    write_file_success = default_log_file_parser.write_formatted_lines_to_file()
    assert write_file_success


def test_output_lint_lines_to_file_with_valid_lines(default_log_file_parser, valid_lint_lines, mock_output_files):
    default_log_file_parser.formatted_lines = [valid_lint_lines.get("pre_commit_lint")]
    default_log_file_parser.text_output_file_name = mock_output_files.get("mock_output_text_file")
    has_written_all_lines = default_log_file_parser.output_lint_lines_to_file()
    assert has_written_all_lines is True


def test_output_lint_lines_to_file_with_empty_lines(default_log_file_parser, mock_output_files):
    default_log_file_parser.text_output_file_name = mock_output_files.get("mock_output_text_file")
    has_written_all_lines = default_log_file_parser.output_lint_lines_to_file()
    assert has_written_all_lines is True


def test_output_lint_lines_to_json_file_with_valid_lines(default_log_file_parser, valid_lint_dictionary,
                                                         mock_output_files):
    default_log_file_parser.lint_dictionary = valid_lint_dictionary
    default_log_file_parser.json_output_file_name = mock_output_files.get("mock_output_json_file")
    has_written_all_lines = default_log_file_parser.output_lint_lines_to_json_file()
    assert has_written_all_lines is True


def test_output_lint_lines_to_json_file_with_empty_lines(default_log_file_parser, empty_lint_dictionary,
                                                         mock_output_files):
    default_log_file_parser.lint_dictionary = empty_lint_dictionary
    default_log_file_parser.json_output_file_name = mock_output_files.get("mock_output_json_file")
    has_written_all_lines = default_log_file_parser.output_lint_lines_to_json_file()
    assert has_written_all_lines is True


def test_make_json_dict_from_lint_lines_with_valid_line(default_log_file_parser, valid_lint_lines):
    default_log_file_parser.formatted_lines = valid_lint_lines.get("cmake_lint")
    default_log_file_parser.make_json_dict_from_lint_lines()
    assert valid_lint_lines.get("cmake_lint")[0] in default_log_file_parser.lint_dictionary.get("body")
    assert valid_lint_lines.get("cmake_lint")[1] in default_log_file_parser.lint_dictionary.get("body")


def test_make_json_dict_from_lint_lines_with_empty_lines(default_log_file_parser):
    default_log_file_parser.make_json_dict_from_lint_lines()
    assert not default_log_file_parser.lint_dictionary.get("body")
