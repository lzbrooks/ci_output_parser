from ci_output_parser.log_file_parsers.regex_log_file_parser import RegexLogFileParser


class JUnitAndroidLogFileParser(RegexLogFileParser):
    def __init__(self, log_file_path=None, parser_name="Android API Target Tests", output_file_name=None,
                 file_parser_parameters=None):
        log_line_parser_parameters = dict(start_regex=r'^Successfully started process \'Gradle Test Executor',
                                          stop_regex=r'^Finished generating test XML results',
                                          parse_regex=r'.*')
        lint_error_parser_parameters = dict(start_regex=None,
                                            stop_regex=None,
                                            parse_regex=r'^(?!Successfully started process)')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name, output_file_name=output_file_name,
                         file_parser_parameters=file_parser_parameters,
                         log_line_parser_parameters=log_line_parser_parameters,
                         lint_error_parser_parameters=lint_error_parser_parameters)


class JUnitAndroidDebugLogFileParser(JUnitAndroidLogFileParser):
    def __init__(self, log_file_path=None, api_version="Target"):
        parser_name = "Android API " + api_version + " Debug Unit Tests"
        file_parser_parameters = dict(start_regex=r'^:app:testDebugUnitTest',
                                      stop_regex=None,
                                      parse_regex=r'.*')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name,
                         file_parser_parameters=file_parser_parameters)


class JUnitAndroidReleaseLogFileParser(JUnitAndroidLogFileParser):
    def __init__(self, log_file_path=None, api_version="Target"):
        parser_name = "Android API " + api_version + " Release Unit Tests"
        file_parser_parameters = dict(start_regex=r'^:app:testReleaseUnitTest',
                                      stop_regex=None,
                                      parse_regex=r'.*')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name,
                         file_parser_parameters=file_parser_parameters)
