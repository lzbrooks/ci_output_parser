from ci_output_parser.log_file_parsers.regex_log_file_parser import RegexLogFileParser


def test_regex_log_file_parser_init_with_default_values(default_regex_log_file_parser,
                                                        default_regex_log_file_parser_parameters,
                                                        valid_log_file_parser_fields):
    assert default_regex_log_file_parser.log_file_path == valid_log_file_parser_fields.get("log_file_path")
    assert default_regex_log_file_parser.parser_name == "Log File Lint"
    assert not default_regex_log_file_parser.formatted_lines
    assert default_regex_log_file_parser.text_output_file_name == "log_file_lint.txt"
    assert default_regex_log_file_parser.json_output_file_name == "log_file_lint.json"
    assert not default_regex_log_file_parser.log_lines
    assert not default_regex_log_file_parser.lint_lines
    assert not default_regex_log_file_parser.lint_errors
    regex_parser = default_regex_log_file_parser.log_file_parser
    assert regex_parser.start_regex == default_regex_log_file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == default_regex_log_file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == default_regex_log_file_parser_parameters.get("parse_regex")
    regex_parser = default_regex_log_file_parser.lint_parser
    assert regex_parser.start_regex == default_regex_log_file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == default_regex_log_file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == default_regex_log_file_parser_parameters.get("parse_regex")
    regex_parser = default_regex_log_file_parser.lint_error_parser
    assert regex_parser.start_regex == default_regex_log_file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == default_regex_log_file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == default_regex_log_file_parser_parameters.get("parse_regex")
    regex_parser = default_regex_log_file_parser.clean_lint_error_parser
    assert regex_parser.start_regex == default_regex_log_file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == default_regex_log_file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == default_regex_log_file_parser_parameters.get("parse_regex")


def test_regex_log_file_parser_init_with_no_file_parser_parameters(default_regex_log_file_parser,
                                                                   default_regex_log_file_parser_parameters):
    regex_parser = default_regex_log_file_parser.log_file_parser
    assert regex_parser.start_regex == default_regex_log_file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == default_regex_log_file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == default_regex_log_file_parser_parameters.get("parse_regex")


def test_regex_log_file_parser_init_with_file_parser_parameters(valid_log_file_parser_fields,
                                                                valid_regex_log_file_parser_parameters):
    regex_log_file_parser = RegexLogFileParser(
        log_file_path=valid_log_file_parser_fields.get("log_file_path"),
        file_parser_parameters=valid_regex_log_file_parser_parameters.get("file_parser_parameters"))
    regex_parser = regex_log_file_parser.log_file_parser
    file_parser_parameters = valid_regex_log_file_parser_parameters.get("file_parser_parameters")
    assert regex_parser.start_regex == file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_regex_log_file_parser_init_with_no_log_line_parser_parameters(default_regex_log_file_parser,
                                                                       default_regex_log_file_parser_parameters):
    regex_parser = default_regex_log_file_parser.log_file_parser
    assert regex_parser.start_regex == default_regex_log_file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == default_regex_log_file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == default_regex_log_file_parser_parameters.get("parse_regex")


def test_regex_log_file_parser_init_with_log_line_parser_parameters(valid_log_file_parser_fields,
                                                                    valid_regex_log_file_parser_parameters):
    regex_log_file_parser = RegexLogFileParser(
        log_file_path=valid_log_file_parser_fields.get("log_file_path"),
        log_line_parser_parameters=valid_regex_log_file_parser_parameters.get("log_line_parser_parameters"))
    regex_parser = regex_log_file_parser.lint_parser
    file_parser_parameters = valid_regex_log_file_parser_parameters.get("log_line_parser_parameters")
    assert regex_parser.start_regex == file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_regex_log_file_parser_init_with_no_lint_error_parser_parameters(default_regex_log_file_parser,
                                                                         default_regex_log_file_parser_parameters):
    regex_parser = default_regex_log_file_parser.lint_error_parser
    assert regex_parser.start_regex == default_regex_log_file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == default_regex_log_file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == default_regex_log_file_parser_parameters.get("parse_regex")


def test_regex_log_file_parser_init_with_lint_error_parser_parameters(valid_log_file_parser_fields,
                                                                      valid_regex_log_file_parser_parameters):
    regex_log_file_parser = RegexLogFileParser(
        log_file_path=valid_log_file_parser_fields.get("log_file_path"),
        lint_error_parser_parameters=valid_regex_log_file_parser_parameters.get("lint_error_parser_parameters"))
    regex_parser = regex_log_file_parser.lint_error_parser
    file_parser_parameters = valid_regex_log_file_parser_parameters.get("lint_error_parser_parameters")
    assert regex_parser.start_regex == file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_regex_log_file_parser_init_with_no_clean_lint_error_parser_parameters(
        default_regex_log_file_parser,
        default_regex_log_file_parser_parameters):
    regex_parser = default_regex_log_file_parser.clean_lint_error_parser
    assert regex_parser.start_regex == default_regex_log_file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == default_regex_log_file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == default_regex_log_file_parser_parameters.get("parse_regex")


