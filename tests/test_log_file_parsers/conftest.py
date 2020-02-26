import pytest

from ci_output_parser.log_file_parsers.android_log_file_parser import AndroidLogFileParser
from ci_output_parser.log_file_parsers.firebase_log_file_parser import FirebaseLogFileParser
from ci_output_parser.log_file_parsers.gtest_log_file_parser import GTestLogFileParser
from ci_output_parser.log_file_parsers.junit_log_file_parser import JUnitAndroidLogFileParser
from ci_output_parser.log_file_parsers.log_file_parser import LogFileParser
from ci_output_parser.log_file_parsers.pre_commit_log_file_parser import PreCommitLogFileParser
from ci_output_parser.log_file_parsers.regex_log_file_parser import RegexLogFileParser
from ci_output_parser.log_file_parsers.vale_log_file_parser import ValeLogFileParser


@pytest.fixture
def valid_lint_lines():
    valid_lint_lines = {
        "no_errors_report": "No errors to report\n",
        "lint_lines": ["Fix End of Files.........................................................Failed\n",
                       "/src/bbtimer.cpp:15: warning: documented symbol `void Stopwatch::start' was not declared or "
                       "defined.\n",
                       " 11:13  warning  In general, use American        Google.Spelling\n",
                       "make[1]: *** [CMakeFiles/blueberry_test.dir/all] Error 2\n"],
        "pre_commit_lint": "Fix End of Files.........................................................Failed\n",
        "vale_lint": [" 11:13  warning  In general, use American        Google.Spelling\n",
                      " docs/index.md\n"],
        "android_lint": ["Ran lint on variant debug: 2 issues found\n",
                         "   Explanation for issues of type \"ButtonStyle\":\n",
                         "   Explanation for issues of type \"GradleDependency\":\n",
                         "   Explanation for issues of type \"PrivateResource\":\n"],
        "junit_android_lint": ["com.example.yorengg1.grape.ExampleUnitTest > addition_isCorrect FAILED\n",
                               "    java.lang.AssertionError: expected:<4> but was:<5>\n",
                               "4 tests completed, 1 failed\n"],
        "gtest_lint": ["[  PASSED  ] 6 tests.\n",
                       "[  FAILED  ] BBTest.checksDirExists\n",
                       " 1 FAILED TEST\n"],
        "firebase_lint": ["gs://test-lab-d8c8hmkshy1wx-kx7vffwv1h988/2020-02-05_17:14:09.593728_Blsj",
                          "seoul-26-en-portrait",
                          "beyond1-28-en-portrait",
                          "│ Failed  │ seoul-26-en-portrait   │ 10 test cases failed, 50 passed │\n",
                          "INFO: Raw results root path is: "
                          "[gs://test-lab-d8c8hmkshy1wx-kx7vffwv1h988/2020-02-05_17:14:09.593728_Blsj/]\n",
                          "There were 20 failures:\n",
                          "1) shouldGetNonZeroDBIdWhenInsertTest("
                          "com.example.yorengg1.grape.data.dao.AnnotationDaoTest)\n",
                          "gs://test-lab-d8c8hmkshy1wx-kx7vffwv1h988/2020-02-05_17:14:09.593728_Blsj\n",
                          "seoul-26-en-portrait\n",
                          "beyond1-28-en-portrait\n",
                          "There was 1 failure:\n",
                          "FAILURES!!!\n"],
        "firebase_test_crash_lint": ["INSTRUMENTATION_STATUS: test=filterImageTest\n",
                                     "INSTRUMENTATION_STATUS_CODE: 0\n",
                                     "INSTRUMENTATION_STATUS: class=com.example.yorengg1.grape.scanner.ScannerTest\n",
                                     "INSTRUMENTATION_STATUS: current=60\n",
                                     "INSTRUMENTATION_STATUS: id=AndroidJUnitRunner\n",
                                     "INSTRUMENTATION_STATUS: numtests=61\n",
                                     "INSTRUMENTATION_STATUS: stream=\n",
                                     "com.example.yorengg1.grape.scanner.ScannerTest:\n",
                                     "INSTRUMENTATION_STATUS: test=batteryLevelTest\n",
                                     "INSTRUMENTATION_STATUS_CODE: 1\n",
                                     "INSTRUMENTATION_RESULT: shortMsg=Process crashed.\n"],
        "firebase_test_timeout_lint": ["INSTRUMENTATION_STATUS: current=30\n",
                                       "INSTRUMENTATION_STATUS_CODE: 0\n",
                                       "INSTRUMENTATION_STATUS: numtests=61\n",
                                       "INSTRUMENTATION_STATUS: stream=\n",
                                       "INSTRUMENTATION_STATUS: id=AndroidJUnitRunner\n",
                                       "INSTRUMENTATION_STATUS: test=shouldReturnMoreWhenMultipleInsertTest\n",
                                       "INSTRUMENTATION_STATUS: class=com.example.yorengg1.grape.data.dao"
                                       ".BodyPartDaoTest\n",
                                       "INSTRUMENTATION_STATUS: current=31\n",
                                       "INSTRUMENTATION_STATUS_CODE: 1"],
        "android_build_lint": ["> Task :app:compileDebugKotlin FAILED\n",
                               "e: /home/circleci/project/app/src/main/java/com/example/yorengg1/grape/userinterface"
                               "/components/views/SliceModeSlider.kt: (44, 57): Unresolved reference: "
                               "currentSliceIndex\n",
                               "Exited with code exit status 1\n"],
        "android_kotlin_lint": ["w: /home/circleci/project/app/src/main/java/com/example/yorengg1/grape/userinterface"
                                "/components/views/CaptureGalleryView.kt: (32, 54): Parameter 'lifecycleOwner' is "
                                "never used\n"],
        "android_javac_lint": ["> Task :app:compileReleaseJavaWithJavac\n",
                               "/home/circleci/code/app/src/main/java/com/example/yorengg1/grape/userinterface"
                               "/SetupActivity.java:183: warning: [deprecation] getFragmentManager() in Activity has "
                               "been deprecated\n",
                               "> Task :app:compileDebugJavaWithJavac\n"]
    }
    return valid_lint_lines


