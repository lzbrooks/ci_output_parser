import pytest

from ci_output_parser.log_file_parsers.android_log_file_parser import AndroidAppLogFileParser, \
    AndroidModelsLogFileParser, AndroidBuildLogFileParser, AndroidKotlinLogFileParser, AndroidJavacLogFileParser, \
    AndroidDebugJavacLogFileParser, AndroidReleaseJavacLogFileParser


def test_android_log_file_parser_init_with_default_values(default_android_log_file_parser,
                                                          android_log_file_parser_parameters):
    assert default_android_log_file_parser.parser_name == android_log_file_parser_parameters.get("parser_name")
    regex_parser = default_android_log_file_parser.lint_parser
    log_line_parser_parameters = android_log_file_parser_parameters.get("log_line_parser")
    assert regex_parser.start_regex == log_line_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == log_line_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == log_line_parser_parameters.get("parse_regex")
    regex_parser = default_android_log_file_parser.lint_error_parser
    lint_error_parser_parameters = android_log_file_parser_parameters.get("lint_error_parser")
    assert regex_parser.start_regex == lint_error_parser_parameters.get("start_regex")
    assert regex_parser.stop_regex == lint_error_parser_parameters.get("stop_regex")
    assert regex_parser.parse_regex == lint_error_parser_parameters.get("parse_regex")


def test_clean_lint_error_lines_with_valid_stop_line_first_group(default_android_log_file_parser, valid_stop_lines):
    default_android_log_file_parser.lint_errors = [valid_stop_lines.get("android_lint")[0]]
    default_android_log_file_parser.clean_lint_error_lines()
    assert not default_android_log_file_parser.lint_errors


def test_clean_lint_error_lines_with_valid_stop_line_second_group(default_android_log_file_parser, valid_stop_lines):
    default_android_log_file_parser.lint_errors = [valid_stop_lines.get("android_lint")[1]]
    default_android_log_file_parser.clean_lint_error_lines()
    assert not default_android_log_file_parser.lint_errors


def test_clean_lint_error_lines_with_valid_lint_line(default_android_log_file_parser, valid_lint_lines):
    default_android_log_file_parser.lint_lines = [valid_lint_lines.get("android_lint")[0]]
    default_android_log_file_parser.lint_errors = [valid_lint_lines.get("android_lint")[0]]
    default_android_log_file_parser.clean_lint_error_lines()
    assert valid_lint_lines.get("android_lint")[0] == default_android_log_file_parser.lint_errors[0]


def test_clean_lint_error_lines_with_empty_lines(default_android_log_file_parser):
    default_android_log_file_parser.clean_lint_error_lines()
    assert not default_android_log_file_parser.lint_errors


def test_android_app_log_file_parser_init_with_valid_values(android_valid_file_path,
                                                            android_app_log_file_parser_parameters):
    log_parser = AndroidAppLogFileParser(android_valid_file_path.get("android_fail_lint_valid_path"))
    file_parser_parameters = android_app_log_file_parser_parameters.get("file_parser")
    assert log_parser.log_file_parser.start_regex == file_parser_parameters.get("start_regex")
    assert log_parser.log_file_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert log_parser.log_file_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_android_app_log_file_parser_with_valid_file(android_valid_file_path, valid_lint_lines,
                                                     mock_file_write_functions):
    log_parser = AndroidAppLogFileParser(android_valid_file_path.get("android_fail_lint_valid_path"))
    log_parser.log_parser()
    assert len(log_parser.formatted_lines) == 52
    assert valid_lint_lines.get("android_lint")[1] in log_parser.formatted_lines


