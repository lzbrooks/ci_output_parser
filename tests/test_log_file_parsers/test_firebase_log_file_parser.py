import pytest

from ci_output_parser.log_file_parsers.firebase_log_file_parser import FirebaseBucketLogFileParser, \
    FirebaseDeviceLogFileParser, FirebaseTestLogFileParser, FirebaseTestCrashLogFileParser, \
    FirebaseTestTimeoutLogFileParser


def test_firebase_log_file_parser_init_with_default_values(default_firebase_log_file_parser,
                                                           firebase_log_file_parser_parameters):
    assert default_firebase_log_file_parser.parser_name == firebase_log_file_parser_parameters.get("parser_name")


def test_format_lint_errors_with_valid_lint_line(default_firebase_log_file_parser, valid_lint_lines):
    default_firebase_log_file_parser.lint_errors = [valid_lint_lines.get("firebase_lint")[0]]
    default_firebase_log_file_parser.format_lint_errors()
    assert valid_lint_lines.get("firebase_lint")[7] == default_firebase_log_file_parser.formatted_lines[0]


def test_format_lint_errors_with_empty_lines(default_firebase_log_file_parser):
    default_firebase_log_file_parser.format_lint_errors()
    assert not default_firebase_log_file_parser.lint_errors


def test_firebase_bucket_log_file_parser_init_with_valid_values(firebase_valid_file_path,
                                                                firebase_bucket_log_file_parser_parameters):
    log_parser = FirebaseBucketLogFileParser(firebase_valid_file_path.get("firebase_lint_valid_path"))
    log_line_parser_parameters = firebase_bucket_log_file_parser_parameters.get("lint_parser")
    assert log_parser.lint_parser.start_regex == log_line_parser_parameters.get("start_regex")
    assert log_parser.lint_parser.stop_regex == log_line_parser_parameters.get("stop_regex")
    assert log_parser.lint_parser.parse_regex == log_line_parser_parameters.get("parse_regex")


def test_firebase_bucket_log_file_parser_with_valid_file(firebase_valid_file_path, valid_lint_lines,
                                                         mock_file_write_functions):
    log_parser = FirebaseBucketLogFileParser(firebase_valid_file_path.get("firebase_lint_valid_path"))
    log_parser.log_parser()
    assert len(log_parser.formatted_lines) == 1
    assert valid_lint_lines.get("firebase_lint")[7] in log_parser.formatted_lines


