import sys
import pytest

from ci_output_parser import cli_manager


def test_choose_and_run_parser_type_with_file_path(docker_valid_file_path, mock_file_write_functions):
    with pytest.raises(SystemExit):
        cli_manager.choose_and_run_parser_type(docker_valid_file_path.get("docker_valid_path"), None)


def test_choose_and_run_parser_type_with_no_file_path(parser_log_file_types):
    with pytest.raises(ValueError, match=parser_log_file_types.get("no_parser_error")):
        cli_manager.choose_and_run_parser_type(None, None)


def test_choose_and_run_parser_type_with_invalid_log_file_type(docker_valid_file_path, parser_log_file_types):
    with pytest.raises(ValueError, match=parser_log_file_types.get("no_parser_error")):
        cli_manager.choose_and_run_parser_type(
            docker_valid_file_path.get("docker_valid_path"),
            parser_log_file_types.get("api_version"))


def test_choose_and_run_parser_type_with_no_file_path_or_file_type(parser_log_file_types):
    with pytest.raises(ValueError, match=parser_log_file_types.get("no_parser_error")):
        cli_manager.choose_and_run_parser_type(None, None)


def test_choose_and_run_parser_type_with_log_file_type_docker(docker_valid_file_path, parser_log_file_types,
                                                              mock_file_write_functions):
    with pytest.raises(SystemExit):
        cli_manager.choose_and_run_parser_type(
            docker_valid_file_path.get("docker_valid_path"),
            parser_log_file_types.get("docker_build"))


def test_choose_and_run_parser_type_with_log_file_type_android(android_valid_file_path, parser_log_file_types,
                                                               mock_file_write_functions):
    with pytest.raises(SystemExit):
        cli_manager.choose_and_run_parser_type(
            android_valid_file_path.get("android_pass_lint_valid_path"),
            parser_log_file_types.get("android_lint"))


def test_choose_and_run_parser_type_with_log_file_type_pre_commit(pre_commit_valid_file_path, parser_log_file_types,
                                                                  mock_file_write_functions):
    with pytest.raises(SystemExit):
        cli_manager.choose_and_run_parser_type(
            pre_commit_valid_file_path.get("pre_commit_lint_valid_path"),
            parser_log_file_types.get("pre_commit_lint"))


def test_choose_and_run_parser_type_with_log_file_type_vale(vale_valid_file_path, parser_log_file_types,
                                                            mock_file_write_functions):
    with pytest.raises(SystemExit):
        cli_manager.choose_and_run_parser_type(
            vale_valid_file_path.get("vale_lint_valid_path"),
            parser_log_file_types.get("vale_lint"))


def test_choose_and_run_parser_type_with_log_file_type_gtest_lint(gtest_valid_file_path, parser_log_file_types,
                                                                  mock_file_write_functions):
    with pytest.raises(SystemExit):
        cli_manager.choose_and_run_parser_type(
            gtest_valid_file_path.get("gtest_lint_valid_path"),
            parser_log_file_types.get("gtest_lint"))


def test_choose_and_run_parser_type_with_no_log_file_type(docker_valid_file_path, mock_file_write_functions):
    with pytest.raises(SystemExit):
        cli_manager.choose_and_run_parser_type(docker_valid_file_path.get("docker_valid_path"), None)


def test_choose_and_run_parser_type_with_log_file_type_android_and_api_version(android_valid_file_path,
                                                                               parser_log_file_types,
                                                                               mock_file_write_functions):
    with pytest.raises(SystemExit):
        cli_manager.choose_and_run_parser_type(
            android_valid_file_path.get("android_pass_lint_valid_path"),
            parser_log_file_types.get("android_lint"),
            parser_log_file_types.get("api_version"))


def test_choose_and_run_parser_type_with_log_file_type_android_and_no_api_version(android_valid_file_path,
                                                                                  parser_log_file_types,
                                                                                  mock_file_write_functions):
    with pytest.raises(SystemExit):
        cli_manager.choose_and_run_parser_type(
            android_valid_file_path.get("android_pass_lint_valid_path"),
            parser_log_file_types.get("android_lint"))