def test_android_app_log_file_parser_with_clean_file(android_valid_file_path,
                                                     mock_file_write_functions):
    log_parser = AndroidAppLogFileParser(android_valid_file_path.get("android_clean_lint_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_app_log_file_parser_with_checkstyle_log_file(android_valid_file_path, valid_lint_lines,
                                                              mock_file_write_functions):
    log_parser = AndroidAppLogFileParser(android_valid_file_path.get("android_checkstyle_lint_valid_path"))
    log_parser.log_parser()
    assert len(log_parser.formatted_lines) == 20
    assert valid_lint_lines.get("android_lint")[2] in log_parser.formatted_lines


def test_android_app_log_file_parser_with_checkstyle_clean_log_file(android_valid_file_path,
                                                                    mock_file_write_functions):
    log_parser = AndroidAppLogFileParser(android_valid_file_path.get("android_checkstyle_clean_lint_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_app_log_file_parser_with_app_fail_log_file(android_valid_file_path, valid_lint_lines,
                                                            mock_file_write_functions):
    log_parser = AndroidAppLogFileParser(android_valid_file_path.get("android_app_lint_fail_lint_valid_path"))
    log_parser.log_parser()
    assert len(log_parser.formatted_lines) == 17
    assert valid_lint_lines.get("android_lint")[3] in log_parser.formatted_lines


def test_android_app_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = AndroidAppLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_android_app_log_file_parser_with_empty_file(empty_file_path,
                                                     mock_file_write_functions):
    log_parser = AndroidAppLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_models_log_file_parser_init_with_valid_values(android_valid_file_path,
                                                               android_models_log_file_parser_parameters):
    log_parser = AndroidModelsLogFileParser(android_valid_file_path.get("android_fail_lint_valid_path"))
    file_parser_parameters = android_models_log_file_parser_parameters.get("file_parser")
    assert log_parser.log_file_parser.start_regex == file_parser_parameters.get("start_regex")
    assert log_parser.log_file_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert log_parser.log_file_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_android_models_log_file_parser_with_valid_file(android_valid_file_path, valid_lint_lines,
                                                        mock_file_write_functions):
    log_parser = AndroidModelsLogFileParser(android_valid_file_path.get("android_pass_lint_valid_path"))
    log_parser.log_parser()
    assert len(log_parser.formatted_lines) == 23
    assert valid_lint_lines.get("android_lint")[1] in log_parser.formatted_lines


def test_android_models_log_file_parser_with_clean_file(android_valid_file_path,
                                                        mock_file_write_functions):
    log_parser = AndroidModelsLogFileParser(android_valid_file_path.get("android_clean_lint_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_models_log_file_parser_with_checkstyle_log_file(android_valid_file_path,
                                                                 mock_file_write_functions):
    log_parser = AndroidModelsLogFileParser(android_valid_file_path.get("android_checkstyle_lint_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_models_log_file_parser_with_checkstyle_clean_file(android_valid_file_path,
                                                                   mock_file_write_functions):
    log_parser = AndroidModelsLogFileParser(android_valid_file_path.get("android_checkstyle_clean_lint_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_models_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = AndroidModelsLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_android_models_log_file_parser_with_empty_file(empty_file_path,
                                                        mock_file_write_functions):
    log_parser = AndroidModelsLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_build_log_file_parser_init_with_valid_values(android_valid_file_path,
                                                              android_build_log_file_parser_parameters):
    log_parser = AndroidBuildLogFileParser(android_valid_file_path.get("android_build_lint_valid_path"))
    file_parser_parameters = android_build_log_file_parser_parameters.get("file_parser")
    assert log_parser.log_file_parser.start_regex == file_parser_parameters.get("start_regex")
    assert log_parser.log_file_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert log_parser.log_file_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_android_build_log_file_parser_with_valid_file(android_valid_file_path, valid_lint_lines,
                                                       mock_file_write_functions):
    log_parser = AndroidBuildLogFileParser(android_valid_file_path.get("android_build_lint_valid_path"))
    log_parser.log_parser()
    print(''.join(log_parser.formatted_lines))
    assert len(log_parser.formatted_lines) == 44
    assert valid_lint_lines.get("android_build_lint")[0] in log_parser.formatted_lines
    assert valid_lint_lines.get("android_build_lint")[1] in log_parser.formatted_lines
    assert valid_lint_lines.get("android_build_lint")[2] in log_parser.formatted_lines


def test_android_build_log_file_parser_with_clean_file(android_valid_file_path,
                                                       mock_file_write_functions):
    log_parser = AndroidBuildLogFileParser(android_valid_file_path.get("android_clean_build_lint_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_build_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = AndroidBuildLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_android_build_log_file_parser_with_empty_file(empty_file_path,
                                                       mock_file_write_functions):
    log_parser = AndroidBuildLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_kotlin_log_file_parser_init_with_valid_values(android_valid_file_path,
                                                               android_kotlin_log_file_parser_parameters):
    log_parser = AndroidKotlinLogFileParser(android_valid_file_path.get("android_warning_build_lint_valid_path"))
    file_parser_parameters = android_kotlin_log_file_parser_parameters.get("file_parser")
    assert log_parser.log_file_parser.start_regex == file_parser_parameters.get("start_regex")
    assert log_parser.log_file_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert log_parser.log_file_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_android_kotlin_log_file_parser_with_valid_file(android_valid_file_path, valid_lint_lines,
                                                        mock_file_write_functions):
    log_parser = AndroidKotlinLogFileParser(android_valid_file_path.get("android_warning_build_lint_valid_path"))
    log_parser.log_parser()
    print(''.join(log_parser.formatted_lines))
    assert len(log_parser.formatted_lines) == 16
    assert valid_lint_lines.get("android_kotlin_lint")[0] in log_parser.formatted_lines


def test_android_kotlin_log_file_parser_with_clean_file(android_valid_file_path,
                                                        mock_file_write_functions):
    log_parser = AndroidKotlinLogFileParser(android_valid_file_path.get("android_clean_build_lint_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_kotlin_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = AndroidKotlinLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_android_kotlin_log_file_parser_with_empty_file(empty_file_path,
                                                        mock_file_write_functions):
    log_parser = AndroidKotlinLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_javac_log_file_parser_init_with_valid_values(android_valid_file_path,
                                                              android_javac_log_file_parser_parameters):
    log_parser = AndroidJavacLogFileParser(android_valid_file_path.get("android_javac_lint_valid_path"))
    assert log_parser.parser_name == android_javac_log_file_parser_parameters.get("parser_name")
    lint_parser_parameters = android_javac_log_file_parser_parameters.get("lint_parser")
    assert log_parser.lint_parser.start_regex == lint_parser_parameters.get("start_regex")
    assert log_parser.lint_parser.stop_regex == lint_parser_parameters.get("stop_regex")
    assert log_parser.lint_parser.parse_regex == lint_parser_parameters.get("parse_regex")


def test_android_javac_log_file_parser_with_valid_file(android_valid_file_path, valid_lint_lines,
                                                       mock_file_write_functions):
    log_parser = AndroidJavacLogFileParser(android_valid_file_path.get("android_javac_lint_valid_path"))
    log_parser.log_parser()
    print(''.join(log_parser.formatted_lines))
    assert len(log_parser.formatted_lines) == 274
    assert valid_lint_lines.get("android_javac_lint")[0] in log_parser.formatted_lines
    assert valid_lint_lines.get("android_javac_lint")[1] in log_parser.formatted_lines


def test_android_javac_log_file_parser_with_clean_file(android_valid_file_path,
                                                       mock_file_write_functions):
    log_parser = AndroidJavacLogFileParser(android_valid_file_path.get("android_clean_lint_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_javac_clean_lint_error_lines_with_no_lint_line(valid_lint_lines,
                                                                empty_file_path):
    log_parser = AndroidJavacLogFileParser(empty_file_path)
    log_parser.lint_lines = []
    log_parser.log_lines = valid_lint_lines.get("android_javac_lint")
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_android_javac_clean_lint_error_lines_with_lint_line(valid_lint_lines,
                                                             valid_stop_lines,
                                                             empty_file_path):
    log_parser = AndroidJavacLogFileParser(empty_file_path)
    log_parser.lint_lines = [valid_stop_lines.get("android_javac_lint")[0]]
    log_parser.log_lines = valid_lint_lines.get("android_javac_lint")
    log_parser.clean_lint_error_lines()
    assert valid_lint_lines.get("android_javac_lint") == log_parser.lint_errors


def test_android_javac_clean_lint_error_lines_with_empty_log_lines(empty_file_path):
    log_parser = AndroidJavacLogFileParser(empty_file_path)
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_android_debug_javac_log_file_parser_init_with_valid_values(android_valid_file_path,
                                                                    android_debug_javac_log_file_parser_parameters):
    log_parser = AndroidDebugJavacLogFileParser(android_valid_file_path.get("android_javac_lint_valid_path"))
    file_parser_parameters = android_debug_javac_log_file_parser_parameters.get("file_parser")
    assert log_parser.log_file_parser.start_regex == file_parser_parameters.get("start_regex")
    assert log_parser.log_file_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert log_parser.log_file_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_android_debug_javac_log_file_parser_with_valid_file(android_valid_file_path, valid_lint_lines,
                                                             mock_file_write_functions):
    log_parser = AndroidDebugJavacLogFileParser(android_valid_file_path.get("android_javac_lint_valid_path"))
    log_parser.log_parser()
    print(''.join(log_parser.formatted_lines))
    assert len(log_parser.formatted_lines) == 79
    assert valid_lint_lines.get("android_javac_lint")[2] in log_parser.formatted_lines


def test_android_debug_javac_log_file_parser_with_clean_file(android_valid_file_path,
                                                             mock_file_write_functions):
    log_parser = AndroidDebugJavacLogFileParser(android_valid_file_path.get("android_clean_lint_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_debug_javac_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = AndroidDebugJavacLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_android_debug_javac_log_file_parser_with_empty_file(empty_file_path,
                                                             mock_file_write_functions):
    log_parser = AndroidDebugJavacLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_release_javac_log_file_parser_init_with_valid_values(android_valid_file_path,
                                                                      android_release_javac_log_file_parser_parameters):
    log_parser = AndroidReleaseJavacLogFileParser(android_valid_file_path.get("android_javac_lint_valid_path"))
    file_parser_parameters = android_release_javac_log_file_parser_parameters.get("file_parser")
    assert log_parser.log_file_parser.start_regex == file_parser_parameters.get("start_regex")
    assert log_parser.log_file_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert log_parser.log_file_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_android_debug_release_log_file_parser_with_valid_file(android_valid_file_path, valid_lint_lines,
                                                               mock_file_write_functions):
    log_parser = AndroidReleaseJavacLogFileParser(android_valid_file_path.get("android_javac_lint_valid_path"))
    log_parser.log_parser()
    print(''.join(log_parser.formatted_lines))
    assert len(log_parser.formatted_lines) == 79
    assert valid_lint_lines.get("android_javac_lint")[0] in log_parser.formatted_lines


def test_android_release_javac_log_file_parser_with_clean_file(android_valid_file_path,
                                                               mock_file_write_functions):
    log_parser = AndroidReleaseJavacLogFileParser(android_valid_file_path.get("android_clean_lint_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_android_release_javac_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = AndroidReleaseJavacLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_android_release_javac_log_file_parser_with_empty_file(empty_file_path,
                                                               mock_file_write_functions):
    log_parser = AndroidReleaseJavacLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines
