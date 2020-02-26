from ci_output_parser.log_file_parsers.regex_log_file_parser import RegexLogFileParser


class GTestLogFileParser(RegexLogFileParser):
    def __init__(self, log_file_path=None, parser_name="GTest Tests", output_file_name=None):
        file_parser_parameters = dict(start_regex=r'^Running main\(\) from gtest_main\.cc',
                                      stop_regex=r'Check test results',
                                      parse_regex=r'.*')
        lint_error_parser_parameters = dict(start_regex=None,
                                            stop_regex=None,
                                            parse_regex=r'warning|Warning|error|Error|FAILED')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name, output_file_name=output_file_name,
                         file_parser_parameters=file_parser_parameters,
                         lint_error_parser_parameters=lint_error_parser_parameters)

    def clean_lint_error_lines(self):
        if self.lint_errors:
            self.lint_errors = self.lint_lines