@pytest.fixture
def invalid_lint_lines():
    invalid_lint_lines = {
        "lint_lines": ["Check JSON...............................................................Passed\n",
                       "warning: ignoring unsupported tag `JAVADOC_BANNER         =' at line 208, file Doxyfile\n",
                       " ---> 0a22a9616855\n",
                       "[ 62%] Building CXX object CMakeFiles/blueberry_test.dir/unittests/blueberry_tests.cpp.o\n"],
        "pre_commit_lint": ["Check JSON...............................................................Passed\n",
                            "Check for broken symlinks............................(no files to check)Skipped\n",
                            "CMakeLists.txt Diff\n"],
        "vale_lint": [" ---> 0a22a9616855\n",
                      "✔ 0 errors, 0 warnings and 0 suggestions in 1 file.\n",
                      "Step 10/26 : RUN vale ./docs &&     vale README.md &&     vale CONTRIBUTING.md &&     vale "
                      "CODE_OF_CONDUCT.md\n"],
        "android_app_lint": ["Download https://maven.google.com/com/android/tools/lint/lint/26.2.0/lint-26.2.0.jar\n",
                             "> Lint found errors in the project; aborting build.\n"],
        "gtest_lint": ["rm: cannot remove '/test_artifacts/*': No such file or directory\n",
                       "Check test results\n"],
        "firebase_lint": ["│ Passed  │ seoul-26-en-portrait   │ 60 passed                       │\n",
                          "	at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:50)\n",
                          "	at androidx.test.internal.runner.junit4.statement."
                          "RunBefores.evaluate(RunBefores.java:76)\n",
                          "	at android.app.Instrumentation$InstrumentationThread.run(Instrumentation.java:2081)\n",
                          "	at org.mockito.internal.MockitoCore.mock(MockitoCore.java:62)\n",
                          "	at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:12)\n"]
    }
    return invalid_lint_lines


@pytest.fixture
def valid_stop_lines():
    valid_stop_lines = {
        "android_lint": ["Ran lint on variant release: 0 issues found\n",
                         "Ran lint on variant debug: 0 issues found\n"],
        "firebase_test_crash_lint": ["INSTRUMENTATION_RESULT: shortMsg=Process crashed.\n"],
        "firebase_test_timeout_lint": ["INSTRUMENTATION_CODE: 0\n"],
        "android_javac_lint": ["23 warnings\n"]
    }
    return valid_stop_lines


@pytest.fixture
def default_log_file_parser(valid_log_file_parser_fields):
    valued_log_file_parser = LogFileParser(log_file_path=valid_log_file_parser_fields.get("log_file_path"),
                                           parser_name=None,
                                           output_file_name=None)
    return valued_log_file_parser


