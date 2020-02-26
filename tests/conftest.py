import os

import pytest

from ci_output_parser.log_file_parsers.log_file_parser import LogFileParser


@pytest.fixture
def mock_file_write_functions(mocker):
    mocker.patch.object(LogFileParser, 'output_lint_lines_to_file', return_value=True)
    mocker.patch.object(LogFileParser, 'output_lint_lines_to_json_file', return_value=True)


@pytest.fixture
def dummy_data_directory_path():
    test_directory = os.path.dirname(os.path.abspath(__file__))
    dummy_data_directory_relative_path = "dummy_data"
    dummy_data_directory_path = os.path.join(test_directory, dummy_data_directory_relative_path)
    return dummy_data_directory_path


@pytest.fixture
def invalid_file_path(dummy_data_directory_path):
    docker_dummy_data_directory = os.path.join(dummy_data_directory_path, "docker")
    relative_path = "bb_docker_invalid_dummy_log_text.txt"
    return os.path.join(docker_dummy_data_directory, relative_path)


@pytest.fixture
def empty_file_path(dummy_data_directory_path):
    docker_dummy_data_directory = os.path.join(dummy_data_directory_path, "docker")
    relative_path = "bb_docker_empty_log_text.txt"
    return os.path.join(docker_dummy_data_directory, relative_path)


@pytest.fixture
def docker_valid_file_path(dummy_data_directory_path):
    docker_dummy_data_directory = os.path.join(dummy_data_directory_path, "docker")
    docker_valid_path = os.path.join(
        docker_dummy_data_directory, "bb_docker_dummy_log_text.txt")
    docker_clean_valid_path = os.path.join(
        docker_dummy_data_directory, "docker_clean_log_text.txt")
    docker_valid_file_path = {
        "docker_valid_path": docker_valid_path,
        "docker_clean_valid_path": docker_clean_valid_path
    }
    return docker_valid_file_path


@pytest.fixture
def cmake_valid_file_path(dummy_data_directory_path):
    docker_dummy_data_directory = os.path.join(dummy_data_directory_path, "docker")
    docker_cmake_valid_path = os.path.join(
        docker_dummy_data_directory, "docker_cmake_source_error_log_text.txt")
    cmake_valid_file_path = {
        "docker_cmake_valid_path": docker_cmake_valid_path
    }
    return cmake_valid_file_path