def test_choose_and_run_parser_type_with_log_file_type_junit_android_and_api_version(junit_valid_file_path,
                                                                                     parser_log_file_types,
                                                                                     mock_file_write_functions):
    with pytest.raises(SystemExit):
        cli_manager.choose_and_run_parser_type(
            junit_valid_file_path.get("junit_lint_valid_path"),
            parser_log_file_types.get("junit_android_lint"),
            parser_log_file_types.get("api_version"))


def test_choose_and_run_parser_type_with_log_file_type_junit_android_and_no_api_version(junit_valid_file_path,
                                                                                        parser_log_file_types,
                                                                                        mock_file_write_functions):
    with pytest.raises(SystemExit):
        cli_manager.choose_and_run_parser_type(
            junit_valid_file_path.get("junit_lint_valid_path"),
            parser_log_file_types.get("junit_android_lint"))


def test_choose_and_run_parser_type_with_log_file_type_firebase_test_and_device_name(firebase_valid_file_path,
                                                                                     parser_log_file_types,
                                                                                     mock_file_write_functions):
    with pytest.raises(SystemExit):
        cli_manager.choose_and_run_parser_type(
            firebase_valid_file_path.get("firebase_test_lint_valid_path"),
            parser_log_file_types.get("firebase_test_lint"),
            parser_log_file_types.get("device_name"))


def test_choose_and_run_parser_type_with_log_file_type_firebase_test_and_no_device_name(firebase_valid_file_path,
                                                                                        parser_log_file_types,
                                                                                        mock_file_write_functions):
    with pytest.raises(SystemExit):
        cli_manager.choose_and_run_parser_type(
            firebase_valid_file_path.get("firebase_test_lint_valid_path"),
            parser_log_file_types.get("firebase_test_lint"))


def test_choose_and_run_parser_type_with_log_file_type_firebase(firebase_valid_file_path,
                                                                parser_log_file_types,
                                                                mock_file_write_functions):
    with pytest.raises(SystemExit):
        cli_manager.choose_and_run_parser_type(
            firebase_valid_file_path.get("firebase_lint_valid_path"),
            parser_log_file_types.get("firebase_lint"))


def test_parse_command_arguments_with_no_args(mocker, parser_command_arguments, parser_log_file_types):
    mocker.patch.object(sys, 'argv', parser_command_arguments.get("program_name"))
    with pytest.raises(ValueError, match=parser_log_file_types.get("no_parser_error")):
        cli_manager.parse_command_arguments()


def test_parse_command_arguments_with_empty_args(mocker, parser_log_file_types):
    mocker.patch.object(sys, 'argv', [])
    with pytest.raises(ValueError, match=parser_log_file_types.get("no_parser_error")):
        cli_manager.parse_command_arguments()


def test_parse_command_arguments_with_file_path(mocker, parser_command_arguments, mock_file_write_functions):
    mocker.patch.object(sys, 'argv', parser_command_arguments.get("docker_build_default"))
    with pytest.raises(SystemExit):
        cli_manager.parse_command_arguments()


def test_parse_command_arguments_with_log_file_type_docker(mocker, parser_command_arguments, mock_file_write_functions):
    mocker.patch.object(sys, 'argv', parser_command_arguments.get("docker_build"))
    with pytest.raises(SystemExit):
        cli_manager.parse_command_arguments()


def test_parse_command_arguments_with_log_file_type_android(mocker, parser_command_arguments,
                                                            mock_file_write_functions):
    mocker.patch.object(sys, 'argv', parser_command_arguments.get("android_lint_default"))
    with pytest.raises(SystemExit):
        cli_manager.parse_command_arguments()


def test_parse_command_arguments_with_android_and_api_version(mocker, parser_command_arguments,
                                                              mock_file_write_functions):
    mocker.patch.object(sys, 'argv', parser_command_arguments.get("android_lint"))
    with pytest.raises(SystemExit):
        cli_manager.parse_command_arguments()


def test_parse_command_arguments_with_log_file_type_pre_commit(mocker, parser_command_arguments,
                                                               mock_file_write_functions):
    mocker.patch.object(sys, 'argv', parser_command_arguments.get("pre_commit_lint"))
    with pytest.raises(SystemExit):
        cli_manager.parse_command_arguments()