@pytest.fixture
def default_log_file_parser_fields(docker_valid_file_path):
    default_log_file_parser_fields = {
        "log_file_path": None,
        "parser_name": "Log File Lint",
        "formatted_lines": [],
        "output_file_name": "log_file_lint",
        "text_output_file_name": "log_file_lint.txt",
        "json_output_file_name": "log_file_lint.json",
        "log_lines": [],
        "lint_lines": [],
        "lint_errors": []
    }
    return default_log_file_parser_fields


@pytest.fixture
def valid_log_file_parser_fields(docker_valid_file_path):
    valid_log_file_parser_fields = {
        "log_file_path": docker_valid_file_path.get("docker_valid_path"),
        "parser_name": "Pre-Commit Lint",
        "formatted_lines": ['\n', '## Log File Lint\n', '\n',
                            '```\n', 'Lint Error\n', '```\n'],
        "output_file_name": "pre_commit_lint",
        "text_output_file_name": "pre_commit_lint.txt",
        "json_output_file_name": "pre_commit_lint.json",
        "log_lines": [],
        "lint_lines": [],
        "lint_errors": ["Lint Error\n"]
    }
    return valid_log_file_parser_fields


@pytest.fixture
def empty_lint_dictionary(valid_lint_format, valid_lint_lines):
    lint_lines = []
    empty_json_dictionary_body = ''.join(lint_lines)
    empty_lint_dictionary = {"body": empty_json_dictionary_body}
    return empty_lint_dictionary


@pytest.fixture
def valid_lint_format():
    valid_lint_format = {
        "parser_name": "Doxygen Lint",
        "header_divider": "\n",
        "parser_name_formatted": "## Doxygen Lint\n",
        "no_parser_name_formatted": "## \n",
        "lint_comment_block": "```\n"
    }
    return valid_lint_format


@pytest.fixture
def mock_output_files(tmpdir, default_log_file_parser_fields):
    mock_output_text_file_name = default_log_file_parser_fields.get("text_output_file_name")
    mock_output_text_file = tmpdir.join(mock_output_text_file_name)
    mock_output_json_file_name = default_log_file_parser_fields.get("json_output_file_name")
    mock_output_json_file = tmpdir.join(mock_output_json_file_name)
    mock_output_files = {
        "mock_output_text_file": mock_output_text_file,
        "mock_output_json_file": mock_output_json_file
    }
    return mock_output_files


@pytest.fixture
def default_regex_log_file_parser(valid_log_file_parser_fields):
    default_regex_log_file_parser = RegexLogFileParser(log_file_path=valid_log_file_parser_fields.get("log_file_path"),
                                                       parser_name=None,
                                                       output_file_name=None,
                                                       file_parser_parameters=None,
                                                       log_line_parser_parameters=None,
                                                       lint_error_parser_parameters=None,
                                                       clean_lint_error_parser_parameters=None)
    return default_regex_log_file_parser


@pytest.fixture
def valid_regex_log_file_parser(valid_log_file_parser_fields, valid_regex_log_file_parser_parameters):
    valid_regex_log_file_parser = RegexLogFileParser(
        log_file_path=valid_log_file_parser_fields.get("log_file_path"),
        parser_name=valid_log_file_parser_fields.get("parser_name"),
        output_file_name=None,
        file_parser_parameters=valid_regex_log_file_parser_parameters.get("file_parser_parameters"),
        log_line_parser_parameters=valid_regex_log_file_parser_parameters.get("log_line_parser_parameters"),
        lint_error_parser_parameters=valid_regex_log_file_parser_parameters.get("lint_error_parser_parameters"),
        clean_lint_error_parser_parameters=valid_regex_log_file_parser_parameters.get(
            "clean_lint_error_parser_parameters"))
    return valid_regex_log_file_parser


@pytest.fixture
def default_regex_log_file_parser_parameters():
    default_regex_log_file_parser_parameters = dict(start_regex=None,
                                                    stop_regex=None,
                                                    parse_regex=r'.*')
    return default_regex_log_file_parser_parameters