@pytest.fixture
def android_valid_file_path(dummy_data_directory_path):
    android_dummy_data_directory = os.path.join(dummy_data_directory_path, "android")
    android_pass_lint_relative_path = "android_dummy_pass_log_text.txt"
    android_pass_lint_valid_path = os.path.join(
        android_dummy_data_directory, android_pass_lint_relative_path)
    android_fail_lint_relative_path = "android_dummy_fail_log_text.txt"
    android_fail_lint_valid_path = os.path.join(
        android_dummy_data_directory, android_fail_lint_relative_path)

    android_checkstyle_lint_relative_path = "android_dummy_checkstyle_log_text.txt"
    android_checkstyle_lint_valid_path = os.path.join(
        android_dummy_data_directory, android_checkstyle_lint_relative_path)
    android_checkstyle_clean_lint_relative_path = "android_dummy_checkstyle_clean_log_text.txt"
    android_checkstyle_clean_lint_valid_path = os.path.join(
        android_dummy_data_directory, android_checkstyle_clean_lint_relative_path)

    android_clean_lint_relative_path = "android_dummy_clean_log_text.txt"
    android_clean_lint_valid_path = os.path.join(
        android_dummy_data_directory, android_clean_lint_relative_path)
    android_app_lint_fail_lint_relative_path = "android_dummy_app_lint_fail_log_text.txt"
    android_app_lint_fail_lint_valid_path = os.path.join(
        android_dummy_data_directory, android_app_lint_fail_lint_relative_path)

    android_build_lint_relative_path = "android_dummy_build_log_text.txt"
    android_build_lint_valid_path = os.path.join(
        android_dummy_data_directory, android_build_lint_relative_path)
    android_clean_build_lint_relative_path = "android_dummy_clean_build_log_text.txt"
    android_clean_build_lint_valid_path = os.path.join(
        android_dummy_data_directory, android_clean_build_lint_relative_path)
    android_warning_build_lint_relative_path = "android_dummy_warning_build_log_text.txt"
    android_warning_build_lint_valid_path = os.path.join(
        android_dummy_data_directory, android_warning_build_lint_relative_path)

    android_javac_lint_relative_path = "android_dummy_javac_log_text.txt"
    android_javac_lint_valid_path = os.path.join(
        android_dummy_data_directory, android_javac_lint_relative_path)
    android_valid_file_path = {
        "android_pass_lint_valid_path": android_pass_lint_valid_path,
        "android_fail_lint_valid_path": android_fail_lint_valid_path,
        "android_clean_lint_valid_path": android_clean_lint_valid_path,
        "android_checkstyle_lint_valid_path": android_checkstyle_lint_valid_path,
        "android_checkstyle_clean_lint_valid_path": android_checkstyle_clean_lint_valid_path,
        "android_app_lint_fail_lint_valid_path": android_app_lint_fail_lint_valid_path,
        "android_build_lint_valid_path": android_build_lint_valid_path,
        "android_clean_build_lint_valid_path": android_clean_build_lint_valid_path,
        "android_warning_build_lint_valid_path": android_warning_build_lint_valid_path,
        "android_javac_lint_valid_path": android_javac_lint_valid_path
    }
    return android_valid_file_path


@pytest.fixture
def pre_commit_valid_file_path(dummy_data_directory_path):
    pre_commit_dummy_data_directory = os.path.join(dummy_data_directory_path, "pre_commit")
    pre_commit_lint_relative_path = "pre_commit_dummy_log_text.txt"
    pre_commit_lint_valid_path = os.path.join(
        pre_commit_dummy_data_directory, pre_commit_lint_relative_path)
    pre_commit_lint_clean_relative_path = "pre_commit_dummy_clean_log_text.txt"
    pre_commit_lint_clean_valid_path = os.path.join(
        pre_commit_dummy_data_directory, pre_commit_lint_clean_relative_path)
    pre_commit_valid_file_path = {
        "pre_commit_lint_valid_path": pre_commit_lint_valid_path,
        "pre_commit_lint_clean_valid_path": pre_commit_lint_clean_valid_path
    }
    return pre_commit_valid_file_path


@pytest.fixture
def vale_valid_file_path(dummy_data_directory_path):
    vale_dummy_data_directory = os.path.join(dummy_data_directory_path, "vale")
    vale_lint_clean_relative_path = "vale_dummy_clean_log_text.txt"
    vale_lint_clean_valid_path = os.path.join(
        vale_dummy_data_directory, vale_lint_clean_relative_path)
    vale_lint_relative_path = "vale_dummy_log_text.txt"
    vale_lint_valid_path = os.path.join(
        vale_dummy_data_directory, vale_lint_relative_path)
    vale_valid_file_path = {
        "vale_lint_clean_valid_path": vale_lint_clean_valid_path,
        "vale_lint_valid_path": vale_lint_valid_path
    }
    return vale_valid_file_path


@pytest.fixture
def junit_valid_file_path(dummy_data_directory_path):
    junit_dummy_data_directory = os.path.join(dummy_data_directory_path, "junit")
    junit_lint_clean_relative_path = "junit_dummy_clean_log_text.txt"
    junit_lint_clean_valid_path = os.path.join(
        junit_dummy_data_directory, junit_lint_clean_relative_path)
    junit_lint_relative_path = "junit_dummy_log_text.txt"
    junit_lint_valid_path = os.path.join(
        junit_dummy_data_directory, junit_lint_relative_path)
    junit_valid_file_path = {
        "junit_lint_clean_valid_path": junit_lint_clean_valid_path,
        "junit_lint_valid_path": junit_lint_valid_path
    }
    return junit_valid_file_path


