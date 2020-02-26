import sys

from ci_output_parser.log_file_parsers.android_log_file_parser import AndroidAppLogFileParser, \
    AndroidModelsLogFileParser, AndroidBuildLogFileParser, AndroidKotlinLogFileParser, AndroidDebugJavacLogFileParser, \
    AndroidReleaseJavacLogFileParser
from ci_output_parser.log_file_parsers.firebase_log_file_parser import FirebaseBucketLogFileParser, \
    FirebaseDeviceLogFileParser, FirebaseTestLogFileParser, FirebaseTestCrashLogFileParser, \
    FirebaseTestTimeoutLogFileParser
from ci_output_parser.log_file_parsers.gtest_log_file_parser import GTestLogFileParser
from ci_output_parser.log_file_parsers.junit_log_file_parser import JUnitAndroidDebugLogFileParser, \
    JUnitAndroidReleaseLogFileParser
from ci_output_parser.log_file_parsers.pre_commit_log_file_parser import PreCommitDockerLogFileParser, \
    PreCommitLogLogFileParser
from ci_output_parser.log_file_parsers.vale_log_file_parser import ValeDockerLogFileParser, ValeLogFileParser


def parse_command_arguments():
    """Resolve file_path, file_type, and first_parser_parameter from command arguments"""
    file_path = None
    file_type = None
    first_parser_parameter = "Target"
    number_of_line_arguments = len(sys.argv)
    if number_of_line_arguments >= 2:
        file_path = sys.argv[1]
    if number_of_line_arguments >= 3:
        file_type = sys.argv[2]
    if number_of_line_arguments >= 4:
        first_parser_parameter = sys.argv[3]
    choose_and_run_parser_type(file_path, file_type, first_parser_parameter)


def choose_and_run_parser_type(file_path, log_file_type, first_parser_parameter="Target"):
    """Parser manager

    Args:
        file_path (string or None): Path to log file to be parsed
        log_file_type (string or None): Parser to be run against log file
        first_parser_parameter (string): First parameter to be used by parser

    """
    ci_output_parser_cli_help = "ci_output_parser file_path [ android_lint [api_version] | " \
                                "junit_android_lint [api_version] | " \
                                "pre_commit_lint | " \
                                "vale_lint | " \
                                "gtest_lint | " \
                                "firebase_lint | " \
                                "firebase_test_lint [device_name] ] \n " \
                                "The default value of the first parser parameter is 'Target' "
    if file_path is None:
        raise ValueError(ci_output_parser_cli_help)
    elif log_file_type is None:
        raise ValueError(ci_output_parser_cli_help)
    elif log_file_type == "android_lint":
        log_file_parser = AndroidAppLogFileParser(file_path, first_parser_parameter)
        log_file_parser.log_parser()
        log_file_parser = AndroidModelsLogFileParser(file_path, first_parser_parameter)
        log_file_parser.log_parser()
        log_file_parser = AndroidBuildLogFileParser(file_path, first_parser_parameter)
        log_file_parser.log_parser()
        log_file_parser = AndroidKotlinLogFileParser(file_path, first_parser_parameter)
        log_file_parser.log_parser()
        log_file_parser = AndroidDebugJavacLogFileParser(file_path, first_parser_parameter)
        log_file_parser.log_parser()
        log_file_parser = AndroidReleaseJavacLogFileParser(file_path, first_parser_parameter)
        log_file_parser.log_parser()
        exit(0)
    elif log_file_type == "junit_android_lint":
        log_file_parser = JUnitAndroidDebugLogFileParser(file_path, first_parser_parameter)
        log_file_parser.log_parser()
        log_file_parser = JUnitAndroidReleaseLogFileParser(file_path, first_parser_parameter)
        log_file_parser.log_parser()
        exit(0)
    elif log_file_type == "pre_commit_lint":
        log_file_parser = PreCommitLogLogFileParser(file_path)
        log_file_parser.log_parser()
        exit(0)
    elif log_file_type == "vale_lint":
        log_file_parser = ValeLogFileParser(file_path)
        log_file_parser.log_parser()
        exit(0)
    elif log_file_type == "gtest_lint":
        log_file_parser = GTestLogFileParser(file_path)
        log_file_parser.log_parser()
        exit(0)
    elif log_file_type == "firebase_lint":
        log_file_parser = FirebaseBucketLogFileParser(file_path)
        log_file_parser.log_parser()
        log_file_parser = FirebaseDeviceLogFileParser(file_path)
        log_file_parser.log_parser()
        exit(0)
    elif log_file_type == "firebase_test_lint":
        log_file_parser = FirebaseTestLogFileParser(file_path, first_parser_parameter)
        log_file_parser.log_parser()
        log_file_parser = FirebaseTestCrashLogFileParser(file_path, first_parser_parameter)
        log_file_parser.log_parser()
        log_file_parser = FirebaseTestTimeoutLogFileParser(file_path, first_parser_parameter)
        log_file_parser.log_parser()
        exit(0)
    else:
        raise ValueError(ci_output_parser_cli_help)