@pytest.fixture
def valid_regex_log_file_parser_parameters():
    valid_regex_log_file_parser_parameters = {
        "file_parser_parameters": dict(start_regex=r'pre-commit run',
                                       stop_regex=r'Removing intermediate container|non-zero code',
                                       parse_regex=r'.*'),
        "log_line_parser_parameters": dict(start_regex=r'Passed|Failed|Skipped$',
                                           stop_regex=r'^ ---> ',
                                           parse_regex=r'.*'),
        "lint_error_parser_parameters": dict(start_regex=r'Failed$',
                                             stop_regex=r'^ ---> ',
                                             parse_regex=r'.*'),
        "clean_lint_error_parser_parameters": dict(start_regex=r'^Fix',
                                                   stop_regex=r'^hookid',
                                                   parse_regex=r'.*')
    }
    return valid_regex_log_file_parser_parameters


@pytest.fixture
def valid_regex_log_file_parser_lines():
    valid_regex_log_file_parser_lines = {
        "log_lines": ["Check JSON...............................................................Passed\n",
                      "Check for broken symlinks............................(no files to check)Skipped\n",
                      "Fix End of Files.........................................................Failed\n",
                      "hookid: end-of-file-fixer\n",
                      " ---> 0a22a9616855\n",
                      "CMakeLists.txt Diff\n"],
        "lint_lines": ["Check JSON...............................................................Passed\n",
                       "Check for broken symlinks............................(no files to check)Skipped\n",
                       "Fix End of Files.........................................................Failed\n",
                       "hookid: end-of-file-fixer\n"],
        "lint_errors": ["Fix End of Files.........................................................Failed\n",
                        "hookid: end-of-file-fixer\n"],
        "clean_lint_errors": ["Fix End of Files.........................................................Failed\n"],
        "formatted_lines": ["\n",
                            "## Pre-Commit Lint\n",
                            "\n",
                            "```\n",
                            "Fix End of Files.........................................................Failed\n",
                            "```\n"]
    }
    return valid_regex_log_file_parser_lines


@pytest.fixture
def valid_lint_dictionary(valid_lint_format, valid_lint_lines):
    lint_lines = [valid_lint_format.get("header_divider"),
                  valid_lint_format.get("parser_name_formatted"),
                  valid_lint_format.get("header_divider"),
                  valid_lint_format.get("lint_comment_block"),
                  valid_lint_lines.get("no_errors_report"),
                  valid_lint_format.get("lint_comment_block")]
    valid_json_dictionary_body = ''.join(lint_lines)
    valid_lint_dictionary = {"body": valid_json_dictionary_body}
    return valid_lint_dictionary


@pytest.fixture
def default_pre_commit_log_file_parser(valid_log_file_parser_fields):
    default_pre_commit_log_file_parser = PreCommitLogFileParser(
        log_file_path=valid_log_file_parser_fields.get("log_file_path"))
    return default_pre_commit_log_file_parser


@pytest.fixture
def pre_commit_log_log_file_parser_parameters():
    pre_commit_log_log_file_parser_parameters = {
        "log_line_parser": dict(start_regex=r'Passed|Failed|Skipped$',
                                stop_regex=r'^ ---> ',
                                parse_regex=r'.*')
    }
    return pre_commit_log_log_file_parser_parameters


@pytest.fixture
def pre_commit_docker_log_file_parser_parameters():
    pre_commit_docker_log_file_parser_parameters = {
        "file_parser": dict(start_regex=r'pre-commit run',
                            stop_regex=r'Removing intermediate container|non-zero code',
                            parse_regex=r'.*'),
        "log_line_parser": dict(start_regex=r'Passed|Failed|Skipped$',
                                stop_regex=r'^ ---> ',
                                parse_regex=r'.*')
    }
    return pre_commit_docker_log_file_parser_parameters


@pytest.fixture
def default_android_log_file_parser(valid_log_file_parser_fields):
    default_android_log_file_parser = AndroidLogFileParser(
        log_file_path=valid_log_file_parser_fields.get("log_file_path"))
    return default_android_log_file_parser


@pytest.fixture
def android_log_file_parser_parameters():
    android_log_file_parser_parameters = {
        "parser_name": "Android API Target Lint",
        "log_line_parser": dict(start_regex=None,
                                stop_regex=None,
                                parse_regex=r'^(?!Download)'),
        "lint_error_parser": dict(start_regex=None,
                                  stop_regex=r'> Lint found errors in the project; aborting build\.',
                                  parse_regex=r'.*')
    }
    return android_log_file_parser_parameters