def test_regex_log_file_parser_init_with_clean_lint_error_parser_parameters(valid_log_file_parser_fields,
                                                                            valid_regex_log_file_parser_parameters):
    regex_log_file_parser = RegexLogFileParser(
        log_file_path=valid_log_file_parser_fields.get("log_file_path"),
        clean_lint_error_parser_parameters=valid_regex_log_file_parser_parameters.get(
            "clean_lint_error_parser_parameters"))
    regex_parser = regex_log_file_parser.clean_lint_error_parser
    file_parser_parameters = valid_regex_log_file_parser_parameters.get("clean_lint_error_parser_parameters")
    assert regex_parser.start_regex == file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_regex_parser_set_up_with_valid_parser_parameters(default_regex_log_file_parser,
                                                          valid_regex_log_file_parser_parameters):
    regex_parser = default_regex_log_file_parser.regex_parser_set_up(
        valid_regex_log_file_parser_parameters.get("file_parser_parameters"))
    file_parser_parameters = valid_regex_log_file_parser_parameters.get("file_parser_parameters")
    assert regex_parser.start_regex == file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_regex_parser_set_up_with_no_parser_parameters(default_regex_log_file_parser,
                                                       default_regex_log_file_parser_parameters):
    regex_parser = default_regex_log_file_parser.regex_parser_set_up()
    assert regex_parser.start_regex == default_regex_log_file_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == default_regex_log_file_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == default_regex_log_file_parser_parameters.get("parse_regex")


def test_log_parser_with_valid_values(valid_regex_log_file_parser,
                                      valid_regex_log_file_parser_lines, mock_file_write_functions):
    valid_regex_log_file_parser.log_parser()
    assert len(valid_regex_log_file_parser.formatted_lines) == 6
    assert valid_regex_log_file_parser.formatted_lines == valid_regex_log_file_parser_lines.get("formatted_lines")


def test_get_log_lines_from_file_with_valid_log_file_parser(valid_regex_log_file_parser,
                                                            valid_lint_lines):
    valid_regex_log_file_parser.get_log_lines_from_file()
    assert len(valid_regex_log_file_parser.log_lines) == 71
    assert valid_lint_lines.get("pre_commit_lint") in valid_regex_log_file_parser.log_lines


def test_get_log_lines_from_file_with_default_log_file_parser(default_regex_log_file_parser,
                                                              valid_lint_lines):
    default_regex_log_file_parser.get_log_lines_from_file()
    assert len(default_regex_log_file_parser.log_lines) == 970
    assert valid_lint_lines.get("pre_commit_lint") in default_regex_log_file_parser.log_lines


def test_get_lint_lines_with_valid_lint_parser(valid_regex_log_file_parser,
                                               valid_regex_log_file_parser_lines):
    valid_regex_log_file_parser.log_lines = valid_regex_log_file_parser_lines.get("log_lines")
    valid_regex_log_file_parser.get_lint_lines()
    assert len(valid_regex_log_file_parser.lint_lines) == 4
    assert valid_regex_log_file_parser.lint_lines == valid_regex_log_file_parser_lines.get("lint_lines")


def test_get_lint_lines_with_default_lint_parser(default_regex_log_file_parser,
                                                 valid_regex_log_file_parser_lines):
    default_regex_log_file_parser.log_lines = valid_regex_log_file_parser_lines.get("log_lines")
    default_regex_log_file_parser.get_lint_lines()
    assert len(default_regex_log_file_parser.lint_lines) == 6
    assert default_regex_log_file_parser.lint_lines == valid_regex_log_file_parser_lines.get("log_lines")


def test_get_lint_error_lines_with_valid_lint_error_parser(valid_regex_log_file_parser,
                                                           valid_regex_log_file_parser_lines):
    valid_regex_log_file_parser.lint_lines = valid_regex_log_file_parser_lines.get("lint_lines")
    valid_regex_log_file_parser.get_lint_error_lines()
    assert len(valid_regex_log_file_parser.lint_lines) == 4
    assert valid_regex_log_file_parser.lint_errors == valid_regex_log_file_parser_lines.get("lint_errors")


def test_get_lint_error_lines_with_default_lint_error_parser(default_regex_log_file_parser,
                                                             valid_regex_log_file_parser_lines):
    default_regex_log_file_parser.lint_lines = valid_regex_log_file_parser_lines.get("lint_lines")
    default_regex_log_file_parser.get_lint_error_lines()
    assert len(default_regex_log_file_parser.lint_lines) == 4
    assert default_regex_log_file_parser.lint_errors == valid_regex_log_file_parser_lines.get("lint_lines")


def test_clean_lint_error_lines_with_valid_clean_lint_error_parser(valid_regex_log_file_parser,
                                                                   valid_regex_log_file_parser_lines):
    valid_regex_log_file_parser.lint_errors = valid_regex_log_file_parser_lines.get("lint_errors")
    valid_regex_log_file_parser.clean_lint_error_lines()
    assert len(valid_regex_log_file_parser.lint_errors) == 1
    assert valid_regex_log_file_parser.lint_errors == valid_regex_log_file_parser_lines.get("clean_lint_errors")


def test_clean_lint_error_lines_with_default_clean_lint_error_parser(default_regex_log_file_parser,
                                                                     valid_regex_log_file_parser_lines):
    default_regex_log_file_parser.lint_errors = valid_regex_log_file_parser_lines.get("lint_errors")
    default_regex_log_file_parser.clean_lint_error_lines()
    assert len(default_regex_log_file_parser.lint_errors) == 2
    assert default_regex_log_file_parser.lint_errors == valid_regex_log_file_parser_lines.get("lint_errors")