def test_firebase_bucket_log_file_parser_with_clean_file(firebase_valid_file_path, valid_lint_lines,
                                                         mock_file_write_functions):
    log_parser = FirebaseBucketLogFileParser(firebase_valid_file_path.get("firebase_lint_clean_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_firebase_bucket_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = FirebaseBucketLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_firebase_bucket_log_file_parser_with_empty_file(empty_file_path, valid_lint_lines,
                                                         mock_file_write_functions):
    log_parser = FirebaseBucketLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_firebase_bucket_clean_lint_error_lines_with_no_fail_line(valid_lint_lines,
                                                                  invalid_lint_lines,
                                                                  empty_file_path):
    log_parser = FirebaseBucketLogFileParser(empty_file_path)
    log_parser.log_lines = [invalid_lint_lines.get("firebase_lint")[0]]
    log_parser.lint_errors = [valid_lint_lines.get("firebase_lint")[0]]
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_firebase_bucket_clean_lint_error_lines_with_valid_fail_line(valid_lint_lines,
                                                                     empty_file_path):
    log_parser = FirebaseBucketLogFileParser(empty_file_path)
    log_parser.log_lines = [valid_lint_lines.get("firebase_lint")[3]]
    log_parser.lint_errors = [valid_lint_lines.get("firebase_lint")[4]]
    log_parser.clean_lint_error_lines()
    assert log_parser.lint_errors[0] == valid_lint_lines.get("firebase_lint")[0]


def test_firebase_bucket_clean_lint_error_lines_with_empty_lines(empty_file_path):
    log_parser = FirebaseBucketLogFileParser(empty_file_path)
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_firebase_device_log_file_parser_init_with_valid_values(firebase_valid_file_path,
                                                                firebase_device_log_file_parser_parameters):
    log_parser = FirebaseDeviceLogFileParser(firebase_valid_file_path.get("firebase_lint_valid_path"))
    file_parser_parameters = firebase_device_log_file_parser_parameters.get("file_parser")
    assert log_parser.log_file_parser.start_regex == file_parser_parameters.get("start_regex")
    assert log_parser.log_file_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert log_parser.log_file_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_firebase_device_log_file_parser_with_valid_file(firebase_valid_file_path, valid_lint_lines,
                                                         mock_file_write_functions):
    log_parser = FirebaseDeviceLogFileParser(firebase_valid_file_path.get("firebase_lint_valid_path"))
    log_parser.log_parser()
    assert len(log_parser.formatted_lines) == 2
    assert valid_lint_lines.get("firebase_lint")[8] in log_parser.formatted_lines
    assert valid_lint_lines.get("firebase_lint")[9] in log_parser.formatted_lines


def test_firebase_device_log_file_parser_with_clean_file(firebase_valid_file_path,
                                                         mock_file_write_functions):
    log_parser = FirebaseDeviceLogFileParser(firebase_valid_file_path.get("firebase_lint_clean_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_firebase_device_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = FirebaseDeviceLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_firebase_device_log_file_parser_with_empty_file(empty_file_path,
                                                         mock_file_write_functions):
    log_parser = FirebaseDeviceLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_firebase_device_clean_lint_error_lines_with_valid_lint_line(valid_lint_lines,
                                                                     empty_file_path):
    log_parser = FirebaseDeviceLogFileParser(empty_file_path)
    log_parser.lint_errors = [valid_lint_lines.get("firebase_lint")[3]]
    log_parser.clean_lint_error_lines()
    assert valid_lint_lines.get("firebase_lint")[1] == log_parser.lint_errors[0]


def test_firebase_device_clean_lint_error_lines_with_empty_lines(empty_file_path):
    log_parser = FirebaseDeviceLogFileParser(empty_file_path)
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_firebase_test_log_file_parser_init_with_valid_values(firebase_valid_file_path,
                                                              firebase_test_log_file_parser_parameters):
    log_parser = FirebaseTestLogFileParser(firebase_valid_file_path.get("firebase_test_lint_valid_path"))
    assert log_parser.parser_name == firebase_test_log_file_parser_parameters.get("parser_name")
    file_parser_parameters = firebase_test_log_file_parser_parameters.get("file_parser")
    assert log_parser.log_file_parser.start_regex == file_parser_parameters.get("start_regex")
    assert log_parser.log_file_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert log_parser.log_file_parser.parse_regex == file_parser_parameters.get("parse_regex")


def test_firebase_test_log_file_parser_with_valid_file(firebase_valid_file_path, valid_lint_lines,
                                                       mock_file_write_functions):
    log_parser = FirebaseTestLogFileParser(firebase_valid_file_path.get("firebase_test_lint_valid_path"))
    log_parser.log_parser()
    print(''.join(log_parser.formatted_lines))
    assert len(log_parser.formatted_lines) == 451
    assert valid_lint_lines.get("firebase_lint")[5] in log_parser.formatted_lines
    assert valid_lint_lines.get("firebase_lint")[6] in log_parser.formatted_lines


def test_firebase_test_log_file_parser_with_clean_file(firebase_valid_file_path,
                                                       mock_file_write_functions):
    log_parser = FirebaseTestLogFileParser(firebase_valid_file_path.get("firebase_lint_test_clean_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_firebase_test_log_file_parser_with_invalid_file(invalid_file_path):
    log_parser = FirebaseTestLogFileParser(invalid_file_path)
    with pytest.raises(FileNotFoundError):
        log_parser.log_parser()


def test_firebase_test_log_file_parser_with_empty_file(empty_file_path,
                                                       mock_file_write_functions):
    log_parser = FirebaseTestLogFileParser(empty_file_path)
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_firebase_test_log_file_parser_with_single_test_valid_file(firebase_valid_file_path, valid_lint_lines,
                                                                   mock_file_write_functions):
    log_parser = FirebaseTestLogFileParser(firebase_valid_file_path.get("firebase_single_test_lint_valid_path"))
    log_parser.log_parser()
    print(''.join(log_parser.formatted_lines))
    assert len(log_parser.formatted_lines) == 19
    assert valid_lint_lines.get("firebase_lint")[10] in log_parser.formatted_lines
    assert valid_lint_lines.get("firebase_lint")[11] in log_parser.formatted_lines


def test_firebase_test_clean_lint_error_lines_with_valid_lint_line(valid_lint_lines,
                                                                   empty_file_path):
    log_parser = FirebaseTestLogFileParser(empty_file_path)
    log_parser.lint_lines = [valid_lint_lines.get("firebase_lint")[5]]
    log_parser.log_lines = [valid_lint_lines.get("firebase_lint")[6]]
    log_parser.clean_lint_error_lines()
    assert valid_lint_lines.get("firebase_lint")[6] == log_parser.lint_errors[0]


def test_firebase_test_clean_lint_error_lines_with_invalid_line_first_group(valid_lint_lines,
                                                                            invalid_lint_lines,
                                                                            empty_file_path):
    log_parser = FirebaseTestLogFileParser(empty_file_path)
    log_parser.lint_lines = []
    log_parser.log_lines = [valid_lint_lines.get("firebase_lint")[5]]
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_firebase_test_clean_lint_error_lines_with_invalid_line_second_group(valid_lint_lines,
                                                                             invalid_lint_lines,
                                                                             empty_file_path):
    log_parser = FirebaseTestLogFileParser(empty_file_path)
    log_parser.lint_lines = [valid_lint_lines.get("firebase_lint")[5]]
    log_parser.log_lines = [invalid_lint_lines.get("firebase_lint")[1]]
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_firebase_test_clean_lint_error_lines_with_invalid_line_third_group(valid_lint_lines,
                                                                            invalid_lint_lines,
                                                                            empty_file_path):
    log_parser = FirebaseTestLogFileParser(empty_file_path)
    log_parser.lint_lines = [valid_lint_lines.get("firebase_lint")[5]]
    log_parser.log_lines = [invalid_lint_lines.get("firebase_lint")[2]]
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_firebase_test_clean_lint_error_lines_with_invalid_line_fourth_group(valid_lint_lines,
                                                                             invalid_lint_lines,
                                                                             empty_file_path):
    log_parser = FirebaseTestLogFileParser(empty_file_path)
    log_parser.lint_lines = [valid_lint_lines.get("firebase_lint")[5]]
    log_parser.log_lines = [invalid_lint_lines.get("firebase_lint")[5]]
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_firebase_test_clean_lint_error_lines_with_invalid_line_fifth_group(valid_lint_lines,
                                                                            invalid_lint_lines,
                                                                            empty_file_path):
    log_parser = FirebaseTestLogFileParser(empty_file_path)
    log_parser.lint_lines = [valid_lint_lines.get("firebase_lint")[5]]
    log_parser.log_lines = [invalid_lint_lines.get("firebase_lint")[3]]
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_firebase_test_clean_lint_error_lines_with_invalid_line_sixth_group(valid_lint_lines,
                                                                            invalid_lint_lines,
                                                                            empty_file_path):
    log_parser = FirebaseTestLogFileParser(empty_file_path)
    log_parser.lint_lines = [valid_lint_lines.get("firebase_lint")[5]]
    log_parser.log_lines = [invalid_lint_lines.get("firebase_lint")[4]]
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_firebase_test_clean_lint_error_lines_with_empty_lines(empty_file_path):
    log_parser = FirebaseTestLogFileParser(empty_file_path)
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_firebase_test_output_lint_lines_to_file_with_valid_lines(empty_file_path,
                                                                  firebase_test_log_file_parser_parameters):
    device_name = firebase_test_log_file_parser_parameters.get("valid_device_name")
    text_output_file_name = firebase_test_log_file_parser_parameters.get("valid_text_output_file_name")
    log_parser = FirebaseTestLogFileParser(empty_file_path, device_name=device_name)
    assert log_parser.text_output_file_name == text_output_file_name


def test_firebase_test_parser_name_assembled_with_valid_device_name(empty_file_path,
                                                                    firebase_test_log_file_parser_parameters):
    device_name = firebase_test_log_file_parser_parameters.get("valid_device_name")
    parser_name = firebase_test_log_file_parser_parameters.get("valid_parser_name")
    log_parser = FirebaseTestLogFileParser(empty_file_path, device_name=device_name)
    assert log_parser.parser_name == parser_name


def test_firebase_test_crash_log_file_parser_init_with_valid_values(firebase_valid_file_path,
                                                                    firebase_test_crash_log_file_parser_parameters):
    log_parser = FirebaseTestCrashLogFileParser(firebase_valid_file_path.get("firebase_test_crash_lint_valid_path"))
    assert log_parser.parser_name == firebase_test_crash_log_file_parser_parameters.get("parser_name")
    file_parser_parameters = firebase_test_crash_log_file_parser_parameters.get("file_parser")
    assert log_parser.log_file_parser.start_regex == file_parser_parameters.get("start_regex")
    assert log_parser.log_file_parser.stop_regex == file_parser_parameters.get("stop_regex")
    assert log_parser.log_file_parser.parse_regex == file_parser_parameters.get("parse_regex")
    lint_parser_parameters = firebase_test_crash_log_file_parser_parameters.get("lint_parser")
    assert log_parser.lint_parser.start_regex == lint_parser_parameters.get("start_regex")
    assert log_parser.lint_parser.stop_regex == lint_parser_parameters.get("stop_regex")
    assert log_parser.lint_parser.parse_regex == lint_parser_parameters.get("parse_regex")


def test_firebase_test_crash_log_file_parser_with_valid_file(firebase_valid_file_path, valid_lint_lines,
                                                             mock_file_write_functions):
    log_parser = FirebaseTestCrashLogFileParser(firebase_valid_file_path.get("firebase_test_crash_lint_valid_path"))
    log_parser.log_parser()
    print(''.join(log_parser.formatted_lines))
    assert len(log_parser.formatted_lines) == 14
    assert valid_lint_lines.get("firebase_test_crash_lint")[2] in log_parser.formatted_lines
    assert valid_lint_lines.get("firebase_test_crash_lint")[10] in log_parser.formatted_lines


def test_firebase_test_crash_log_file_parser_with_second_valid_file(firebase_valid_file_path, valid_lint_lines,
                                                                    mock_file_write_functions):
    log_parser = FirebaseTestCrashLogFileParser(
        firebase_valid_file_path.get("firebase_test_crash_second_lint_valid_path"))
    log_parser.log_parser()
    print(''.join(log_parser.formatted_lines))
    assert len(log_parser.formatted_lines) == 14
    assert valid_lint_lines.get("firebase_test_crash_lint")[9] in log_parser.formatted_lines
    assert valid_lint_lines.get("firebase_test_crash_lint")[10] in log_parser.formatted_lines


def test_firebase_test_crash_log_file_parser_with_clean_file(firebase_valid_file_path,
                                                             mock_file_write_functions):
    log_parser = FirebaseTestCrashLogFileParser(firebase_valid_file_path.get("firebase_lint_test_clean_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_firebase_test_crash_clean_lint_error_lines_with_valid_lint_line(valid_lint_lines,
                                                                         valid_stop_lines,
                                                                         empty_file_path):
    log_parser = FirebaseTestCrashLogFileParser(empty_file_path)
    log_parser.lint_lines = [valid_stop_lines.get("firebase_test_crash_lint")[0]]
    log_parser.log_lines = valid_lint_lines.get("firebase_test_crash_lint")
    log_parser.clean_lint_error_lines()
    assert valid_lint_lines.get("firebase_test_crash_lint")[2] == log_parser.lint_errors[0]


def test_firebase_test_crash_clean_lint_error_lines_with_empty_lint_lines(valid_lint_lines,
                                                                          empty_file_path):
    log_parser = FirebaseTestCrashLogFileParser(empty_file_path)
    log_parser.lint_lines = []
    log_parser.log_lines = valid_lint_lines.get("firebase_test_crash_lint")
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_firebase_test_crash_clean_lint_error_lines_with_empty_log_lines(empty_file_path):
    log_parser = FirebaseTestCrashLogFileParser(empty_file_path)
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_firebase_test_crash_output_lint_lines_to_file_with_valid_lines(
        empty_file_path,
        firebase_test_crash_log_file_parser_parameters):
    device_name = firebase_test_crash_log_file_parser_parameters.get("valid_device_name")
    text_output_file_name = firebase_test_crash_log_file_parser_parameters.get("valid_text_output_file_name")
    log_parser = FirebaseTestCrashLogFileParser(empty_file_path, device_name=device_name)
    assert log_parser.text_output_file_name == text_output_file_name


def test_firebase_test_crash_parser_name_assembled_with_valid_device_name(
        empty_file_path,
        firebase_test_crash_log_file_parser_parameters):
    device_name = firebase_test_crash_log_file_parser_parameters.get("valid_device_name")
    parser_name = firebase_test_crash_log_file_parser_parameters.get("valid_parser_name")
    log_parser = FirebaseTestCrashLogFileParser(empty_file_path, device_name=device_name)
    assert log_parser.parser_name == parser_name


def test_firebase_test_timeout_log_file_parser_init_with_valid_values(firebase_valid_file_path,
                                                                      firebase_test_timeout_log_file_parser_parameters):
    log_parser = FirebaseTestTimeoutLogFileParser(firebase_valid_file_path.get("firebase_test_timeout_lint_valid_path"))
    assert log_parser.parser_name == firebase_test_timeout_log_file_parser_parameters.get("parser_name")
    lint_parser_parameters = firebase_test_timeout_log_file_parser_parameters.get("lint_parser")
    assert log_parser.lint_parser.start_regex == lint_parser_parameters.get("start_regex")
    assert log_parser.lint_parser.stop_regex == lint_parser_parameters.get("stop_regex")
    assert log_parser.lint_parser.parse_regex == lint_parser_parameters.get("parse_regex")


def test_firebase_test_timeout_log_file_parser_with_valid_file(firebase_valid_file_path, valid_lint_lines,
                                                               mock_file_write_functions):
    log_parser = FirebaseTestTimeoutLogFileParser(firebase_valid_file_path.get("firebase_test_timeout_lint_valid_path"))
    log_parser.log_parser()
    print(''.join(log_parser.formatted_lines))
    assert len(log_parser.formatted_lines) == 15
    assert valid_lint_lines.get("firebase_test_timeout_lint")[1] in log_parser.formatted_lines
    assert valid_lint_lines.get("firebase_test_timeout_lint")[7] in log_parser.formatted_lines


def test_firebase_test_timeout_log_file_parser_with_clean_file(firebase_valid_file_path,
                                                               mock_file_write_functions):
    log_parser = FirebaseTestTimeoutLogFileParser(firebase_valid_file_path.get("firebase_lint_test_clean_valid_path"))
    log_parser.log_parser()
    assert not log_parser.formatted_lines


def test_firebase_test_timeout_clean_lint_error_lines_with_no_lint_line(valid_lint_lines,
                                                                        empty_file_path):
    log_parser = FirebaseTestTimeoutLogFileParser(empty_file_path)
    log_parser.lint_lines = []
    log_parser.log_lines = valid_lint_lines.get("firebase_test_timeout_lint")
    log_parser.clean_lint_error_lines()
    assert valid_lint_lines.get("firebase_test_timeout_lint")[1] == log_parser.lint_errors[2]


def test_firebase_test_timeout_clean_lint_error_lines_with_lint_line(valid_lint_lines,
                                                                     valid_stop_lines,
                                                                     empty_file_path):
    log_parser = FirebaseTestTimeoutLogFileParser(empty_file_path)
    log_parser.lint_lines = [valid_stop_lines.get("firebase_test_timeout_lint")[0]]
    log_parser.log_lines = valid_lint_lines.get("firebase_test_timeout_lint")
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_firebase_test_timeout_clean_lint_error_lines_with_empty_log_lines(empty_file_path):
    log_parser = FirebaseTestTimeoutLogFileParser(empty_file_path)
    log_parser.clean_lint_error_lines()
    assert not log_parser.lint_errors


def test_firebase_test_timeout_output_lint_lines_to_file_with_valid_lines(
        empty_file_path,
        firebase_test_timeout_log_file_parser_parameters):
    device_name = firebase_test_timeout_log_file_parser_parameters.get("valid_device_name")
    text_output_file_name = firebase_test_timeout_log_file_parser_parameters.get("valid_text_output_file_name")
    log_parser = FirebaseTestTimeoutLogFileParser(empty_file_path, device_name=device_name)
    assert log_parser.text_output_file_name == text_output_file_name


def test_firebase_test_timeout_parser_name_assembled_with_valid_device_name(
        empty_file_path,
        firebase_test_timeout_log_file_parser_parameters):
    device_name = firebase_test_timeout_log_file_parser_parameters.get("valid_device_name")
    parser_name = firebase_test_timeout_log_file_parser_parameters.get("valid_parser_name")
    log_parser = FirebaseTestTimeoutLogFileParser(empty_file_path, device_name=device_name)
    assert log_parser.parser_name == parser_name