@pytest.fixture
def android_app_log_file_parser_parameters():
    android_app_log_file_parser_parameters = {
        "file_parser": dict(start_regex=r'^:app:lint|> Task :app:lint',
                            stop_regex=r'^Wrote HTML report to|No issues found',
                            parse_regex=r'.*')
    }
    return android_app_log_file_parser_parameters


@pytest.fixture
def android_models_log_file_parser_parameters():
    android_models_log_file_parser_parameters = {
        "file_parser": dict(start_regex=r'^:models:lint|> Task :models:lint',
                            stop_regex=r'^Wrote HTML report to|BUILD SUCCESSFUL',
                            parse_regex=r'.*')
    }
    return android_models_log_file_parser_parameters


@pytest.fixture
def default_vale_log_file_parser(valid_log_file_parser_fields):
    default_vale_log_file_parser = ValeLogFileParser(
        log_file_path=valid_log_file_parser_fields.get("log_file_path"))
    return default_vale_log_file_parser


@pytest.fixture
def vale_log_file_parser_parameters():
    vale_log_file_parser_parameters = {
        "parser_name": "Vale Lint",
    }
    return vale_log_file_parser_parameters


@pytest.fixture
def vale_docker_log_file_parser_parameters():
    vale_docker_log_file_parser_parameters = {
        "file_parser": dict(start_regex=r'vale.*docs',
                            stop_regex=r'Removing intermediate container|non-zero code',
                            parse_regex=r'.*')
    }
    return vale_docker_log_file_parser_parameters


@pytest.fixture
def default_junit_android_log_file_parser(valid_log_file_parser_fields):
    default_junit_android_log_file_parser = JUnitAndroidLogFileParser(
        log_file_path=valid_log_file_parser_fields.get("log_file_path"))
    return default_junit_android_log_file_parser


@pytest.fixture
def junit_android_log_file_parser_parameters():
    junit_android_log_file_parser_parameters = {
        "parser_name": "Android API Target Tests",
        "log_line_parser": dict(start_regex=r'^Successfully started process \'Gradle Test Executor',
                                stop_regex=r'^Finished generating test XML results',
                                parse_regex=r'.*'),
        "lint_error_parser": dict(start_regex=None,
                                  stop_regex=None,
                                  parse_regex=r'^(?!Successfully started process)')
    }
    return junit_android_log_file_parser_parameters


@pytest.fixture
def junit_android_debug_log_file_parser_parameters():
    junit_android_debug_log_file_parser_parameters = {
        "file_parser": dict(start_regex=r'^:app:testDebugUnitTest',
                            stop_regex=None,
                            parse_regex=r'.*')
    }
    return junit_android_debug_log_file_parser_parameters


@pytest.fixture
def junit_android_release_log_file_parser_parameters():
    junit_android_release_log_file_parser_parameters = {
        "file_parser": dict(start_regex=r'^:app:testReleaseUnitTest',
                            stop_regex=None,
                            parse_regex=r'.*')
    }
    return junit_android_release_log_file_parser_parameters


@pytest.fixture
def default_gtest_log_file_parser(valid_log_file_parser_fields):
    default_gtest_log_file_parser = GTestLogFileParser(
        log_file_path=valid_log_file_parser_fields.get("log_file_path"))
    return default_gtest_log_file_parser


@pytest.fixture
def gtest_log_file_parser_parameters():
    gtest_log_file_parser_parameters = {
        "parser_name": "GTest Tests",
        "file_parser": dict(start_regex=r'^Running main\(\) from gtest_main\.cc',
                            stop_regex=r'Check test results',
                            parse_regex=r'.*'),
        "lint_error_parser": dict(start_regex=None,
                                  stop_regex=None,
                                  parse_regex=r'warning|Warning|error|Error|FAILED')
    }
    return gtest_log_file_parser_parameters


@pytest.fixture
def default_firebase_log_file_parser(valid_log_file_parser_fields):
    default_firebase_log_file_parser = FirebaseLogFileParser(
        log_file_path=valid_log_file_parser_fields.get("log_file_path"))
    return default_firebase_log_file_parser


@pytest.fixture
def firebase_log_file_parser_parameters():
    firebase_log_file_parser_parameters = {
        "parser_name": "Firebase Lint"
    }
    return firebase_log_file_parser_parameters


@pytest.fixture
def firebase_bucket_log_file_parser_parameters():
    firebase_bucket_log_file_parser_parameters = {
        "lint_parser": dict(start_regex=None,
                            stop_regex=None,
                            parse_regex=r'gs:\/\/.*')
    }
    return firebase_bucket_log_file_parser_parameters