@pytest.fixture
def gtest_valid_file_path(dummy_data_directory_path):
    gtest_dummy_data_directory = os.path.join(dummy_data_directory_path, "gtest")
    gtest_lint_clean_relative_path = "gtest_dummy_clean_log_text.txt"
    gtest_lint_clean_valid_path = os.path.join(
        gtest_dummy_data_directory, gtest_lint_clean_relative_path)
    gtest_lint_relative_path = "gtest_dummy_log_text.txt"
    gtest_lint_valid_path = os.path.join(
        gtest_dummy_data_directory, gtest_lint_relative_path)
    gtest_valid_file_path = {
        "gtest_lint_clean_valid_path": gtest_lint_clean_valid_path,
        "gtest_lint_valid_path": gtest_lint_valid_path
    }
    return gtest_valid_file_path


@pytest.fixture
def firebase_valid_file_path(dummy_data_directory_path):
    firebase_dummy_data_directory = os.path.join(dummy_data_directory_path, "firebase")
    firebase_lint_clean_relative_path = "firebase_dummy_clean_log_text.txt"
    firebase_lint_clean_valid_path = os.path.join(
        firebase_dummy_data_directory, firebase_lint_clean_relative_path)
    firebase_lint_relative_path = "firebase_dummy_log_text.txt"
    firebase_lint_valid_path = os.path.join(
        firebase_dummy_data_directory, firebase_lint_relative_path)
    firebase_lint_test_relative_path = "firebase_dummy_test_log_text.txt"
    firebase_test_lint_valid_path = os.path.join(
        firebase_dummy_data_directory, firebase_lint_test_relative_path)
    firebase_lint_test_clean_relative_path = "firebase_dummy_test_clean_log_text.txt"
    firebase_lint_test_clean_valid_path = os.path.join(
        firebase_dummy_data_directory, firebase_lint_test_clean_relative_path)
    firebase_lint_single_test_relative_path = "firebase_dummy_single_test_log_text.txt"
    firebase_single_test_lint_valid_path = os.path.join(
        firebase_dummy_data_directory, firebase_lint_single_test_relative_path)
    firebase_lint_test_crash_relative_path = "firebase_dummy_test_crash_log_text.txt"
    firebase_test_crash_lint_valid_path = os.path.join(
        firebase_dummy_data_directory, firebase_lint_test_crash_relative_path)
    firebase_lint_test_crash_second_relative_path = "firebase_dummy_test_crash_second_log_text.txt"
    firebase_test_crash_second_lint_valid_path = os.path.join(
        firebase_dummy_data_directory, firebase_lint_test_crash_second_relative_path)
    firebase_lint_test_timeout_relative_path = "firebase_dummy_test_timeout_log_text.txt"
    firebase_test_timeout_lint_valid_path = os.path.join(
        firebase_dummy_data_directory, firebase_lint_test_timeout_relative_path)
    firebase_valid_file_path = {
        "firebase_lint_clean_valid_path": firebase_lint_clean_valid_path,
        "firebase_lint_valid_path": firebase_lint_valid_path,
        "firebase_test_lint_valid_path": firebase_test_lint_valid_path,
        "firebase_lint_test_clean_valid_path": firebase_lint_test_clean_valid_path,
        "firebase_single_test_lint_valid_path": firebase_single_test_lint_valid_path,
        "firebase_test_crash_lint_valid_path": firebase_test_crash_lint_valid_path,
        "firebase_test_crash_second_lint_valid_path": firebase_test_crash_second_lint_valid_path,
        "firebase_test_timeout_lint_valid_path": firebase_test_timeout_lint_valid_path
    }
    return firebase_valid_file_path