@pytest.fixture
def firebase_device_log_file_parser_parameters():
    firebase_device_log_file_parser_parameters = {
        "file_parser": dict(start_regex=None,
                            stop_regex=None,
                            parse_regex=r'Failed')
    }
    return firebase_device_log_file_parser_parameters


@pytest.fixture
def firebase_test_log_file_parser_parameters():
    firebase_test_log_file_parser_parameters = {
        "parser_name": "Firebase Device Tests",
        "file_parser": dict(start_regex=r'^There were|There was',
                            stop_regex=r'^INSTRUMENTATION_CODE',
                            parse_regex=r'.*'),
        "valid_text_output_file_name": "firebase_seoul_26_en_portrait_tests.txt",
        "valid_device_name": "seoul-26-en-portrait",
        "valid_parser_name": "Firebase seoul-26-en-portrait Tests"
    }
    return firebase_test_log_file_parser_parameters


@pytest.fixture
def firebase_test_crash_log_file_parser_parameters():
    firebase_test_crash_log_file_parser_parameters = {
        "parser_name": "Firebase Device Tests",
        "file_parser": dict(start_regex=None,
                            stop_regex=r'^INSTRUMENTATION_CODE',
                            parse_regex=r'.*'),
        "lint_parser": dict(start_regex=None,
                            stop_regex=None,
                            parse_regex=r'shortMsg=Process crashed'),
        "valid_text_output_file_name": "firebase_seoul_26_en_portrait_tests.txt",
        "valid_device_name": "seoul-26-en-portrait",
        "valid_parser_name": "Firebase seoul-26-en-portrait Tests"
    }
    return firebase_test_crash_log_file_parser_parameters


@pytest.fixture
def firebase_test_timeout_log_file_parser_parameters():
    firebase_test_timeout_log_file_parser_parameters = {
        "parser_name": "Firebase Device Tests",
        "lint_parser": dict(start_regex=None,
                            stop_regex=None,
                            parse_regex=r'INSTRUMENTATION_CODE:'),
        "valid_text_output_file_name": "firebase_seoul_26_en_portrait_tests.txt",
        "valid_device_name": "seoul-26-en-portrait",
        "valid_parser_name": "Firebase seoul-26-en-portrait Tests"
    }
    return firebase_test_timeout_log_file_parser_parameters


@pytest.fixture
def android_build_log_file_parser_parameters():
    android_build_log_file_parser_parameters = {
        "parser_name": "Android API Target Build Lint",
        "file_parser": dict(start_regex=r'^> Task .* FAILED\n$',
                            stop_regex=None,
                            parse_regex=r'.*')
    }
    return android_build_log_file_parser_parameters


@pytest.fixture
def android_kotlin_log_file_parser_parameters():
    android_kotlin_log_file_parser_parameters = {
        "parser_name": "Android API Target Kotlin Lint",
        "file_parser": dict(start_regex=None,
                            stop_regex=None,
                            parse_regex=r'^w: ')
    }
    return android_kotlin_log_file_parser_parameters


@pytest.fixture
def android_javac_log_file_parser_parameters():
    android_javac_log_file_parser_parameters = {
        "parser_name": "Android API Target Javac Lint",
        "lint_parser": dict(start_regex=None,
                            stop_regex=None,
                            parse_regex=r'^[0-9]+ warnings$')
    }
    return android_javac_log_file_parser_parameters


@pytest.fixture
def android_debug_javac_log_file_parser_parameters():
    android_debug_javac_log_file_parser_parameters = {
        "parser_name": "Android API Target Debug Javac Lint",
        "file_parser": dict(start_regex=r'^> Task :app:compileDebugJavaWithJavac',
                            stop_regex=r'^[0-9]+ warnings$',
                            parse_regex=r'.*')
    }
    return android_debug_javac_log_file_parser_parameters


@pytest.fixture
def android_release_javac_log_file_parser_parameters():
    android_release_javac_log_file_parser_parameters = {
        "parser_name": "Android API Target Release Javac Lint",
        "file_parser": dict(start_regex=r'^> Task :app:compileReleaseJavaWithJavac',
                            stop_regex=r'^[0-9]+ warnings$',
                            parse_regex=r'.*')
    }
    return android_release_javac_log_file_parser_parameters
